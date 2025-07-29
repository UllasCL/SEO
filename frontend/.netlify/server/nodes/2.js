

export const index = 2;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/products/_slug_/_error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/2.2aa83b0d.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.37cfb1fb.js","_app/immutable/chunks/stores.8b503561.js","_app/immutable/chunks/singletons.826363e0.js"];
export const stylesheets = ["_app/immutable/assets/2.6a4897bd.css"];
export const fonts = [];
