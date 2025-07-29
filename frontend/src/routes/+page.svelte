<script>
  import { onMount } from 'svelte';
  import { productAPI } from '$lib/api.js';

  let products = [];
  let loading = true;
  let error = null;

  onMount(async () => {
    try {
      products = await productAPI.getAllProducts();
    } catch (err) {
      error = 'Failed to load products';
      console.error('Error loading products:', err);
    } finally {
      loading = false;
    }
  });
</script>

<svelte:head>
  <title>SEO Page Generator - AI-Powered Product Pages</title>
  <meta name="description" content="Create SEO-optimized product pages automatically with AI. Generate landing pages that rank on Google." />
  <meta property="og:title" content="SEO Page Generator - AI-Powered Product Pages" />
  <meta property="og:description" content="Create SEO-optimized product pages automatically with AI. Generate landing pages that rank on Google." />
  <meta property="og:type" content="website" />
</svelte:head>

<div class="container">
  <section class="hero">
    <h1>AI-Powered SEO Page Generator</h1>
    <p class="hero-subtitle">
      Create SEO-optimized product pages that automatically appear in Google Search results.
      Our AI generates compelling content, proper metadata, and structured data for maximum visibility.
    </p>
    <div class="hero-actions">
      <a href="/admin" class="btn btn-primary">Create New Page</a>
      <a href="#products" class="btn btn-secondary">View Products</a>
    </div>
  </section>

  <section id="products" class="products-section">
    <h2>Generated Product Pages</h2>
    
    {#if loading}
      <div class="loading">
        <p>Loading products...</p>
      </div>
    {:else if error}
      <div class="error">
        <p>{error}</p>
      </div>
    {:else if products.length === 0}
      <div class="empty-state">
        <h3>No products yet</h3>
        <p>Get started by creating your first SEO-optimized product page.</p>
        <a href="/admin" class="btn btn-primary">Create First Product</a>
      </div>
    {:else}
      <div class="products-grid">
        {#each products as product}
          <div class="product-card">
            <h3>
              <a href="/products/{product.slug}" class="product-link">
                {product.name}
              </a>
            </h3>
            <p class="product-category">{product.category}</p>
            <p class="product-description">{product.meta_description}</p>
            <div class="product-features">
              {#each product.features.slice(0, 3) as feature}
                <span class="feature-tag">{feature}</span>
              {/each}
            </div>
            <div class="product-actions">
              <a href="/products/{product.slug}" class="btn btn-primary btn-sm">View Page</a>
              <span class="product-date">
                Created {new Date(product.created_at).toLocaleDateString()}
              </span>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </section>

  <section class="features-section">
    <h2>Platform Features</h2>
    <div class="features-grid">
      <div class="feature">
        <h3>🤖 AI-Generated Content</h3>
        <p>Advanced AI creates compelling, keyword-rich content optimized for search engines.</p>
      </div>
      <div class="feature">
        <h3>🎯 SEO Optimized</h3>
        <p>Automatic meta tags, JSON-LD structured data, and Open Graph tags for maximum visibility.</p>
      </div>
      <div class="feature">
        <h3>📊 Auto Indexing</h3>
        <p>Dynamic sitemaps and Google ping notifications ensure fast indexing of new pages.</p>
      </div>
      <div class="feature">
        <h3>📱 Responsive Design</h3>
        <p>Mobile-friendly pages that look great on all devices and screen sizes.</p>
      </div>
    </div>
  </section>
</div>

<style>
  .hero {
    text-align: center;
    padding: 4rem 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    margin: -2rem -2rem 3rem -2rem;
    border-radius: 0 0 20px 20px;
  }

  .hero h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    font-weight: 700;
  }

  .hero-subtitle {
    font-size: 1.25rem;
    margin-bottom: 2rem;
    opacity: 0.9;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
  }

  .hero-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  .products-section {
    margin-bottom: 4rem;
  }

  .products-section h2 {
    font-size: 2rem;
    margin-bottom: 2rem;
    text-align: center;
  }

  .products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
  }

  .product-card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: transform 0.3s, box-shadow 0.3s;
  }

  .product-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  }

  .product-link {
    text-decoration: none;
    color: #333;
    font-weight: 600;
  }

  .product-link:hover {
    color: #007bff;
  }

  .product-category {
    color: #007bff;
    font-weight: 500;
    margin: 0.5rem 0;
  }

  .product-description {
    color: #666;
    margin-bottom: 1rem;
    line-height: 1.5;
  }

  .product-features {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }

  .feature-tag {
    background: #e3f2fd;
    color: #1976d2;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.85rem;
  }

  .product-actions {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }

  .product-date {
    color: #999;
    font-size: 0.85rem;
  }

  .empty-state {
    text-align: center;
    padding: 3rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .empty-state h3 {
    margin-bottom: 1rem;
    color: #666;
  }

  .features-section {
    margin-top: 4rem;
  }

  .features-section h2 {
    font-size: 2rem;
    margin-bottom: 2rem;
    text-align: center;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
  }

  .feature {
    text-align: center;
    padding: 2rem;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .feature h3 {
    margin-bottom: 1rem;
    font-size: 1.25rem;
  }

  @media (max-width: 768px) {
    .hero {
      padding: 2rem 1rem;
      margin: -2rem -1rem 2rem -1rem;
    }

    .hero h1 {
      font-size: 2rem;
    }

    .hero-subtitle {
      font-size: 1rem;
    }

    .products-grid {
      grid-template-columns: 1fr;
    }

    .product-actions {
      flex-direction: column;
      gap: 0.5rem;
      align-items: stretch;
    }
  }
</style> 