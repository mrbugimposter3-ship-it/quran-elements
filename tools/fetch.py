import json,time,urllib.request,urllib.parse,sys
UA="QuranElements/1.0 (github.com/mrbugimposter3-ship-it/quran-elements)"
F="code,product_name,brands,stores,countries_tags"
def get(q,page,ps=100):
    u="https://search.openfoodfacts.org/search?"+urllib.parse.urlencode(dict(q=q,page=page,page_size=ps,fields=F))
    for t in range(5):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=60))
        except Exception as e: print("retry",e,file=sys.stderr);time.sleep(5*(t+1))
    raise SystemExit("fail "+q)
out={}
QS={}
for st in ["walmart","amazon","costco"]:
    for c in ["united-states","canada"]:
        QS[(st,c)]=f'stores:{st} AND countries_tags:"en:{c}"'
for c in ["united-states","canada"]:
    QS[("costco-kirkland",c)]=f'brands:"Kirkland Signature" AND countries_tags:"en:{c}"'
for k,q in QS.items():
    j=get(q,1); n=j["count"]; pages=j["page_count"]; print(k,n,pages,flush=True)
    hits=j["hits"]
    for p in range(2,pages+1):
        if p*100>10000: print("cap",k);break
        hits+=get(q,p)["hits"]; time.sleep(0.3)
    out["|".join(k)]=hits
json.dump(out,open("raw_off.json","w"))
print("done",sum(len(v) for v in out.values()))
