

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.4992c901.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.37cfb1fb.js","_app/immutable/chunks/stores.2653550b.js","_app/immutable/chunks/singletons.a11b2737.js"];
export const stylesheets = [];
export const fonts = [];
