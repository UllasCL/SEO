<script>
  import { page } from '$app/stores';
  
  $: status = $page.status;
  $: message = $page.error?.message || 'An error occurred';
</script>

<svelte:head>
  <title>Product Not Found - SEO Page Generator</title>
  <meta name="robots" content="noindex, nofollow" />
</svelte:head>

<div class="container">
  <div class="error-container">
    <div class="error-icon">
      {#if status === 404}
        🔍
      {:else}
        ⚠️
      {/if}
    </div>
    
    <h1 class="error-title">
      {#if status === 404}
        Product Not Found
      {:else}
        Oops! Something went wrong
      {/if}
    </h1>
    
    <p class="error-message">{message}</p>
    
    {#if status === 404}
      <div class="help-text">
        <p>The product you're looking for doesn't exist or may have been removed.</p>
        <p>Here's what you can do:</p>
        <ul>
          <li>Check the URL for typos</li>
          <li>Browse all available products</li>
          <li>Create a new product in the admin panel</li>
        </ul>
      </div>
    {/if}
    
    <div class="error-actions">
      <a href="/" class="btn btn-primary">← Back to Home</a>
      <a href="/admin" class="btn btn-secondary">Admin Panel</a>
    </div>
    
    {#if status === 404}
      <div class="suggestions">
        <h3>Create This Product</h3>
        <p>Want to create a product with this name? Use our admin panel:</p>
        <a href="/admin" class="btn btn-primary">Create New Product</a>
      </div>
    {/if}
  </div>
</div>

<style>
  .error-container {
    text-align: center;
    max-width: 600px;
    margin: 4rem auto;
    padding: 2rem;
  }

  .error-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
  }

  .error-title {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #333;
  }

  .error-message {
    font-size: 1.2rem;
    color: #666;
    margin-bottom: 2rem;
  }

  .help-text {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
    margin-bottom: 2rem;
    text-align: left;
  }

  .help-text ul {
    margin: 1rem 0;
    padding-left: 1.5rem;
  }

  .help-text li {
    margin-bottom: 0.5rem;
  }

  .error-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 2rem;
  }

  .suggestions {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    margin-top: 2rem;
  }

  .suggestions h3 {
    margin-bottom: 1rem;
  }

  .suggestions .btn {
    background: white;
    color: #667eea;
    margin-top: 1rem;
  }

  .suggestions .btn:hover {
    background: #f8f9fa;
  }

  @media (max-width: 768px) {
    .error-container {
      padding: 1rem;
    }

    .error-title {
      font-size: 2rem;
    }

    .error-actions {
      flex-direction: column;
      align-items: center;
    }
  }
</style> 