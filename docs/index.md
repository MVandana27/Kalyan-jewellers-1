
<div class="sidebar">
  <a href="#discover-timeless-beauty">Discover Timeless Beauty</a>
  <a href="#our-commitment-to-you">Our Commitment to You</a>
  <a href="#exclusive-services-we-offer">Exclusive Services</a>
  <a href="#visit-us">Visit Us</a>
</div>


<div class="kj-logo-wrapper">
  <div class="kj-logo-container">
    <img src="assets/images/KJ logo 1.png" class="kj-logo">
    <div class="kj-logo-aura"></div>
    <div class="kj-gemstones">
      <div class="gem gem-1">◆</div>
      <div class="gem gem-2">◆</div>
      <div class="gem gem-3">◆</div>
    </div>
    <div class="kj-light-reflections">
      <div class="light-beam beam-1"></div>
      <div class="light-beam beam-2"></div>
    </div>
  </div>
</div>

<style>
  /* Premium Centering Container */
  .kj-logo-wrapper {
    display: grid;
    place-items: center;
    min-height: 30vh; 
    margin-bottom: 15px;
    
  }

  /* Luxury Logo Container */
  .kj-logo-container {
    position: relative;
    width: max-content;
    padding: 2.0rem;
    border-radius: 50%;
    background: 
      radial-gradient(circle at center, 
        rgba(255, 255, 255, 0.03) 0%, 
        rgba(255, 255, 255, 0) 70%);
    box-shadow:
      0 0 30px rgba(212, 175, 55, 0.1),
      inset 0 0 20px rgba(212, 175, 55, 0.05);
    transform-style: preserve-3d;
    margin-top: -10vh;   
  }

  /* Main Logo Styling */
  .kj-logo {
    width: 120px;
    height: auto;
    filter: 
      drop-shadow(0 5px 15px rgba(212, 175, 55, 0.4))
      brightness(1.05);
    transform: translateZ(20px);
    transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
  }

  /* 3D Aura Effect */
  .kj-logo-aura {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: 
      radial-gradient(circle at center, 
        rgba(212, 175, 55, 0.3) 0%, 
        transparent 70%);
    opacity: 0;
    transition: opacity 0.8s ease;
    transform: translateZ(10px);
  }

  /* Diamond Gemstones */
  .kj-gemstones {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    pointer-events: none;
  }
  
  .gem {
    position: absolute;
    font-size: 1.2rem;
    color: #FFD700;
    text-shadow: 
      0 0 10px rgb(248, 215, 30),
      0 0 20px #FFF;
    opacity: 0;
    animation: gem-glint 4s infinite;
  }
  
  .gem-1 { top: 15%; left: 20%; animation-delay: 0.5s; }
  .gem-2 { top: 75%; left: 70%; animation-delay: 1s; }
  .gem-3 { bottom: 10%; right: 50%; animation-delay: 1.5s; }

  /* Light Reflection Beams */
  .kj-light-reflections {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    overflow: hidden;
    border-radius: 50%;
  }
  
  .light-beam {
    position: absolute;
    background: linear-gradient(
      90deg,
      rgba(255, 255, 255, 0) 0%,
      rgba(255, 255, 255, 0.15) 50%,
      rgba(255, 255, 255, 0) 100%
    );
    height: 2px;
    width: 40%;
    top: 50%;
    opacity: 0;
  }
  
  .beam-1 {
    left: -40%;
    transform: rotate(30deg);
    animation: light-sweep 8s infinite;
  }
  
  .beam-2 {
    right: -40%;
    transform: rotate(-30deg);
    animation: light-sweep 8s infinite 2s;
  }

  /* Animations */
  @keyframes gem-glint {
    0%, 100% { opacity: 0; transform: scale(0.8); }
    50% { opacity: 1; transform: scale(1.2); }
  }
  
  @keyframes light-sweep {
    0% { left: -40%; opacity: 0; }
    20% { opacity: 0.7; }
    50% { left: 140%; opacity: 0; }
    100% { left: 140%; opacity: 0; }
  }

  /* Hover Effects */
  .kj-logo-container:hover {
    transform: rotateY(5deg);
  }
  
  .kj-logo-container:hover .kj-logo {
    filter: 
      drop-shadow(0 8px 25px rgba(212, 175, 55, 0.6))
      brightness(1.1);
    transform: translateZ(30px) scale(1.03);
  }
  
  .kj-logo-container:hover .kj-logo-aura {
    opacity: 1;
  }

  /* Responsive Design */
  @media (max-width: 768px) {
    .kj-logo {
      width: 150px;
    }
    .kj-logo-container {
      padding: 1.8rem;
    }
  }
