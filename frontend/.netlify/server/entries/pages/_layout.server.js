const API_BASE_URL = {}.VITE_API_BASE_URL || "http://localhost:8000";
async function apiCall(fetch, endpoint, options = {}) {
  const url = `${API_BASE_URL}${endpoint}`;
  console.log(`🌐 Server API call: ${options.method || "GET"} ${url}`);
  try {
    const response = await fetch(url, {
      headers: {
        "Content-Type": "application/json",
        ...options.headers
      },
      ...options
    });
    console.log(`📡 Response: ${response.status} ${response.statusText}`);
    if (!response.ok) {
      const errorText = await response.text().catch(() => "No error details");
      console.error(`❌ API Error ${response.status}: ${errorText}`);
      return {
        success: false,
        status: response.status,
        error: response.statusText,
        details: errorText
      };
    }
    const data = await response.json();
    console.log(`✅ API Success: ${url}`);
    return {
      success: true,
      data
    };
  } catch (err) {
    console.error(`❌ Network Error: ${err.message}`);
    return {
      success: false,
      status: 0,
      error: "Network Error",
      details: err.message
    };
  }
}
async function checkBackendHealth(fetch) {
  const result = await apiCall(fetch, "/");
  return result.success && result.data?.status === "healthy";
}
async function load({ fetch }) {
  console.log("🔧 Layout server load - checking backend health...");
  try {
    const backendHealthy = await checkBackendHealth(fetch);
    console.log(`🏥 Backend health: ${backendHealthy ? "healthy" : "unhealthy"}`);
    return {
      backendHealthy
    };
  } catch (error) {
    console.error("❌ Error checking backend health:", error);
    return {
      backendHealthy: false
    };
  }
}
export {
  load
};
