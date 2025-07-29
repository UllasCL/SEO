#!/usr/bin/env python3
"""
Startup script for the SEO Page Generator backend.
This script sets up the environment and starts the FastAPI server.
"""

import os
import sys
from pathlib import Path

def check_requirements():
    """Check if all required packages are installed"""
    try:
        import fastapi
        import uvicorn
        import sqlalchemy
        import openai
        import requests
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e.name}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and has required variables"""
    env_file = Path(".env")
    
    if not env_file.exists():
        print("❌ .env file not found")
        print("Please copy .env.example to .env and add your OpenAI API key")
        return False
    
    # Read .env file
    with open(env_file) as f:
        env_content = f.read()
    
    if "OPENAI_API_KEY=your_openai_api_key_here" in env_content:
        print("❌ Please set your OpenAI API key in .env file")
        return False
    
    if "OPENAI_API_KEY=" not in env_content:
        print("❌ OPENAI_API_KEY not found in .env file")
        return False
    
    print("✅ Environment file configured")
    return True

def main():
    """Main startup function"""
    print("🚀 Starting SEO Page Generator Backend...")
    print("-" * 50)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check environment
    if not check_env_file():
        sys.exit(1)
    
    print("✅ All checks passed!")
    print("🌐 Starting FastAPI server...")
    print("📍 Backend will be available at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("-" * 50)
    
    # Start the server
    os.system("python main.py")

if __name__ == "__main__":
    main() 