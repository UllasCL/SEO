<script>
  import { onMount } from 'svelte';
  import { productAPI } from '$lib/api.js';
  
  export let data;
  
  console.log('🔍 Product page data:', data);
  
  let product = data?.product;
  let loading = !product;
  let error = null;
  
  // Add safety checks
  $: if (!product && !loading) {
    console.error('❌ Product data is missing!', data);
  } else if (product) {
    console.log('✅ Product loaded:', product.name);
  }
  
  // Fallback: if no product data, try loading on client side
  onMount(async () => {
    if (!product && !error) {
      loading = true;
      try {
        const urlParams = new URLSearchParams(window.location.search);
        const slug = window.location.pathname.split('/').pop();
        
        console.log(`🔄 Fallback loading for slug: ${slug}`);
        product = await productAPI.getProduct(slug);
        console.log('✅ Fallback loading successful:', product.name);
        loading = false;
      } catch (err) {
        console.error('❌ Fallback loading failed:', err);
        error = err.response?.status === 404 ? 'Product not found' : 'Failed to load product';
        loading = false;
      }
    }
  });
</script>

<svelte:head>
  {#if product}
    <title>{product.seo_title}</title>
    <meta name="description" content={product.meta_description} />
    <meta name="keywords" content={product.keywords.join(', ')} />
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="product" />
    <meta property="og:title" content={product.seo_title} />
    <meta property="og:description" content={product.meta_description} />
    <meta property="og:site_name" content="SEO Page Generator" />
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image" />
    <meta property="twitter:title" content={product.seo_title} />
    <meta property="twitter:description" content={product.meta_description} />
    
    <!-- Canonical URL -->
    <link rel="canonical" href={`http://localhost:5173/products/${product.slug}`} />
    
    <!-- JSON-LD Structured Data -->
    {@html `<script type="application/ld+json">${JSON.stringify(product.json_ld_schema)}</script>`}
  {:else}
    <title>Loading Product - SEO Page Generator</title>
    <meta name="description" content="Loading product information..." />
  {/if}
</svelte:head>

{#if loading}
  <div class="container">
    <div class="loading-container">
      <div class="loading-spinner"></div>
      <p>Loading product...</p>
    </div>
  </div>
{:else if error}
  <div class="container">
    <div class="error-container">
      <h1>Error</h1>
      <p>{error}</p>
      <a href="/" class="btn btn-primary">← Back to Home</a>
    </div>
  </div>
{:else if product}

  <article class="container">
    <!-- Breadcrumbs -->
    <nav class="breadcrumbs">
      <a href="/">Home</a>
      <span class="separator">›</span>
      <a href="/?category={encodeURIComponent(product.category)}">{product.category}</a>
      <span class="separator">›</span>
      <span class="current">{product.name}</span>
    </nav>

    <!-- Product Header -->
    <header class="product-header">
      <h1>{product.name}</h1>
      <p class="product-category">{product.category}</p>
      <div class="product-meta">
        <span class="location">📍 {product.location}</span>
        <span class="audience">👥 {product.target_audience}</span>
      </div>
    </header>

    <!-- Introduction -->
    <section class="intro-section card">
      <p class="intro-text">{product.intro_content}</p>
    </section>

    <!-- Features -->
    <section class="features-section card">
      <h2>Key Features</h2>
      <div class="features-grid">
        {#each product.features as feature}
          <div class="feature-item">
            <span class="feature-icon">✓</span>
            <span class="feature-text">{feature}</span>
          </div>
        {/each}
      </div>
    </section>

    <!-- Content Sections -->
    {#each product.sections as section}
      <section class="content-section card">
        <h2>{section.heading}</h2>
        <p class="section-content">{section.content}</p>
      </section>
    {/each}

    <!-- Call to Action -->
    <section class="cta-section card">
      <div class="cta-content">
        <h2>Ready to Get Started?</h2>
        <p>Don't miss out on this amazing opportunity!</p>
        <button class="btn btn-primary btn-large">{product.call_to_action}</button>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section card">
      <h2>Frequently Asked Questions</h2>
      <div class="faq-list">
        {#each product.faqs as faq, index}
          <details class="faq-item">
            <summary class="faq-question">{faq.question}</summary>
            <div class="faq-answer">
              <p>{faq.answer}</p>
            </div>
          </details>
        {/each}
      </div>
    </section>

    <!-- Keywords Section (for SEO) -->
    <section class="keywords-section">
      <div class="keywords-content">
        <h3>Related Topics</h3>
        <div class="keywords-list">
          {#each product.keywords as keyword}
            <span class="keyword-tag">{keyword}</span>
          {/each}
        </div>
      </div>
    </section>

    <!-- Back to Products -->
    <nav class="navigation-footer">
      <a href="/" class="btn btn-secondary">← Back to All Products</a>
      <div class="share-buttons">
        <span>Share:</span>
        <a href="https://twitter.com/intent/tweet?text={encodeURIComponent(product.seo_title)}&url={encodeURIComponent(`http://localhost:5173/products/${product.slug}`)}" 
           target="_blank" 
           rel="noopener"
           class="share-btn twitter">Twitter</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={encodeURIComponent(`http://localhost:5173/products/${product.slug}`)}" 
           target="_blank" 
           rel="noopener"
           class="share-btn facebook">Facebook</a>
      </div>
    </nav>
  </article>
{/if}

<style>
  .loading-container {
    text-align: center;
    padding: 4rem 2rem;
  }

  .loading-spinner {
    width: 40px;
    height: 40px;
    border: 3px solid #f3f3f3;
    border-top: 3px solid #007bff;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: 0 auto 1rem;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .error-container {
    text-align: center;
    padding: 4rem 2rem;
  }

  .breadcrumbs {
    margin-bottom: 2rem;
    font-size: 0.9rem;
    color: #666;
  }

  .breadcrumbs a {
    color: #007bff;
    text-decoration: none;
  }

  .breadcrumbs a:hover {
    text-decoration: underline;
  }

  .separator {
    margin: 0 0.5rem;
  }

  .current {
    color: #333;
    font-weight: 500;
  }

  .product-header {
    text-align: center;
    margin-bottom: 3rem;
    padding: 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 16px;
  }

  .product-header h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    font-weight: 700;
  }

  .product-category {
    font-size: 1.25rem;
    opacity: 0.9;
    margin-bottom: 1rem;
  }

  .product-meta {
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
    opacity: 0.9;
  }

  .intro-section {
    margin-bottom: 2rem;
  }

  .intro-text {
    font-size: 1.2rem;
    line-height: 1.7;
    color: #444;
    text-align: center;
    margin: 0;
  }

  .features-section h2 {
    margin-bottom: 1.5rem;
    color: #333;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
  }

  .feature-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
    transition: transform 0.2s;
  }

  .feature-item:hover {
    transform: translateY(-2px);
  }

  .feature-icon {
    color: #28a745;
    font-weight: bold;
    font-size: 1.2rem;
  }

  .feature-text {
    font-weight: 500;
  }

  .content-section {
    margin-bottom: 2rem;
  }

  .content-section h2 {
    color: #333;
    margin-bottom: 1rem;
  }

  .section-content {
    line-height: 1.7;
    color: #555;
    margin: 0;
  }

  .cta-section {
    background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
    color: white;
    text-align: center;
    margin: 3rem 0;
  }

  .cta-content h2 {
    margin-bottom: 1rem;
  }

  .cta-content p {
    margin-bottom: 2rem;
    opacity: 0.9;
  }

  .btn-large {
    padding: 1rem 2rem;
    font-size: 1.2rem;
    background: white;
    color: #28a745;
    border: none;
    font-weight: 600;
  }

  .btn-large:hover {
    background: #f8f9fa;
    transform: translateY(-2px);
  }

  .faq-section h2 {
    margin-bottom: 2rem;
    color: #333;
  }

  .faq-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .faq-item {
    border: 1px solid #e9ecef;
    border-radius: 8px;
    overflow: hidden;
  }

  .faq-question {
    padding: 1.25rem;
    background: #f8f9fa;
    cursor: pointer;
    font-weight: 600;
    list-style: none;
    user-select: none;
    transition: background-color 0.2s;
  }

  .faq-question:hover {
    background: #e9ecef;
  }

  .faq-question::-webkit-details-marker {
    display: none;
  }

  .faq-answer {
    padding: 1.25rem;
    border-top: 1px solid #e9ecef;
  }

  .faq-answer p {
    margin: 0;
    line-height: 1.6;
    color: #555;
  }

  .keywords-section {
    margin: 3rem 0;
    padding: 2rem;
    background: #f8f9fa;
    border-radius: 12px;
  }

  .keywords-content h3 {
    margin-bottom: 1rem;
    color: #333;
  }

  .keywords-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .keyword-tag {
    background: #007bff;
    color: white;
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 500;
  }

  .navigation-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid #e9ecef;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .share-buttons {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .share-btn {
    padding: 0.5rem 1rem;
    border-radius: 6px;
    text-decoration: none;
    color: white;
    font-size: 0.9rem;
    font-weight: 500;
  }

  .share-btn.twitter {
    background: #1da1f2;
  }

  .share-btn.facebook {
    background: #4267b2;
  }

  .share-btn:hover {
    opacity: 0.9;
    transform: translateY(-1px);
  }

  @media (max-width: 768px) {
    .product-header {
      padding: 1.5rem;
    }

    .product-header h1 {
      font-size: 2rem;
    }

    .product-meta {
      flex-direction: column;
      gap: 0.5rem;
    }

    .features-grid {
      grid-template-columns: 1fr;
    }

    .navigation-footer {
      flex-direction: column;
      text-align: center;
    }

    .keywords-list {
      justify-content: center;
    }
  }
</style> 