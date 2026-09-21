// nocurlbash.com is otherwise a static site (see public/index.html) served
// via the ASSETS binding below. The one piece of actual logic here: accept
// a POST to any path and echo it back as JSON (method/headers/body), the
// same shape as httpbin.org/anything -- so this domain doubles as a
// throwaway webhook-delivery target for testing, instead of 404/405ing on
// every POST like a pure static site would.
//
// The status code is randomized (roughly half the time a 5xx) rather than
// always 200, so it also works as a flaky-endpoint stand-in for exercising
// a webhook relay's pending/retry/backoff behavior, not just its happy path.
const FAILURE_STATUSES = [500, 502, 503];

export default {
  async fetch(request, env) {
    if (request.method === "POST") {
      const headers = Object.fromEntries(request.headers);
      const body = await request.text();
      const succeed = Math.random() < 0.5;
      const status = succeed
        ? 200
        : FAILURE_STATUSES[Math.floor(Math.random() * FAILURE_STATUSES.length)];

      return new Response(
        JSON.stringify(
          {
            method: request.method,
            url: request.url,
            headers,
            body,
            simulated: succeed ? "success" : "failure",
          },
          null,
          2,
        ),
        {
          status,
          headers: { "content-type": "application/json" },
        },
      );
    }

    return env.ASSETS.fetch(request);
  },
};
