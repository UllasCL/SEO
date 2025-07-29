#!/bin/bash

echo "🚀 SEO Page Generator - Quick Deploy Script"
echo "============================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
fi

# Add all files
echo "📝 Adding files to Git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Production deployment setup - $(date)"

echo ""
echo "✅ Code prepared for deployment!"
echo ""
echo "🔗 Next steps:"
echo "1. Create a GitHub repository at: https://github.com/new"
echo "2. Name it: seo-page-generator"
echo "3. Run these commands to push:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/seo-page-generator.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. Then deploy:"
echo "   • Backend: https://railway.app (connect GitHub repo, set root to 'backend')"
echo "   • Frontend: https://vercel.com (connect GitHub repo, set root to 'frontend')"
echo ""
echo "📖 Full guide: ./DEPLOYMENT_GUIDE.md" 