</style>






Kalyan Jewellers is one of India’s largest and most trusted jewelry brands, offering an extensive collection of **Gold**, **Diamond**, **Platinum**, and **Silver** jewelry. Established in 1993, Kalyan Jewellers has grown to over **300+ showrooms** across India and the Middle East, renowned for their high-quality craftsmanship and authentic designs.

<div class="gold-rates-marquee">
  <div class="gold-rates-track">
    <span>
      April 18-04-2025 | 24 KT - ₹9041 | 18 KT - ₹6788 | Platinum - ₹3192 | Silver Rates: Kerala - ₹102, Tamil Nadu - ₹104 | Silver Rate Pan India -₹102  &nbsp;&nbsp;&nbsp;
    </span>
    <span>
      April 18-04-2025 | 24 KT - ₹9041 | 18 KT - ₹6788 | Platinum - ₹3192 | Silver Rates: Kerala - ₹102, Tamil Nadu - ₹104 | Silver Rate Pan India -₹102 &nbsp;&nbsp;&nbsp;
    </span>
  </div>
</div>


<style>
.gold-rates-marquee {
  width: 100%;
  overflow: hidden;
  box-sizing: border-box;
  background: linear-gradient(90deg,rgb(177, 43, 48), #e52d27,rgb(234, 141, 94),rgb(245, 186, 77),rgb(129, 117, 82));
  padding: 12px 0;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(27, 26, 26, 0.2);
  color: white;
  font-weight: bold;
  white-space: nowrap;
}

.gold-rates-track {
  display: inline-block;
  white-space: nowrap;
  animation: scroll-marquee 9s linear infinite;
}

.gold-rates-track span {
  display: inline-block;
  padding: 0 2rem;
}

@keyframes scroll-marquee {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-50%);
  }
}
</style>

For decades, **Kalyan Jewellers** has been synonymous with purity, elegance, and exquisite craftsmanship. We take pride in offering a breathtaking collection of **gold, diamond, platinum, and gemstone jewelry**, designed to celebrate every special moment of your life.  

## **Discover Timeless Beauty**  


At **Kalyan Jewellers**, every piece is crafted with precision and passion, blending **heritage, artistry, and modern design**. Whether you're looking for a **regal bridal set, a contemporary diamond ring, or a timeless temple necklace**, we have something for every occasion.  



## **Our Commitment to You**  

- **Uncompromised Purity** – BIS-hallmarked gold and certified diamonds ensure the highest quality.  
- **Ethical Sourcing** – We uphold transparency in every piece we create.  
- **Exquisite Craftsmanship** – Jewelry handcrafted by skilled artisans with attention to detail.  



## **Exclusive Services We Offer**  

- **Custom Jewelry Design** – Bring your vision to life with a personalized touch.  
- **Jewelry Repair & Restoration** – Restore the beauty of your cherished pieces.  
- **Gold Exchange & Buyback** – Trusted, hassle-free transactions.  
- **Bridal & Wedding Collection** – Curated selections for your special day.  


## **Visit Us**  

Explore our stunning collection online or visit our nearest showroom for a personalized experience. Let **Kalyan Jewellers** help you find the perfect piece that defines your elegance and style.  





<div class="hero" markdown>

[View Collections](/category){: .custom-button }
[Book Consultation](/map/contact){: .custom-button }

</div>


<style>
/* Slide and highlight heading on hover */
h1:hover,
h2:hover,
h3:hover,
h4:hover,
h5:hover,
h6:hover {
  transform: translateX(4px); /* Slide effect */
  
  transition: all 0.3s ease-in-out;
  cursor: pointer;
  padding-inline: 4px;
  border-radius: 4px;
}
</style>





<p class="visit-text">For full details visit <a href="https://www.kalyanjewellers.net/" target="_blank">www.kalyanjewellers.org</a></p>


