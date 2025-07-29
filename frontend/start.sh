#!/bin/bash

echo "🚀 Starting SEO Page Generator Frontend..."
echo "================================================"

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed"
    echo "Please install Node.js 18+ from https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed"
    echo "Please install npm (usually comes with Node.js)"
    exit 1
fi

echo "✅ Node.js and npm are installed"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
    
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        exit 1
    fi
else
    echo "✅ Dependencies already installed"
fi

echo "✅ All checks passed!"
echo "🌐 Starting SvelteKit development server..."
echo "📍 Frontend will be available at: http://localhost:5173"
echo "🔄 Hot reload enabled - changes will be reflected automatically"
echo "================================================"

# Start the development server
npm run dev 