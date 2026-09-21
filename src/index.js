// nocurlbash.com is otherwise a static site (see public/index.html) served
// via the ASSETS binding below. The one piece of actual logic here: accept
// a POST to any path and echo it back as JSON (method/headers/body), the
// same shape as httpbin.org/anything -- so this domain doubles as a
// throwaway webhook-delivery target for testing, instead of 404/405ing on
// every POST like a pure static site would.
export default {
  async fetch(request, env) {
    if (request.method === "POST") {
      const headers = Object.fromEntries(request.headers);
      const body = await request.text();
      return new Response(
        JSON.stringify(
          {
            method: request.method,
            url: request.url,
            headers,
            body,
          },
          null,
          2,
        ),
        {
          status: 200,
          headers: { "content-type": "application/json" },
        },
      );
    }

    return env.ASSETS.fetch(request);
  },
};
