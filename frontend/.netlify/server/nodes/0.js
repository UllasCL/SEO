import * as server from '../entries/pages/_layout.server.js';

export const index = 0;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/pages/_layout.svelte.js')).default;
export { server };
export const server_id = "src/routes/+layout.server.js";
export const imports = ["_app/immutable/nodes/0.8bc1ea46.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.37cfb1fb.js","_app/immutable/chunks/stores.916af4d5.js","_app/immutable/chunks/singletons.2b829cc3.js"];
export const stylesheets = ["_app/immutable/assets/0.ce325fde.css"];
export const fonts = [];
