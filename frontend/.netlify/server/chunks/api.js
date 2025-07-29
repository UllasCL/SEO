import axios from "axios";
const API_BASE_URL = {}.VITE_API_BASE_URL || "http://localhost:8000";
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json"
  }
});
const productAPI = {
  // Generate SEO page
  async generate(productData) {
    const response = await api.post("/generate", productData);
    return response.data;
  },
  // Get product by slug
  async getProduct(slug) {
    const response = await api.get(`/product/${slug}`);
    return response.data;
  },
  // Get all products
  async getAllProducts() {
    const response = await api.get("/products");
    return response.data;
  },
  // Delete product
  async deleteProduct(slug) {
    const response = await api.delete(`/product/${slug}`);
    return response.data;
  },
  // Ping Google for sitemap
  async pingGoogle() {
    const response = await api.post("/ping-google");
    return response.data;
  }
};
export {
  productAPI as p
};
