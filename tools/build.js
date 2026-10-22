const fs=require('fs'),B=require('./barcode-ayah.js');
const D=JSON.parse(fs.readFileSync('stream.json'));const U=JSON.parse(fs.readFileSync('uthmani.json')).data.surahs;
const raw=JSON.parse(fs.readFileSync('raw_off.json'));const OUT=process.argv[2];
const P={},stat={rawHits:0,badLen:0,badCheck:0};
const txt=v=>Array.isArray(v)?v.join(', '):(v||'');
for(const [key,hits] of Object.entries(raw)){
  for(const h of hits){stat.rawHits++;
    const n=B.normalize(h.code); if(!n.ok){stat[n.why==='len'?'badLen':'badCheck']++;continue}
    const c=n.s, st=new Set(), co=new Set();
    const stores=txt(h.stores).toLowerCase(), brands=txt(h.brands);
    if(/wal-?mart/.test(stores))st.add('Walmart'); if(/amazon/.test(stores))st.add('Amazon'); if(/costco/.test(stores))st.add('Costco');
    if(/kirkland/i.test(brands)){st.add('Costco')}
    for(const t of h.countries_tags||[]){if(t==='en:united-states')co.add('US');if(t==='en:canada')co.add('CA')}
    if(!st.size||!co.size)continue;
    const name=(txt(h.product_name)||'').trim().slice(0,90), brand=brands.split(',')[0].trim().slice(0,40);
    const p=P[c]||(P[c]={c,n:'',b:'',s:new Set(),k:new Set(),kl:false});
    if(!p.n&&name)p.n=name; if(!p.b&&brand)p.b=brand; st.forEach(x=>p.s.add(x)); co.forEach(x=>p.k.add(x)); if(/kirkland/i.test(brands))p.kl=true;
  }}
const codes=Object.keys(P).sort();console.error('unique',codes.length,stat);
const shards={};const counts={total:codes.length,byStore:{},byCountry:{},byStoreCountry:{},kirkland:0,scores:{}};
let i=0;
for(const c of codes){const p=P[c];const [r]=B.best(D,c,1);
  const row=[c,p.n,p.b,[...p.s].sort().join('+'),[...p.k].sort().join('+'),r[2],r[0],r[1],p.kl?1:0];
  (shards[c[0]]=shards[c[0]]||[]).push(row);
  for(const s of p.s){counts.byStore[s]=(counts.byStore[s]||0)+1;for(const k of p.k){const kk=s+' '+k;counts.byStoreCountry[kk]=(counts.byStoreCountry[kk]||0)+1}}
  for(const k of p.k)counts.byCountry[k]=(counts.byCountry[k]||0)+1; if(p.kl)counts.kirkland++;
  counts.scores[r[0]]=(counts.scores[r[0]]||0)+1;
  if(++i%2000===0)console.error(i);
}
fs.mkdirSync(OUT+'/data/products',{recursive:true});
for(const [d,rows] of Object.entries(shards))fs.writeFileSync(`${OUT}/data/products/p${d}.json`,JSON.stringify(rows));
counts.shards=Object.fromEntries(Object.entries(shards).map(([d,r])=>[d,r.length]));counts.built=new Date().toISOString();counts.source='Open Food Facts (search.openfoodfacts.org), ODbL';
fs.writeFileSync(OUT+'/data/products/index.json',JSON.stringify(counts,null,1));
const names=U.map(s=>s.name),ac=U.map(s=>s.ayahs.length);
fs.writeFileSync(OUT+'/data/letters.json',JSON.stringify({src:'quran-uthmani via api.alquran.cloud (Tanzil); letters only, basmala prefix of ayah 1 removed except 1:1',L:D.L,S:D.S,N:names,C:ac}));
console.log(JSON.stringify(counts,null,1));
