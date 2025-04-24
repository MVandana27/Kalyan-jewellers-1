from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import logging
from typing import Optional

# Load environment variables
load_dotenv()

# Configuration
class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    DOCS_PATH = os.path.join(os.path.dirname(__file__), "docs")  # Relative path to docs

    @classmethod
    def validate(cls):
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        if not os.path.exists(cls.DOCS_PATH):
            raise FileNotFoundError(f"Document path not found: {cls.DOCS_PATH}")

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Data model for request validation
class ChatRequest(BaseModel):
    question: str

# Global components
qa_chain: Optional[RetrievalQA] = None

@app.on_event("startup")
async def startup_event():
    """Initialize application components"""
    global qa_chain
    
    try:
        Settings.validate()
        
        logger.info("Loading documents...")
        loader = DirectoryLoader(Settings.DOCS_PATH, glob="**/*.md", show_progress=True)
        docs = loader.load()
        
        logger.info("Splitting documents...")
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = splitter.split_documents(docs)
        
        logger.info("Creating embeddings...")
        embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        logger.info("Building vector store...")
        vectorstore = FAISS.from_documents(split_docs, embedding)
        
        logger.info("Initializing QA chain...")
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            chain_type="stuff"
        )
        logger.info("Application startup complete")
        
    except Exception as e:
        logger.error(f"Startup failed: {str(e)}")
        raise

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    """
    Handle chat requests with proper validation and error handling
    """
    if not qa_chain:
        raise HTTPException(status_code=503, detail="Service initializing, please try again later")
    
    try:
        # Validate input
        question = chat_request.question.strip()
        if not question:
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        if len(question) > 1000:
            raise HTTPException(status_code=400, detail="Question too long (max 1000 characters)")
        
        # Process question
        logger.info(f"Processing question: {question[:50]}...")
        result = qa_chain.invoke({"query": question})
        
        return {"response": result.get("result", "No answer generated")}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error processing your question")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if qa_chain else "initializing",
        "service": "chat-api",
        "version": "1.0.0"
    }


