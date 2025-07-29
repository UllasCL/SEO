export async function load({ fetch }) {
  console.log('🔧 Layout server load - simplified for deployment...');
  
  // For now, skip backend health check during build
  // This can be done client-side instead
  return {
    backendHealthy: true
  };
} 