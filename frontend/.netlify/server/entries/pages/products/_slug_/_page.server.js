import axios from "axios";
import "../../../../chunks/index.js";
const API_BASE_URL = {}.VITE_API_BASE_URL || "http://localhost:8000";
axios.create({
  baseURL: API_BASE_URL,
  timeout: 1e4,
  // 10 second timeout
  headers: {
    "Content-Type": "application/json"
  }
});
const ssr = false;
export {
  ssr
};
