from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Set your Gemini API key (Consider storing it securely in production)
os.environ["GOOGLE_API_KEY"] = "AIzaSyAYdUMOn6tZANgNWJ2wQgOkt0K3juLiqU8"

# Initialize FastAPI app
app = FastAPI()

# CORS Middleware (update 'allow_origins' in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to your domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Load and process your Markdown content ---
loader = DirectoryLoader("D:/kalyan-jewellers-1/docs", glob="**/*.md", show_progress=True)
docs = loader.load()

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_docs = splitter.split_documents(docs)

# Create embeddings and vectorstore
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(split_docs, embedding)

# Create retriever and QA chain
retriever = vectorstore.as_retriever()
llm = ChatGoogleGenerativeAI(model="gemini-pro")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# --- API endpoint ---
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()  # Parse JSON input
    question = data.get("question")  # Extract the 'question' field
    
    if not question:
        return {"error": "No question provided"}
    
    # Get the response using the QA chain
    response = qa_chain.run(question)
    
    return {"response": response}


