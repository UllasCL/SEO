import { checkBackendHealth } from '$lib/server-utils.js';

export async function load({ fetch }) {
  console.log('🔧 Layout server load - checking backend health...');
  
  try {
    const backendHealthy = await checkBackendHealth(fetch);
    console.log(`🏥 Backend health: ${backendHealthy ? 'healthy' : 'unhealthy'}`);
    
    return {
      backendHealthy
    };
  } catch (error) {
    console.error('❌ Error checking backend health:', error);
    return {
      backendHealthy: false
    };
  }
} 