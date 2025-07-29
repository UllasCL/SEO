

export const index = 4;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/admin/_page.svelte.js')).default;
export const imports = ["_app/immutable/nodes/4.ebcf692c.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.37cfb1fb.js","_app/immutable/chunks/api.3a2e407a.js"];
export const stylesheets = ["_app/immutable/assets/4.27a2a8bc.css"];
export const fonts = [];
