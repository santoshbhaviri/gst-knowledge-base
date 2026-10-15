const { chromium } = require('playwright');
const https = require('https'); const fs = require('fs'); const tls = require('tls');
const { HttpsProxyAgent } = (()=>{try{return require('https-proxy-agent')}catch(e){return {}}})();
const ca = fs.readFileSync(process.env.S + '/bundle-le.pem');
const proxy = process.env.HTTPS_PROXY;
// fetch through proxy with custom CA using CONNECT
const http = require('http');
function fetchVia(url, method, headers, body) {
  return new Promise((resolve, reject) => {
    const u = new URL(url); const p = new URL(proxy);
    const req = http.request({ host: p.hostname, port: p.port, method: 'CONNECT', path: `${u.hostname}:443`, headers: p.username ? {'Proxy-Authorization': 'Basic ' + Buffer.from(decodeURIComponent(p.username)+':'+decodeURIComponent(p.password)).toString('base64')} : {} });
    req.on('connect', (res, socket) => {
      if (res.statusCode !== 200) return reject(new Error('CONNECT ' + res.statusCode));
      const h = Object.assign({}, headers); delete h['host'];
      const r2 = https.request({ socket, servername: u.hostname, ca, host: u.hostname, path: u.pathname + u.search, method, headers: h, agent: false }, (res2) => {
        const chunks = []; res2.on('data', c => chunks.push(c)); res2.on('end', () => resolve({ status: res2.statusCode, headers: res2.headers, body: Buffer.concat(chunks) }));
      });
      r2.on('error', reject); if (body) r2.write(body); r2.end();
    });
    req.on('error', reject); req.end();
  });
}
const fetchOnce = fetchVia;
async function fetchRetry(url, method, headers, body) {
  let last;
  for (let i = 0; i < 5; i++) {
    try {
      const h = Object.assign({}, headers); h['accept-encoding'] = 'identity';
      const r = await fetchOnce(url, method, h, body);
      const ct = String(r.headers['content-type']||'');
      if (ct.includes('html') && r.status === 200 && !/<\/html>\s*$/i.test(r.body.toString().slice(-200))) { last = new Error('truncated'); continue; }
      return r;
    } catch (e) { last = e; await new Promise(r => setTimeout(r, 1500)); }
  }
  throw last;
}
module.exports = { fetchVia: fetchRetry };
if (require.main === module) {
  (async () => {
    const browser = await chromium.launch();
    const ctx = await browser.newContext({ acceptDownloads: true });
    await ctx.route('**/*', async (route) => {
      const r = route.request(); const url = r.url();
      if (!url.includes('egazette') || /\.(png|jpe?g|gif|css|woff2?|ico)(\?|$)/i.test(url)) return route.abort();
      try {
        const res = await fetchRetry(url, r.method(), await r.allHeaders(), r.postDataBuffer()); if(process.env.DBG) console.error(r.method(), res.status, url.slice(0,120), res.headers.location||'');
        const hd = {}; for (const [k, v] of Object.entries(res.headers)) hd[k] = Array.isArray(v) ? v.join('\n') : v;
        if (res.status >= 300 && res.status < 400 && res.headers.location) { const loc = new URL(res.headers.location, url).href; delete hd['location']; hd['content-type']='text/html'; delete hd['content-length']; delete hd['content-encoding']; return route.fulfill({ status: 200, headers: hd, body: '<html><body><script>location.replace(' + JSON.stringify(loc) + ')</script></body></html>' }); }
        await route.fulfill({ status: res.status, headers: hd, body: res.body });
      } catch (e) { console.error('ERR', url, e.message); route.abort(); }
    });
    const page = await ctx.newPage();
    const script = require(process.argv[2]);
    await script(page, ctx);
    await browser.close();
  })();
}
