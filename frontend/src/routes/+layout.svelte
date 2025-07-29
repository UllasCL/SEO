<script>
  import { page } from '$app/stores';
  
  export let data;
  $: backendHealthy = data?.backendHealthy ?? true;
</script>

<svelte:head>
  <title>SEO Page Generator</title>
  <meta name="description" content="AI-powered SEO page generator for products and services" />
</svelte:head>

<!-- Backend Status Indicator -->
{#if !backendHealthy}
  <div class="backend-status-warning">
    ⚠️ Backend service is unavailable. Some features may not work properly.
    <a href="/admin" class="status-link">Check Admin Panel</a>
  </div>
{/if}

<nav class="navbar">
  <div class="nav-container">
    <a href="/" class="nav-brand">
      SEO Generator
      {#if !backendHealthy}
        <span class="status-indicator offline" title="Backend Offline">●</span>
      {:else}
        <span class="status-indicator online" title="Backend Online">●</span>
      {/if}
    </a>
    <div class="nav-links">
      <a href="/" class:active={$page.url.pathname === '/'}>Home</a>
      <a href="/admin" class:active={$page.url.pathname === '/admin'}>Admin</a>
    </div>
  </div>
</nav>

<main>
  <slot />
</main>

<footer class="footer">
  <div class="footer-content">
    <p>&copy; 2024 SEO Page Generator. Built with SvelteKit & FastAPI.</p>
  </div>
</footer>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
  }

  :global(*) {
    box-sizing: border-box;
  }

  .backend-status-warning {
    background: #fff3cd;
    color: #856404;
    padding: 0.75rem 1rem;
    text-align: center;
    border-bottom: 1px solid #ffeaa7;
    font-size: 0.9rem;
  }

  .status-link {
    color: #007bff;
    text-decoration: none;
    margin-left: 0.5rem;
  }

  .status-link:hover {
    text-decoration: underline;
  }

  .navbar {
    background: #fff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 100;
  }

  .nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
  }

  .nav-brand {
    font-size: 1.5rem;
    font-weight: bold;
    color: #007bff;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .status-indicator {
    font-size: 0.8rem;
    animation: pulse 2s infinite;
  }

  .status-indicator.online {
    color: #28a745;
  }

  .status-indicator.offline {
    color: #dc3545;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }

  .nav-links {
    display: flex;
    gap: 2rem;
  }

  .nav-links a {
    text-decoration: none;
    color: #666;
    font-weight: 500;
    transition: color 0.3s;
  }

  .nav-links a:hover,
  .nav-links a.active {
    color: #007bff;
  }

  main {
    min-height: calc(100vh - 140px);
    padding: 2rem 0;
  }

  .footer {
    background: #fff;
    border-top: 1px solid #eee;
    margin-top: auto;
  }

  .footer-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    text-align: center;
    color: #666;
  }

  :global(.container) {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
  }

  :global(.card) {
    background: white;
    border-radius: 8px;
    padding: 2rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
  }

  :global(.btn) {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    font-weight: 500;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.3s;
  }

  :global(.btn-primary) {
    background: #007bff;
    color: white;
  }

  :global(.btn-primary:hover) {
    background: #0056b3;
  }

  :global(.btn-secondary) {
    background: #6c757d;
    color: white;
  }

  :global(.btn-danger) {
    background: #dc3545;
    color: white;
  }

  :global(.form-group) {
    margin-bottom: 1.5rem;
  }

  :global(.form-label) {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 500;
  }

  :global(.form-input) {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 1rem;
  }

  :global(.form-textarea) {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #ddd;
    border-radius: 6px;
    font-size: 1rem;
    min-height: 100px;
    resize: vertical;
  }

  :global(.loading) {
    text-align: center;
    padding: 2rem;
  }

  :global(.error) {
    color: #dc3545;
    background: #f8d7da;
    border: 1px solid #f5c6cb;
    padding: 1rem;
    border-radius: 6px;
    margin-bottom: 1rem;
  }

  :global(.success) {
    color: #155724;
    background: #d4edda;
    border: 1px solid #c3e6cb;
    padding: 1rem;
    border-radius: 6px;
    margin-bottom: 1rem;
  }

  @media (max-width: 768px) {
    .nav-container {
      padding: 1rem;
    }
    
    .nav-links {
      gap: 1rem;
    }
    
    :global(.container) {
      padding: 0 1rem;
    }
  }
</style> 