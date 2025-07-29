import * as universal from '../entries/pages/products/_slug_/_page.js';
import * as server from '../entries/pages/products/_slug_/_page.server.js';

export const index = 5;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/products/_slug_/_page.svelte.js')).default;
export { universal };
export const universal_id = "src/routes/products/[slug]/+page.js";
export { server };
export const server_id = "src/routes/products/[slug]/+page.server.js";
export const imports = ["_app/immutable/nodes/5.82a04265.js","_app/immutable/chunks/api.3a2e407a.js","_app/immutable/chunks/control.c2cf8273.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.37cfb1fb.js"];
export const stylesheets = ["_app/immutable/assets/5.3dac0083.css"];
export const fonts = [];
