import json,collections
ABJAD="ابجدهوزحطيكلمنسعفصقرشتثخذضظغ"   # index 1..28 (jummal order)
NORM={"ٱ":"ا","أ":"ا","إ":"ا","آ":"ا","ء":"ا","ؤ":"و","ئ":"ي","ة":"ه","ى":"ي"}
d=json.load(open("uthmani.json"))["data"]["surahs"]
BAS=d[0]["ayahs"][0]["text"].lstrip("\ufeff")
other=collections.Counter()
stream=[];starts=[];refs=[];texts={}
for s in d:
  for a in s["ayahs"]:
    t=a["text"].lstrip("\ufeff")
    if s["number"]!=1 and a["numberInSurah"]==1 and t.startswith(BAS+" "): t=t[len(BAS)+1:]
    starts.append(len(stream));refs.append((s["number"],a["numberInSurah"]))
    for ch in t:
      c=NORM.get(ch,ch)
      if c in ABJAD: stream.append(c)
      elif "\u0621"<=ch<="\u064a" or ch in "\u0671\u06cc\u06a9": other[ch]+=1
print(len(stream),len(starts),other.most_common(10))
json.dump({"L":"".join(stream),"S":starts},open("stream.json","w"),ensure_ascii=False)
