import os
import json
import re
import logging
from typing import Dict, Any, List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger("seo_generator")

class SEOContentGenerator:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error("❌ OPENAI_API_KEY not found in environment variables")
            raise ValueError("OPENAI_API_KEY is required")
        
        logger.info("🔑 Initializing OpenAI client...")
        self.client = OpenAI(api_key=api_key)
        logger.info("✅ OpenAI client initialized successfully")
        
    def generate_slug(self, name: str) -> str:
        """Generate URL-friendly slug from product name"""
        original_name = name
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', name.lower())
        slug = re.sub(r'\s+', '-', slug)
        slug = re.sub(r'-+', '-', slug)
        final_slug = slug.strip('-')
        
        logger.debug(f"🔗 Generated slug: '{original_name}' -> '{final_slug}'")
        return final_slug
    
    async def generate_seo_content(self, product_input: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive SEO content using OpenAI"""
        
        logger.info(f"🎯 Generating SEO content for: {product_input.get('name', 'Unknown')}")
        logger.debug(f"📋 Input data: {product_input}")
        
        prompt = f"""You're an SEO content strategist creating a public-facing page for a product. Generate SEO-optimized content using this input:

- Product Name: {product_input['name']}
- Category: {product_input['category']}
- Keywords: {', '.join(product_input['keywords'])}
- Features: {', '.join(product_input['features'])}
- Location: {product_input['location']}
- Target Audience: {product_input['target_audience']}

Generate a JSON response with the following structure:

{{
  "seo_title": "SEO-optimized title under 60 characters",
  "meta_description": "Compelling meta description under 160 characters",
  "intro_content": "Engaging 150-200 word introduction paragraph that's keyword-rich and compelling",
  "sections": [
    {{
      "heading": "Benefits & Features",
      "content": "Detailed content about benefits and features"
    }},
    {{
      "heading": "Why Choose Us",
      "content": "Compelling reasons and use cases"
    }}
  ],
  "faqs": [
    {{
      "question": "Relevant FAQ question",
      "answer": "Comprehensive answer"
    }},
    {{
      "question": "Another important question",
      "answer": "Detailed answer"
    }},
    {{
      "question": "Third FAQ question",
      "answer": "Helpful answer"
    }}
  ],
  "call_to_action": "Compelling CTA text like 'Order Premium Colombian Coffee Today' or 'Get Your Coffee Fix Now'",
  "json_ld_schema": {{
    "@context": "https://schema.org/",
    "@type": "Product",
    "name": "{product_input['name']}",
    "description": "Product description",
    "category": "{product_input['category']}",
    "brand": {{
      "@type": "Brand",
      "name": "Your Brand Name"
    }},
    "offers": {{
      "@type": "Offer",
      "availability": "https://schema.org/InStock",
      "priceCurrency": "USD"
    }}
  }}
}}

Make sure the content is engaging, keyword-optimized, and designed to rank well in search engines. Focus on the target audience and include the provided keywords naturally throughout the content."""

        logger.info("🤖 Sending request to OpenAI...")
        
        try:
            response = await self._call_openai(prompt)
            logger.info("✅ Received response from OpenAI")
            logger.debug(f"📝 Raw OpenAI response length: {len(response)} characters")
            
            content = json.loads(response)
            logger.info("✅ Successfully parsed JSON response")
            
            # Generate slug
            slug = self.generate_slug(product_input['name'])
            content['slug'] = slug
            
            logger.info(f"🎉 SEO content generation completed for slug: {slug}")
            return content
            
        except json.JSONDecodeError as e:
            logger.error(f"❌ Failed to parse OpenAI JSON response: {e}")
            logger.error(f"📄 Raw response: {response[:500]}...")
            logger.info("🔄 Using fallback content generation")
            return self._generate_fallback_content(product_input)
        except Exception as e:
            logger.error(f"❌ Error generating SEO content: {e}", exc_info=True)
            logger.info("🔄 Using fallback content generation")
            return self._generate_fallback_content(product_input)
    
    async def _call_openai(self, prompt: str) -> str:
        """Make API call to OpenAI"""
        logger.debug(f"📤 Calling OpenAI API with model: gpt-4")
        logger.debug(f"📝 Prompt length: {len(prompt)} characters")
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert SEO content strategist. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            content = response.choices[0].message.content
            logger.info(f"📥 OpenAI API call successful - Response length: {len(content)} characters")
            return content
            
        except Exception as e:
            logger.error(f"❌ OpenAI API call failed: {e}", exc_info=True)
            raise
    
    def _generate_fallback_content(self, product_input: Dict[str, Any]) -> Dict[str, Any]:
        """Generate fallback content if OpenAI fails"""
        logger.warning("⚠️ Generating fallback content (OpenAI unavailable)")
        
        slug = self.generate_slug(product_input['name'])
        logger.info(f"🔧 Creating fallback content for slug: {slug}")
        
        return {
            "slug": slug,
            "seo_title": f"{product_input['name']} - Premium {product_input['category']}",
            "meta_description": f"Discover {product_input['name']} - {', '.join(product_input['features'][:2])}. Perfect for {product_input['target_audience']}.",
            "intro_content": f"Welcome to {product_input['name']}, your premier choice for {product_input['category'].lower()}. Our product offers {', '.join(product_input['features'])} and is specially designed for {product_input['target_audience']}.",
            "sections": [
                {
                    "heading": "Key Features",
                    "content": f"Our {product_input['name']} stands out with these exceptional features: {', '.join(product_input['features'])}. Each feature is carefully crafted to meet the needs of {product_input['target_audience']}."
                },
                {
                    "heading": "Why Choose Us",
                    "content": f"Located in {product_input['location']}, we specialize in {product_input['category']} that exceeds expectations. Our commitment to quality and customer satisfaction makes us the preferred choice."
                }
            ],
            "faqs": [
                {
                    "question": f"What makes {product_input['name']} special?",
                    "answer": f"Our {product_input['name']} features {', '.join(product_input['features'][:2])}, making it perfect for {product_input['target_audience']}."
                },
                {
                    "question": "How do I place an order?",
                    "answer": "You can contact us directly through our website or call our customer service team for immediate assistance."
                },
                {
                    "question": "Do you ship nationwide?",
                    "answer": f"Yes, we ship from our {product_input['location']} location to customers nationwide with fast and reliable delivery."
                }
            ],
            "call_to_action": f"Get Your {product_input['name']} Today",
            "json_ld_schema": {
                "@context": "https://schema.org/",
                "@type": "Product",
                "name": product_input['name'],
                "description": f"Premium {product_input['category']} with {', '.join(product_input['features'])}",
                "category": product_input['category'],
                "brand": {
                    "@type": "Brand",
                    "name": "Premium Products"
                },
                "offers": {
                    "@type": "Offer",
                    "availability": "https://schema.org/InStock",
                    "priceCurrency": "USD"
                }
            }
        }
        
        logger.info(f"✅ Fallback content generated successfully for: {product_input['name']}")
        return fallback_content 