# 🚀 Production Deployment Guide

Deploy your SEO Page Generator to production in 15 minutes!

## 📋 Prerequisites

- GitHub account
- OpenAI API key
- 10 minutes of your time

## 🔄 Step 1: Prepare Git Repository

```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit - SEO Page Generator"

# Create GitHub repository
# Go to github.com → New Repository → "seo-page-generator"
# Then push your code:
git remote add origin https://github.com/yourusername/seo-page-generator.git
git branch -M main
git push -u origin main
```

## 🚂 Step 2: Deploy Backend to Railway

### 2.1 Create Railway Account
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Connect your GitHub account

### 2.2 Deploy Backend
1. Click "Deploy from GitHub repo"
2. Select your `seo-page-generator` repository
3. Railway will auto-detect it's a Python app
4. Set the root directory to `/backend`

### 2.3 Configure Environment Variables
In Railway dashboard → Variables, add:

```env
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./seo_generator.db
FRONTEND_URL=https://your-frontend-url.vercel.app
BASE_URL=https://your-backend-url.railway.app
PORT=8000
```

### 2.4 Get Your Backend URL
- After deployment, copy your Railway app URL
- Format: `https://your-app-name.railway.app`

## ⚡ Step 3: Deploy Frontend to Vercel

### 3.1 Create Vercel Account
1. Go to [Vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Connect your GitHub account

### 3.2 Deploy Frontend
1. Click "New Project"
2. Import your `seo-page-generator` repository
3. Set Framework Preset: "SvelteKit"
4. Set Root Directory: `frontend`
5. Click "Deploy"

### 3.3 Configure Environment Variables
In Vercel dashboard → Settings → Environment Variables:

```env
VITE_API_BASE_URL=https://your-backend-url.railway.app
```

### 3.4 Redeploy
- Go to Deployments tab
- Click "Redeploy" to apply environment variables

## 🔧 Step 4: Update Backend with Frontend URL

1. Go back to Railway dashboard
2. Update `FRONTEND_URL` environment variable with your Vercel URL
3. Redeploy the backend

## ✅ Step 5: Test Your Deployment

### 5.1 Test Backend
```bash
curl https://your-backend-url.railway.app/
# Should return: {"message":"SEO Page Generator API","version":"1.0.0","status":"healthy"}
```

### 5.2 Test Frontend
1. Visit your Vercel URL
2. Try creating a product in admin panel
3. Verify product pages load correctly

### 5.3 Test SEO Features
1. Check sitemap: `https://your-backend-url.railway.app/sitemap.xml`
2. Test Google ping: `POST https://your-backend-url.railway.app/ping-google`
3. Verify meta tags in page source

## 🌐 Step 6: Submit to Google

### 6.1 Google Search Console
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add your website property
3. Verify ownership (HTML file method)
4. Submit sitemap: `https://your-backend-url.railway.app/sitemap.xml`

### 6.2 Request Indexing
1. Go to URL Inspection tool
2. Enter your product page URLs
3. Click "Request Indexing"

## 📊 Expected Results

- **Backend**: API accessible at Railway URL
- **Frontend**: Website live at Vercel URL  
- **SEO**: All meta tags, schemas, sitemap working
- **Google**: Pages indexed within 1-2 weeks

## 🐛 Troubleshooting

### Backend Issues
- **500 Error**: Check Railway logs for Python errors
- **Environment Variables**: Ensure all vars are set correctly
- **Database**: SQLite should work automatically

### Frontend Issues  
- **API Errors**: Verify VITE_API_BASE_URL is correct
- **Build Failures**: Check Node.js version compatibility
- **CORS Errors**: Ensure backend allows frontend domain

### SEO Issues
- **No Meta Tags**: Check if product data is loading
- **Sitemap Empty**: Verify backend database has products
- **Schema Errors**: Test with Google Rich Results tool

## 🎯 Post-Deployment Checklist

- [ ] Backend API responding
- [ ] Frontend loading correctly
- [ ] Admin panel working
- [ ] Product pages generating
- [ ] Sitemap accessible
- [ ] Google Search Console setup
- [ ] First product pages created
- [ ] SEO meta tags verified

## 🚀 Optional Enhancements

### Custom Domain
- **Vercel**: Add custom domain in dashboard
- **Railway**: Available on paid plans

### Analytics
- Add Google Analytics to frontend
- Monitor traffic in Vercel analytics
- Track API usage in Railway metrics

### Database Upgrade
- **Production**: Consider PostgreSQL for Railway
- **Backup**: Set up automated backups

## 📞 Support

If you encounter issues:
1. Check Railway/Vercel logs
2. Verify environment variables
3. Test APIs manually with curl
4. Check GitHub repository settings

---

**Ready to go live? Let's start with Step 1! 🚀** 