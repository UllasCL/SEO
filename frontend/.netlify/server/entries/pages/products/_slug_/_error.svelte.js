import { c as create_ssr_component, b as subscribe, e as escape } from "../../../../chunks/ssr.js";
import { p as page } from "../../../../chunks/stores.js";
const _error_svelte_svelte_type_style_lang = "";
const css = {
  code: ".error-container.svelte-ri9jim.svelte-ri9jim{text-align:center;max-width:600px;margin:4rem auto;padding:2rem}.error-icon.svelte-ri9jim.svelte-ri9jim{font-size:4rem;margin-bottom:1rem}.error-title.svelte-ri9jim.svelte-ri9jim{font-size:2.5rem;margin-bottom:1rem;color:#333}.error-message.svelte-ri9jim.svelte-ri9jim{font-size:1.2rem;color:#666;margin-bottom:2rem}.help-text.svelte-ri9jim.svelte-ri9jim{background:#f8f9fa;padding:1.5rem;border-radius:8px;margin-bottom:2rem;text-align:left}.help-text.svelte-ri9jim ul.svelte-ri9jim{margin:1rem 0;padding-left:1.5rem}.help-text.svelte-ri9jim li.svelte-ri9jim{margin-bottom:0.5rem}.error-actions.svelte-ri9jim.svelte-ri9jim{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:2rem}.suggestions.svelte-ri9jim.svelte-ri9jim{background:linear-gradient(135deg, #667eea 0%, #764ba2 100%);color:white;padding:2rem;border-radius:12px;margin-top:2rem}.suggestions.svelte-ri9jim h3.svelte-ri9jim{margin-bottom:1rem}.suggestions.svelte-ri9jim .btn.svelte-ri9jim{background:white;color:#667eea;margin-top:1rem}.suggestions.svelte-ri9jim .btn.svelte-ri9jim:hover{background:#f8f9fa}@media(max-width: 768px){.error-container.svelte-ri9jim.svelte-ri9jim{padding:1rem}.error-title.svelte-ri9jim.svelte-ri9jim{font-size:2rem}.error-actions.svelte-ri9jim.svelte-ri9jim{flex-direction:column;align-items:center}}",
  map: null
};
const Error = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  let status;
  let message;
  let $page, $$unsubscribe_page;
  $$unsubscribe_page = subscribe(page, (value) => $page = value);
  $$result.css.add(css);
  status = $page.status;
  message = $page.error?.message || "An error occurred";
  $$unsubscribe_page();
  return `${$$result.head += `<!-- HEAD_svelte-1lkmg95_START -->${$$result.title = `<title>Product Not Found - SEO Page Generator</title>`, ""}<meta name="robots" content="noindex, nofollow"><!-- HEAD_svelte-1lkmg95_END -->`, ""} <div class="container"><div class="error-container svelte-ri9jim"><div class="error-icon svelte-ri9jim">${status === 404 ? `🔍` : `⚠️`}</div> <h1 class="error-title svelte-ri9jim">${status === 404 ? `Product Not Found` : `Oops! Something went wrong`}</h1> <p class="error-message svelte-ri9jim">${escape(message)}</p> ${status === 404 ? `<div class="help-text svelte-ri9jim" data-svelte-h="svelte-1vtt4n3"><p>The product you&#39;re looking for doesn&#39;t exist or may have been removed.</p> <p>Here&#39;s what you can do:</p> <ul class="svelte-ri9jim"><li class="svelte-ri9jim">Check the URL for typos</li> <li class="svelte-ri9jim">Browse all available products</li> <li class="svelte-ri9jim">Create a new product in the admin panel</li></ul></div>` : ``} <div class="error-actions svelte-ri9jim" data-svelte-h="svelte-1gfzpv6"><a href="/" class="btn btn-primary">← Back to Home</a> <a href="/admin" class="btn btn-secondary">Admin Panel</a></div> ${status === 404 ? `<div class="suggestions svelte-ri9jim" data-svelte-h="svelte-a0npqe"><h3 class="svelte-ri9jim">Create This Product</h3> <p>Want to create a product with this name? Use our admin panel:</p> <a href="/admin" class="btn btn-primary svelte-ri9jim">Create New Product</a></div>` : ``}</div> </div>`;
});
export {
  Error as default
};
