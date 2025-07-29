<script>
  import { onMount } from 'svelte';
  import { productAPI } from '$lib/api.js';

  let formData = {
    name: '',
    category: '',
    features: [''],
    keywords: [''],
    location: '',
    target_audience: ''
  };

  let products = [];
  let loading = false;
  let message = '';
  let messageType = '';

  onMount(async () => {
    await loadProducts();
  });

  async function loadProducts() {
    try {
      products = await productAPI.getAllProducts();
    } catch (error) {
      console.error('Error loading products:', error);
    }
  }

  function addFeature() {
    formData.features = [...formData.features, ''];
  }

  function removeFeature(index) {
    formData.features = formData.features.filter((_, i) => i !== index);
  }

  function addKeyword() {
    formData.keywords = [...formData.keywords, ''];
  }

  function removeKeyword(index) {
    formData.keywords = formData.keywords.filter((_, i) => i !== index);
  }

  async function generateProduct() {
    if (!formData.name || !formData.category || !formData.location || !formData.target_audience) {
      showMessage('Please fill in all required fields', 'error');
      return;
    }

    // Filter out empty features and keywords
    const cleanedData = {
      ...formData,
      features: formData.features.filter(f => f.trim()),
      keywords: formData.keywords.filter(k => k.trim())
    };

    if (cleanedData.features.length === 0) {
      showMessage('Please add at least one feature', 'error');
      return;
    }

    if (cleanedData.keywords.length === 0) {
      showMessage('Please add at least one keyword', 'error');
      return;
    }

    loading = true;
    try {
      const response = await productAPI.generate(cleanedData);
      
      if (response.success) {
        showMessage(`Successfully generated SEO page: ${response.product.name}`, 'success');
        resetForm();
        await loadProducts();
        
        // Ping Google for sitemap update
        try {
          await productAPI.pingGoogle();
          showMessage('Successfully notified Google about the new page', 'success');
        } catch (error) {
          console.warn('Failed to ping Google:', error);
        }
      } else {
        showMessage(response.message || 'Failed to generate product', 'error');
      }
    } catch (error) {
      showMessage('Error generating product: ' + (error.response?.data?.detail || error.message), 'error');
    } finally {
      loading = false;
    }
  }

  async function deleteProduct(slug, name) {
    if (!confirm(`Are you sure you want to delete "${name}"? This action cannot be undone.`)) {
      return;
    }

    try {
      await productAPI.deleteProduct(slug);
      showMessage(`Successfully deleted ${name}`, 'success');
      await loadProducts();
    } catch (error) {
      showMessage('Error deleting product: ' + (error.response?.data?.detail || error.message), 'error');
    }
  }

  function resetForm() {
    formData = {
      name: '',
      category: '',
      features: [''],
      keywords: [''],
      location: '',
      target_audience: ''
    };
  }

  function showMessage(text, type) {
    message = text;
    messageType = type;
    setTimeout(() => {
      message = '';
      messageType = '';
    }, 5000);
  }

  function loadExampleData() {
    formData = {
      name: 'Colombian Dark Roast Coffee',
      category: 'Gourmet Coffee',
      features: [
        'Single-Origin Excellence',
        'Bold Flavor Profile',
        'Ethical Sourcing',
        'Small-Batch Fresh Roasting'
      ],
      keywords: ['dark roast coffee', 'Colombian coffee beans', 'best gourmet coffee'],
      location: 'USA',
      target_audience: 'Coffee lovers who enjoy bold, premium flavors'
    };
  }
</script>

<svelte:head>
  <title>Admin - SEO Page Generator</title>
  <meta name="description" content="Admin panel for creating and managing SEO-optimized product pages" />
  <meta name="robots" content="noindex, nofollow" />
</svelte:head>

