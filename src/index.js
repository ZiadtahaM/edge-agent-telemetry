export default {
  async fetch(request, env, ctx) {
    const environment = env.ENVIRONMENT || 'development';
    return new Response(JSON.stringify({ message: "Hello from companion worker", environment }), {
      headers: { "content-type": "application/json" }
    });
  }
};
