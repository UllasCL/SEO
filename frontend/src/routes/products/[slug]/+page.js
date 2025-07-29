import { productAPI } from '$lib/api.js';
import { error } from '@sveltejs/kit';

export async function load({ params }) {
  const { slug } = params;
  
  console.log(`🔍 Client-side loading product: ${slug}`);
  
  try {
    const product = await productAPI.getProduct(slug);
    console.log(`✅ Client-side product loaded: ${product.name}`);
    
    return {
      product
    };
  } catch (err) {
    console.error(`❌ Client-side error loading product:`, err);
    
    if (err.response?.status === 404) {
      throw error(404, `Product '${slug}' not found`);
    }
    
    throw error(500, `Failed to load product: ${err.message}`);
  }
}

// Ensure this runs only on the client side
export const ssr = false; 