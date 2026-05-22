const defaultServiceOrigin = "http://127.0.0.1:8787";

export function resolveServiceOrigin(env: Record<string, string | undefined> = process.env): string {
  return env.INBOX_SERVICE_URL ?? env.FRE_META_SERVICE_ORIGIN ?? defaultServiceOrigin;
}

export function resolvePort(env: Record<string, string | undefined> = process.env): number {
  return Number(env.PORT ?? "3000");
}

export const html = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>fre-meta-harness inbox</title>
    <style>
      :root {
        --bg: #f4f0e8;
        --panel: #fffaf1;
        --ink: #1d2a22;
        --muted: #5a6b61;
        --green: #2e7d32;
        --amber: #a8681d;
        --red: #a1302d;
      }
      body { margin: 0; font-family: Georgia, 'Iowan Old Style', serif; color: var(--ink); background: radial-gradient(circle at top, #fff7e2, var(--bg)); }
      main { max-width: 1100px; margin: 0 auto; padding: 32px 20px 48px; }
      h1, h2 { margin: 0 0 12px; }
      .meta { color: var(--muted); margin-bottom: 24px; }
      .toolbar { display: flex; gap: 12px; align-items: center; margin-bottom: 24px; }
      button { border: 0; background: var(--ink); color: white; border-radius: 999px; padding: 10px 16px; cursor: pointer; }
      .cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
      .card { background: var(--panel); border: 1px solid #e2d8c5; border-radius: 18px; padding: 18px; box-shadow: 0 8px 30px rgba(0,0,0,0.06); }
      .row { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
      .pill { border-radius: 999px; padding: 4px 10px; font-size: 12px; border: 1px solid currentColor; }
      .green { color: var(--green); }
      .amber { color: var(--amber); }
      .red { color: var(--red); }
      ul { padding-left: 18px; }
      code { background: rgba(0,0,0,0.06); padding: 2px 6px; border-radius: 6px; }
      pre { background: #fbf6eb; padding: 14px; border-radius: 12px; overflow: auto; }
    </style>
  </head>
  <body>
    <main>
      <h1>Inbox Protocol Dashboard</h1>
      <p class="meta">Governed inbox packets, gate state, and routing artifacts for the parent fre-meta-harness.</p>
      <div class="toolbar">
        <button id="scan">Scan inbox</button>
        <button id="refresh">Refresh view</button>
        <span id="status" class="meta">Loading…</span>
      </div>
      <section>
        <h2>Packets</h2>
        <div id="packets" class="cards"></div>
      </section>
      <section>
        <h2>Routing Decisions</h2>
        <pre id="routing"></pre>
      </section>
      <section>
        <h2>Delegation Bundles</h2>
        <pre id="delegation"></pre>
      </section>
    </main>
    <script>
      const statusEl = document.getElementById('status');
      const packetsEl = document.getElementById('packets');
      const routingEl = document.getElementById('routing');
      const delegationEl = document.getElementById('delegation');

      function badgeClass(status) {
        if (status === 'routed' || status === 'green') return 'green';
        if (status === 'needs_clarification' || status === 'amber' || status === 'pending') return 'amber';
        return 'red';
      }

      function renderPacket(packet) {
        const gates = (packet.gate_states || []).map(gate => {
          return '<span class="pill ' + badgeClass(gate.status) + '">' + gate.gate_id + ': ' + gate.status + '</span>';
        }).join('');
        const errors = (packet.errors || []).length
          ? '<ul>' + packet.errors.map(error => '<li>' + error + '</li>').join('') + '</ul>'
          : '<p>No packet errors.</p>';
        return '<article class="card">' +
          '<div class="row"><strong>' + packet.packet_name + '</strong><span class="pill ' + badgeClass(packet.status) + '">' + packet.status + '</span></div>' +
          '<p><code>' + packet.artifact_id + '</code> · ' + packet.producer_role + '</p>' +
          '<div class="row">' + gates + '</div>' +
          '<p>Consumers: ' + (packet.resolved_consumers || []).join(', ') + '</p>' +
          errors +
        '</article>';
      }

      async function loadQueue() {
        statusEl.textContent = 'Loading queue…';
        const response = await fetch('/api/inbox/queue');
        const data = await response.json();
        packetsEl.innerHTML = (data.packets || []).map(renderPacket).join('') || '<article class="card"><p>No governed inbox packets found.</p></article>';
        routingEl.textContent = JSON.stringify(data.routing_decisions || [], null, 2);
        delegationEl.textContent = JSON.stringify(data.delegation_bundles || [], null, 2);
        statusEl.textContent = 'Queue refreshed from Python service.';
      }

      async function scanInbox() {
        statusEl.textContent = 'Running inbox scan…';
        await fetch('/api/inbox/scan', { method: 'POST' });
        await loadQueue();
      }

      document.getElementById('scan').addEventListener('click', scanInbox);
      document.getElementById('refresh').addEventListener('click', loadQueue);
      loadQueue();
    </script>
  </body>
</html>`;

export function createFetchHandler(serviceOrigin: string): (request: Request) => Promise<Response> {
  return async function fetchHandler(request: Request): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return Response.json({ status: "ok" });
    }
    if (url.pathname === "/config.json") {
      return Response.json({ serviceOrigin });
    }
    if (url.pathname.startsWith("/api/")) {
      const target = new URL(url.pathname + url.search, serviceOrigin);
      return fetch(target, {
        method: request.method,
        headers: request.headers,
        body: request.method === "GET" || request.method === "HEAD" ? undefined : await request.text(),
      });
    }
    return new Response(html, {
      headers: { "content-type": "text/html; charset=utf-8" },
    });
  };
}

export function createServer(env: Record<string, string | undefined> = process.env) {
  const serviceOrigin = resolveServiceOrigin(env);
  const port = resolvePort(env);
  return Bun.serve({
    port,
    fetch: createFetchHandler(serviceOrigin),
  });
}

if (import.meta.main) {
  const port = resolvePort();
  createServer();
  console.log(`fre-meta-harness inbox app listening on http://127.0.0.1:${port}`);
}
