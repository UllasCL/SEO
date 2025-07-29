export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set(["_redirects"]),
	mimeTypes: {},
	_: {
		client: {"start":"_app/immutable/entry/start.cda28c37.js","app":"_app/immutable/entry/app.314673e9.js","imports":["_app/immutable/entry/start.cda28c37.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/singletons.826363e0.js","_app/immutable/chunks/control.c2cf8273.js","_app/immutable/entry/app.314673e9.js","_app/immutable/chunks/scheduler.e108d1fd.js","_app/immutable/chunks/index.37cfb1fb.js"],"stylesheets":[],"fonts":[]},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js')),
			__memo(() => import('./nodes/2.js')),
			__memo(() => import('./nodes/3.js')),
			__memo(() => import('./nodes/4.js')),
			__memo(() => import('./nodes/5.js'))
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 3 },
				endpoint: null
			},
			{
				id: "/admin",
				pattern: /^\/admin\/?$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 4 },
				endpoint: null
			},
			{
				id: "/products/[slug]",
				pattern: /^\/products\/([^/]+?)\/?$/,
				params: [{"name":"slug","optional":false,"rest":false,"chained":false}],
				page: { layouts: [0,,], errors: [1,2,], leaf: 5 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		}
	}
}
})();
