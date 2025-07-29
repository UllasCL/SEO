async function load({ fetch }) {
  console.log("🔧 Layout server load - simplified for deployment...");
  return {
    backendHealthy: true
  };
}
export {
  load
};