<div class="container">
  <div class="admin-header">
    <h1>SEO Page Generator Admin</h1>
    <p>Create AI-powered, SEO-optimized product pages that automatically appear in Google Search.</p>
  </div>

  {#if message}
    <div class="message {messageType}">
      {message}
    </div>
  {/if}

  <div class="admin-layout">
    <!-- Form Section -->
    <section class="form-section card">
      <div class="section-header">
        <h2>Create New Product Page</h2>
        <button type="button" class="btn btn-secondary btn-sm" on:click={loadExampleData}>
          Load Example
        </button>
      </div>

      <form on:submit|preventDefault={generateProduct}>
        <div class="form-row">
          <div class="form-group">
            <label for="name" class="form-label">Product Name *</label>
            <input 
              type="text" 
              id="name"
              class="form-input" 
              bind:value={formData.name}
              placeholder="e.g., Colombian Dark Roast Coffee"
              required
            />
          </div>

          <div class="form-group">
            <label for="category" class="form-label">Category *</label>
            <input 
              type="text" 
              id="category"
              class="form-input" 
              bind:value={formData.category}
              placeholder="e.g., Gourmet Coffee"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Features *</label>
          {#each formData.features as feature, index}
            <div class="input-group">
              <input 
                type="text" 
                class="form-input" 
                bind:value={formData.features[index]}
                placeholder="e.g., Single-Origin Excellence"
              />
              <button 
                type="button" 
                class="btn btn-danger btn-sm"
                on:click={() => removeFeature(index)}
                disabled={formData.features.length <= 1}
              >
                Remove
              </button>
            </div>
          {/each}
          <button type="button" class="btn btn-secondary btn-sm" on:click={addFeature}>
            + Add Feature
          </button>
        </div>

        <div class="form-group">
          <label class="form-label">Keywords *</label>
          {#each formData.keywords as keyword, index}
            <div class="input-group">
              <input 
                type="text" 
                class="form-input" 
                bind:value={formData.keywords[index]}
                placeholder="e.g., dark roast coffee"
              />
              <button 
                type="button" 
                class="btn btn-danger btn-sm"
                on:click={() => removeKeyword(index)}
                disabled={formData.keywords.length <= 1}
              >
                Remove
              </button>
            </div>
          {/each}
          <button type="button" class="btn btn-secondary btn-sm" on:click={addKeyword}>
            + Add Keyword
          </button>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="location" class="form-label">Location *</label>
            <input 
              type="text" 
              id="location"
              class="form-input" 
              bind:value={formData.location}
              placeholder="e.g., USA"
              required
            />
          </div>

          <div class="form-group">
            <label for="target_audience" class="form-label">Target Audience *</label>
            <input 
              type="text" 
              id="target_audience"
              class="form-input" 
              bind:value={formData.target_audience}
              placeholder="e.g., Coffee lovers who enjoy bold flavors"
              required
            />
          </div>
        </div>

        <div class="form-actions">
          <button type="submit" class="btn btn-primary" disabled={loading}>
            {#if loading}
              Generating...
            {:else}
              🚀 Generate SEO Page
            {/if}
          </button>
          <button type="button" class="btn btn-secondary" on:click={resetForm}>
            Clear Form
          </button>
        </div>
      </form>
    </section>

    <!-- Products List Section -->
    <section class="products-section card">
      <h2>Existing Products ({products.length})</h2>
      
      {#if products.length === 0}
        <div class="empty-state">
          <p>No products created yet. Use the form to create your first SEO page!</p>
        </div>
      {:else}
        <div class="products-table">
          {#each products as product}
            <div class="product-row">
              <div class="product-info">
                <h3>
                  <a href="/products/{product.slug}" target="_blank" class="product-link">
                    {product.name}
                  </a>
                </h3>
                <p class="product-meta">
                  {product.category} • {product.location} • 
                  Created {new Date(product.created_at).toLocaleDateString()}
                </p>
                <div class="product-features">
                  {#each product.features.slice(0, 3) as feature}
                    <span class="feature-tag">{feature}</span>
                  {/each}
                  {#if product.features.length > 3}
                    <span class="feature-tag more">+{product.features.length - 3} more</span>
                  {/if}
                </div>
              </div>
              <div class="product-actions">
                <a href="/products/{product.slug}" target="_blank" class="btn btn-primary btn-sm">
                  View Page
                </a>
                <button 
                  class="btn btn-danger btn-sm"
                  on:click={() => deleteProduct(product.slug, product.name)}
                >
                  Delete
                </button>
              </div>
            </div>
          {/each}
        </div>
      {/if}
    </section>
  </div>
</div>

<style>
  .admin-header {
    text-align: center;
    margin-bottom: 3rem;
  }

  .admin-header h1 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
    color: #333;
  }

  .admin-header p {
    color: #666;
    font-size: 1.1rem;
  }

  .admin-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: start;
  }

  .section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
  }

  .section-header h2 {
    margin: 0;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }

  .input-group {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }

  .input-group .form-input {
    flex: 1;
  }

  .form-actions {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
  }

  .products-table {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .product-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 1rem;
    border: 1px solid #e9ecef;
    border-radius: 8px;
    transition: box-shadow 0.2s;
  }

  .product-row:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .product-info {
    flex: 1;
  }

  .product-link {
    text-decoration: none;
    color: #007bff;
    font-weight: 600;
  }

  .product-link:hover {
    text-decoration: underline;
  }

  .product-meta {
    color: #666;
    font-size: 0.9rem;
    margin: 0.5rem 0;
  }

  .product-features {
    display: flex;
    flex-wrap: wrap;
    gap: 0.25rem;
  }

  .feature-tag {
    background: #e3f2fd;
    color: #1976d2;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-size: 0.8rem;
  }

  .feature-tag.more {
    background: #f5f5f5;
    color: #666;
  }

  .product-actions {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    min-width: 100px;
  }

  .empty-state {
    text-align: center;
    padding: 2rem;
    color: #666;
  }

  .message.success {
    background: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    border-radius: 6px;
    padding: 1rem;
    margin-bottom: 2rem;
  }

  .message.error {
    background: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    border-radius: 6px;
    padding: 1rem;
    margin-bottom: 2rem;
  }

  @media (max-width: 1024px) {
    .admin-layout {
      grid-template-columns: 1fr;
    }

    .form-row {
      grid-template-columns: 1fr;
    }

    .product-row {
      flex-direction: column;
      gap: 1rem;
    }

    .product-actions {
      flex-direction: row;
      align-self: stretch;
    }
  }

  @media (max-width: 768px) {
    .section-header {
      flex-direction: column;
      gap: 1rem;
      align-items: stretch;
    }

    .form-actions {
      flex-direction: column;
    }
  }
</style> 