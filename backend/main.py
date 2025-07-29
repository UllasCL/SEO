from fastapi import FastAPI, Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import requests
import os
import time
from urllib.parse import quote

from database import get_db, create_tables, Product
from models import ProductInput, ProductResponse, GenerateResponse
from seo_generator import SEOContentGenerator
from logger import logger

# Create tables on startup
logger.info("🚀 Initializing SEO Page Generator API...")
create_tables()
logger.info("✅ Database tables created/verified")

app = FastAPI(
    title="SEO Page Generator API",
    description="AI-powered SEO page generator for products and services",
    version="1.0.0"
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Log incoming request
    logger.info(f"📥 {request.method} {request.url.path} - Client: {request.client.host if request.client else 'unknown'}")
    
    # Process request
    response = await call_next(request)
    
    # Log response
    process_time = time.time() - start_time
    logger.info(f"📤 {request.method} {request.url.path} - Status: {response.status_code} - Time: {process_time:.3f}s")
    
    return response

# CORS middleware - Allow frontend URL from environment
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
logger.info(f"🌐 CORS: FRONTEND_URL = {FRONTEND_URL}")

allowed_origins = [
    "http://localhost:5173", 
    "http://localhost:3000",  # SvelteKit dev servers
    FRONTEND_URL  # Production frontend URL
]

logger.info(f"🌐 CORS: Allowed origins = {allowed_origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporary: Allow all origins for testing
    allow_credentials=False,  # Must be False when using allow_origins=["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize SEO generator
logger.info("🤖 Initializing SEO Content Generator...")
try:
    seo_generator = SEOContentGenerator()
    logger.info("✅ SEO Content Generator initialized successfully")
except Exception as e:
    logger.error(f"❌ Failed to initialize SEO Content Generator: {e}")
    raise

@app.get("/")
async def root():
    logger.info("🏠 Root endpoint accessed")
    return {"message": "SEO Page Generator API", "version": "1.0.0", "status": "healthy"}

@app.post("/generate", response_model=GenerateResponse)
async def generate_seo_page(product_input: ProductInput, db: Session = Depends(get_db)):
    """Generate SEO-optimized page content for a product"""
    logger.info(f"🚀 Starting SEO page generation for: {product_input.name}")
    
    try:
        # Convert to dict for processing
        product_data = product_input.model_dump()
        logger.debug(f"📝 Product data: {product_data}")
        
        # Generate SEO content using AI
        logger.info("🤖 Calling AI to generate SEO content...")
        seo_content = await seo_generator.generate_seo_content(product_data)
        logger.info(f"✅ AI content generated successfully for slug: {seo_content.get('slug', 'unknown')}")
        
        # Check if slug already exists
        slug = seo_content['slug']
        logger.info(f"🔍 Checking if slug '{slug}' already exists...")
        existing_product = db.query(Product).filter(Product.slug == slug).first()
        
        if existing_product:
            logger.info(f"📝 Updating existing product with slug: {slug}")
            # Update existing product
            for key, value in product_data.items():
                setattr(existing_product, key, value)
            
            existing_product.seo_title = seo_content['seo_title']
            existing_product.meta_description = seo_content['meta_description']
            existing_product.intro_content = seo_content['intro_content']
            existing_product.sections = seo_content['sections']
            existing_product.faqs = seo_content['faqs']
            existing_product.call_to_action = seo_content['call_to_action']
            existing_product.json_ld_schema = seo_content['json_ld_schema']
            
            db.commit()
            db.refresh(existing_product)
            logger.info(f"✅ Product updated successfully: {existing_product.name}")
            
            return GenerateResponse(
                success=True,
                message="Product updated successfully",
                product=ProductResponse.model_validate(existing_product)
            )
        else:
            logger.info(f"➕ Creating new product with slug: {slug}")
            # Create new product
            db_product = Product(
                slug=seo_content['slug'],
                name=product_data['name'],
                category=product_data['category'],
                features=product_data['features'],
                keywords=product_data['keywords'],
                location=product_data['location'],
                target_audience=product_data['target_audience'],
                seo_title=seo_content['seo_title'],
                meta_description=seo_content['meta_description'],
                intro_content=seo_content['intro_content'],
                sections=seo_content['sections'],
                faqs=seo_content['faqs'],
                call_to_action=seo_content['call_to_action'],
                json_ld_schema=seo_content['json_ld_schema']
            )
            
            db.add(db_product)
            db.commit()
            db.refresh(db_product)
            logger.info(f"✅ New product created successfully: {db_product.name} (ID: {db_product.id})")
            
            return GenerateResponse(
                success=True,
                message="SEO page generated successfully",
                product=ProductResponse.model_validate(db_product)
            )
            
    except Exception as e:
        logger.error(f"❌ Error generating SEO page for {product_input.name}: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to generate SEO page: {str(e)}")

@app.get("/product/{slug}", response_model=ProductResponse)
async def get_product(slug: str, db: Session = Depends(get_db)):
    """Get product data by slug"""
    logger.info(f"🔍 Fetching product with slug: {slug}")
    
    product = db.query(Product).filter(Product.slug == slug).first()
    if not product:
        logger.warning(f"❌ Product not found with slug: {slug}")
        raise HTTPException(status_code=404, detail="Product not found")
    
    logger.info(f"✅ Product found: {product.name} (ID: {product.id})")
    return ProductResponse.model_validate(product)

@app.get("/products", response_model=List[ProductResponse])
async def get_all_products(db: Session = Depends(get_db)):
    """Get all products"""
    logger.info("📋 Fetching all products")
    
    products = db.query(Product).all()
    logger.info(f"✅ Found {len(products)} products")
    
    return [ProductResponse.model_validate(product) for product in products]

@app.get("/sitemap.xml")
async def get_sitemap(db: Session = Depends(get_db)):
    """Generate dynamic sitemap.xml"""
    logger.info("🗺️ Generating sitemap.xml")
    
    products = db.query(Product).all()
    base_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
    logger.info(f"📄 Creating sitemap with {len(products)} products, base URL: {base_url}")
    
    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{base_url}</loc>
        <lastmod>2024-01-01T00:00:00+00:00</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>'''
    
    for product in products:
        sitemap_xml += f'''
    <url>
        <loc>{base_url}/products/{product.slug}</loc>
        <lastmod>{product.updated_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>'''
    
    sitemap_xml += '\n</urlset>'
    
    logger.info("✅ Sitemap generated successfully")
    return Response(content=sitemap_xml, media_type="application/xml")

@app.post("/ping-google")
async def ping_google_sitemap():
    """Notify Google about sitemap updates"""
    logger.info("📡 Pinging Google for sitemap update")
    
    try:
        base_url = os.getenv("BASE_URL", "http://localhost:8000")
        sitemap_url = f"{base_url}/sitemap.xml"
        google_ping_url = f"http://www.google.com/ping?sitemap={quote(sitemap_url)}"
        
        logger.info(f"🔗 Sitemap URL: {sitemap_url}")
        logger.info(f"📤 Pinging Google at: {google_ping_url}")
        
        response = requests.get(google_ping_url)
        
        if response.status_code == 200:
            logger.info("✅ Successfully pinged Google")
            return {"success": True, "message": "Successfully pinged Google about sitemap update"}
        else:
            logger.warning(f"⚠️ Google ping failed with status: {response.status_code}")
            return {"success": False, "message": f"Failed to ping Google: {response.status_code}"}
            
    except Exception as e:
        logger.error(f"❌ Error pinging Google: {str(e)}", exc_info=True)
        return {"success": False, "message": f"Error pinging Google: {str(e)}"}

@app.delete("/product/{slug}")
async def delete_product(slug: str, db: Session = Depends(get_db)):
    """Delete a product by slug"""
    logger.info(f"🗑️ Attempting to delete product with slug: {slug}")
    
    product = db.query(Product).filter(Product.slug == slug).first()
    if not product:
        logger.warning(f"❌ Product not found for deletion: {slug}")
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_name = product.name
    db.delete(product)
    db.commit()
    
    logger.info(f"✅ Product deleted successfully: {product_name}")
    return {"success": True, "message": "Product deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.getenv("PORT", 8000))
    logger.info(f"🌐 Starting FastAPI server on http://0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port) 