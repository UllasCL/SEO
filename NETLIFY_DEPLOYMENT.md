# 🌐 Deploy Frontend to Netlify

Deploy your SvelteKit frontend to Netlify in 5 minutes!

## 🚀 Quick Deployment Steps

### Step 1: Optimize for Netlify
First, let's update your SvelteKit adapter for better Netlify support:

```bash
cd frontend
npm install @sveltejs/adapter-netlify --save-dev
```

### Step 2: Create Netlify Configuration
Create `frontend/netlify.toml`:

```toml
[build]
  command = "npm run build"
  functions = "netlify/functions"
  publish = "build"

[build.environment]
  NODE_VERSION = "18"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[dev]
  command = "npm run dev"
  port = 5173
  publish = "build"
```

### Step 3: Deploy to Netlify

#### Option A: Drag & Drop (Fastest)
1. **Build locally:**
   ```bash
   cd frontend
   npm install
   npm run build
   ```

2. **Deploy:**
   - Go to [netlify.com](https://netlify.com)
   - Drag the `build` folder to Netlify
   - Get your URL instantly!

#### Option B: GitHub Integration (Recommended)
1. **Go to Netlify:**
   - Sign up at [netlify.com](https://netlify.com) with GitHub
   - Click "New site from Git"
   - Choose your repository

2. **Configure Build:**
   - **Branch:** `main` (or your deployment branch)
   - **Build command:** `npm run build`
   - **Publish directory:** `build`
   - **Root directory:** `frontend`

3. **Deploy:**
   - Click "Deploy site"
   - Get your URL: `https://amazing-name-123.netlify.app`

### Step 4: Environment Variables

In Netlify dashboard → Site settings → Environment variables:

```env
VITE_API_BASE_URL=https://your-render-backend.onrender.com
```

**Replace with your actual Render URL!**

### Step 5: Update Backend CORS

Update your Render backend environment variables:

```env
FRONTEND_URL=https://your-netlify-site.netlify.app
```

## 🎯 Custom Domain (Optional)

### Free Netlify Subdomain
- Netlify gives you: `https://yoursite.netlify.app`
- Can customize: Site settings → Domain management → Options → Edit site name

### Custom Domain
- Add your domain: Site settings → Domain management → Add custom domain
- Follow DNS instructions
- Free SSL included!

## ⚡ Performance Optimizations

### 1. Enable Form Handling
Add to `netlify.toml`:
```toml
[build.processing]
  skip_processing = false

[build.processing.css]
  bundle = true
  minify = true

[build.processing.js]
  bundle = true
  minify = true

[build.processing.html]
  pretty_urls = true
```

### 2. Cache Headers
```toml
[[headers]]
  for = "/build/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

## 🔧 Troubleshooting

### Build Fails
```bash
# Check locally first
cd frontend
npm install
npm run build
# If this works, the issue is with Netlify config
```

### 404 Errors
- Make sure you have the redirect rule in `netlify.toml`
- SPA routes need `/*` → `/index.html` redirect

### API Not Working
- Check `VITE_API_BASE_URL` environment variable
- Verify your Render backend is live
- Check browser console for CORS errors

## 📊 Expected Results

✅ **Frontend:** Live at `https://yoursite.netlify.app`  
✅ **Auto-deploy:** Updates on every git push  
✅ **SSL:** Automatic HTTPS  
✅ **CDN:** Global fast loading  
✅ **Forms:** Contact forms work out of the box  

## 🚀 Quick Deploy Script

Want to deploy right now? Run this:

```bash
# Go to frontend directory
cd frontend

# Install dependencies
npm install

# Add Netlify adapter (if not already done)
npm install @sveltejs/adapter-netlify --save-dev

# Build for production
npm run build

# Now drag the 'build' folder to netlify.com!
echo "✅ Build complete! Drag the 'build' folder to netlify.com"
```

## 🎯 Next Steps After Deployment

1. **Get your Netlify URL**
2. **Update backend FRONTEND_URL** on Render
3. **Test your site** - create products, view pages
4. **Custom domain** (optional)
5. **Analytics** - Netlify Analytics available

**Ready to deploy?** Choose Option A for instant deployment or Option B for continuous deployment! 🚀 

## 🎯 The Issue is Clear

Netlify is running the build from the **repository root** instead of the **`frontend` directory**.

## 🔧 Exact Steps to Fix

### In your Netlify dashboard:

1. **Go to your site** → **Site settings**
2. **Click "Build & deploy"** (left sidebar) 
3. **Find "Build settings"** section
4. **Click "Edit settings"**

5. **Set these EXACT values:**
   ```
   Base directory: frontend
   Build command: npm run build  
   Publish directory: build
   ```

6. **Click "Save"**

### Important Notes:
- **Base directory** is the most critical setting
- Without `frontend` as base directory, npm can't find `package.json`
- Publish directory should be `build` (relative to the base)

## 🔄 After Saving Settings

1. **Go to "Deploys" tab**
2. **Click "Trigger deploy"** → **"Deploy site"**

## 📊 Expected Result

With correct settings:
- ✅ Netlify runs `npm run build` **inside** `frontend/` directory
- ✅ Finds `frontend/package.json` ✅
- ✅ Build succeeds ✅
- ✅ Publishes from `frontend/build/` ✅

**The key is setting Base directory to `frontend` - double-check this setting!** 🎯 

## ✅ Your Configuration is Correct

**What you have:**
- Base directory: `frontend` 
- Publish directory: `frontend/build`

**This means Netlify will:**
- Run build commands in: `/opt/build/repo/frontend/` ✅
- Look for built files in: `/opt/build/repo/frontend/build/` ✅

## 📊 Two Valid Approaches

### Approach 1 (Your current setup):
```
<code_block_to_apply_changes_from>
```

### Approach 2 (Alternative):
```
Base directory: frontend  
Publish directory: build
```

**Both work!** Your setup is actually more explicit and clear.

## 🚀 Current Status

With your settings:
- ✅ **Base directory: `frontend`** (finds package.json)
- ✅ **Publish directory: `frontend/build`** (finds built files)
- ✅ **Build command: `npm run build`** (runs in frontend directory)

## 🔄 Next Steps

Your configuration looks perfect! Try deploying now:

1. **Save your current settings** (if not already saved)
2. **Go to "Deploys" tab**
3. **Click "Trigger deploy"** → **"Deploy site"**

## 📱 What Should Happen

- ✅ Finds `frontend/package.json` ✅
- ✅ Runs `npm install` and `npm run build` ✅
- ✅ Publishes files from `frontend/build/` ✅
- ✅ Site loads without 404 ✅

**Your configuration is correct - try the deploy now!** 🎯 