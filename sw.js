const C='qelements-v3',F=['./','index.html','elements.js','infaq.js','barcode.html','barcode-ayah.js','data/letters.json','manifest.webmanifest','icon-192.png','icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(F)));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;const u=new URL(e.request.url);
 if(u.hostname==='raw.githubusercontent.com'){const k=new Request(u.origin+u.pathname);
  e.respondWith(fetch(e.request).then(r=>{if(r.ok){const cp=r.clone();caches.open(C).then(c=>c.put(k,cp))}return r}).catch(()=>caches.match(k).then(r=>r||Response.error())));return}
 if(u.origin!==location.origin)return;
 e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true})))});
