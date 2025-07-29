# 🚀 SEO-Optimized Page Generator Platform

A full-stack web platform that automatically generates SEO-optimized product pages using AI. Built with **FastAPI** (Python) backend and **SvelteKit** frontend, this platform creates public-facing landing pages designed to rank on Google Search.

## 🎯 Features

- **🤖 AI-Powered Content Generation**: Uses OpenAI GPT-4 to create compelling, keyword-rich content
- **🎯 SEO Optimized**: Automatic meta tags, JSON-LD structured data, and Open Graph tags
- **📊 Auto Google Indexing**: Dynamic sitemaps with Google ping notifications
- **📱 Responsive Design**: Mobile-friendly pages that look great on all devices
- **⚡ Fast & Modern**: Built with SvelteKit for lightning-fast performance
- **🔧 Easy Management**: Admin interface for creating and managing pages

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   SvelteKit     │    │    FastAPI      │    │    OpenAI       │
│   Frontend      │◄──►│    Backend      │◄──►│   GPT-4 API     │
│                 │    │                 │    │                 │
│ • Dynamic Routes│    │ • AI Integration│    │ • Content Gen   │
│ • SEO Meta Tags │    │ • Database      │    │ • SEO Strategy  │
│ • Admin Panel   │    │ • API Endpoints │    │ • Structured    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 18+
- OpenAI API Key

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Add your OpenAI API key to .env
echo "OPENAI_API_KEY=your_openai_api_key_here" >> .env

# Start the FastAPI server
python main.py
```

The backend will be available at `http://localhost:8000`

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 📁 Project Structure

```
seo-page-generator/
├── backend/                 # FastAPI Backend
│   ├── main.py             # Main application file
│   ├── database.py         # Database models and config
│   ├── models.py           # Pydantic models
│   ├── seo_generator.py    # OpenAI integration
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment variables template
└── frontend/               # SvelteKit Frontend
    ├── src/
    │   ├── routes/
    │   │   ├── +layout.svelte         # Main layout
    │   │   ├── +page.svelte           # Home page
    │   │   ├── admin/
    │   │   │   └── +page.svelte       # Admin panel
    │   │   └── products/
    │   │       └── [slug]/
    │   │           ├── +page.server.js # Server-side data loading
    │   │           └── +page.svelte    # Dynamic product page
    │   ├── lib/
    │   │   └── api.js                 # API client
    │   └── app.html                   # HTML template
    ├── package.json
    ├── svelte.config.js
    └── vite.config.js
```

## 🔧 API Endpoints

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/generate` | Generate SEO page from product data |
| `GET` | `/product/{slug}` | Get product data by slug |
| `GET` | `/products` | Get all products |
| `GET` | `/sitemap.xml` | Dynamic sitemap for SEO |
| `POST` | `/ping-google` | Notify Google of sitemap updates |
| `DELETE` | `/product/{slug}` | Delete a product |

### Example API Usage

```python
# Generate a new SEO page
import requests

product_data = {
    "name": "Colombian Dark Roast Coffee",
    "category": "Gourmet Coffee",
    "features": [
        "Single-Origin Excellence",
        "Bold Flavor Profile",
        "Ethical Sourcing"
    ],
    "keywords": ["dark roast coffee", "Colombian coffee"],
    "location": "USA",
    "target_audience": "Coffee lovers who enjoy bold, premium flavors"
}

response = requests.post("http://localhost:8000/generate", json=product_data)
print(response.json())
```

## 📝 Example Product Input

```json
{
  "name": "Colombian Dark Roast Coffee",
  "category": "Gourmet Coffee",
  "features": [
    "Single-Origin Excellence",
    "Bold Flavor Profile",
    "Ethical Sourcing",
    "Small-Batch Fresh Roasting"
  ],
  "keywords": ["dark roast coffee", "Colombian coffee beans", "best gourmet coffee"],
  "location": "USA",
  "target_audience": "Coffee lovers who enjoy bold, premium flavors"
}
```

## 🎨 Generated Page Features

Each generated page includes:

- **SEO-Optimized Title & Meta Description**
- **Structured JSON-LD Schema Markup**
- **Open Graph & Twitter Cards**
- **Responsive Design with Modern UI**
- **Feature Highlights & Benefits**
- **FAQ Section for Long-tail Keywords**
- **Call-to-Action Buttons**
- **Social Sharing Integration**
- **Breadcrumb Navigation**

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./seo_generator.db
FRONTEND_URL=http://localhost:5173
BASE_URL=http://localhost:8000
```

### Database

The platform uses SQLite by default, but can be configured for PostgreSQL:

```python
# For PostgreSQL
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## 🚀 Deployment

### Backend Deployment (Railway/Render)

```bash
# Add production dependencies
pip freeze > requirements.txt

# Deploy to your preferred platform
# Make sure to set environment variables
```

### Frontend Deployment (Vercel/Netlify)

```bash
# Build for production
npm run build

# Deploy the built files
```

## 📊 SEO Features

### Automatic SEO Optimization

- **Meta Tags**: Title, description, keywords
- **Open Graph**: Facebook/LinkedIn sharing
- **Twitter Cards**: Twitter sharing optimization
- **JSON-LD**: Structured data for rich snippets
- **Canonical URLs**: Prevent duplicate content
- **Sitemap**: Automatic generation and Google ping

### Content Strategy

The AI generates:
- **Keyword-rich titles** (under 60 characters)
- **Compelling meta descriptions** (under 160 characters)
- **Feature-focused content** with benefits
- **FAQ sections** for long-tail keywords
- **Schema markup** for search engines

## 🛠️ Customization

### Adding Custom Fields

1. Update the database model in `backend/database.py`
2. Update Pydantic models in `backend/models.py`
3. Modify the AI prompt in `backend/seo_generator.py`
4. Update the frontend form in `frontend/src/routes/admin/+page.svelte`

### Styling Customization

The frontend uses CSS custom properties for easy theming. Modify the global styles in `frontend/src/routes/+layout.svelte`.

## 🔍 Monitoring & Analytics

### Built-in Features

- Product creation timestamps
- Automatic sitemap updates
- Google ping notifications

### Optional Integrations

- Google Analytics 4
- Google Search Console API
- SEO monitoring tools

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🆘 Support

For issues and questions:

1. Check the [Issues](../../issues) page
2. Review the documentation
3. Create a new issue with detailed information

## 🔮 Roadmap

- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Bulk import/export functionality
- [ ] Custom templates
- [ ] A/B testing for content
- [ ] Integration with more AI models

---

**Built with ❤️ using SvelteKit, FastAPI, and OpenAI** 