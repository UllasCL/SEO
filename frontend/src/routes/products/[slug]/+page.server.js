import axios from 'axios';
import { error } from '@sveltejs/kit';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

// Configure axios with timeout and better error handling
const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000, // 10 second timeout
  headers: {
    'Content-Type': 'application/json',
  }
});

// Disable server-side rendering for this route to avoid SSR fetch issues
export const ssr = false; 