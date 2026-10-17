import json
raw="""1|H|Hydrogen|هيدروجين
2|He|Helium|هيليوم
3|Li|Lithium|ليثيوم
4|Be|Beryllium|بيريليوم
5|B|Boron|بورون
6|C|Carbon|كربون
7|N|Nitrogen|نيتروجين
8|O|Oxygen|أكسجين
9|F|Fluorine|فلور
10|Ne|Neon|نيون
11|Na|Sodium|صوديوم
12|Mg|Magnesium|مغنيسيوم
13|Al|Aluminum|ألومنيوم
14|Si|Silicon|سيليكون
15|P|Phosphorus|فوسفور
16|S|Sulfur|كبريت
17|Cl|Chlorine|كلور
18|Ar|Argon|أرغون
19|K|Potassium|بوتاسيوم
20|Ca|Calcium|كالسيوم
21|Sc|Scandium|سكانديوم
22|Ti|Titanium|تيتانيوم
23|V|Vanadium|فاناديوم
24|Cr|Chromium|كروم
25|Mn|Manganese|منغنيز
26|Fe|Iron|حديد
27|Co|Cobalt|كوبالت
28|Ni|Nickel|نيكل
29|Cu|Copper|نحاس
30|Zn|Zinc|زنك
31|Ga|Gallium|غاليوم
32|Ge|Germanium|جرمانيوم
33|As|Arsenic|زرنيخ
34|Se|Selenium|سيلينيوم
35|Br|Bromine|بروم
36|Kr|Krypton|كريبتون
37|Rb|Rubidium|روبيديوم
38|Sr|Strontium|سترونشيوم
39|Y|Yttrium|إتريوم
40|Zr|Zirconium|زركونيوم
41|Nb|Niobium|نيوبيوم
42|Mo|Molybdenum|موليبدينوم
43|Tc|Technetium|تكنيشيوم
44|Ru|Ruthenium|روثينيوم
45|Rh|Rhodium|روديوم
46|Pd|Palladium|بالاديوم
47|Ag|Silver|فضة
48|Cd|Cadmium|كادميوم
49|In|Indium|إنديوم
50|Sn|Tin|قصدير
51|Sb|Antimony|إثمد (أنتيمون)
52|Te|Tellurium|تيلوريوم
53|I|Iodine|يود
54|Xe|Xenon|زينون
55|Cs|Cesium|سيزيوم
56|Ba|Barium|باريوم
57|La|Lanthanum|لانثانوم
58|Ce|Cerium|سيريوم
59|Pr|Praseodymium|براسيوديميوم
60|Nd|Neodymium|نيوديميوم
61|Pm|Promethium|بروميثيوم
62|Sm|Samarium|ساماريوم
63|Eu|Europium|يوروبيوم
64|Gd|Gadolinium|غادولينيوم
65|Tb|Terbium|تربيوم
66|Dy|Dysprosium|ديسبروسيوم
67|Ho|Holmium|هولميوم
68|Er|Erbium|إربيوم
69|Tm|Thulium|ثوليوم
70|Yb|Ytterbium|إتيربيوم
71|Lu|Lutetium|لوتيشيوم
72|Hf|Hafnium|هافنيوم
73|Ta|Tantalum|تنتالوم
74|W|Tungsten|تنغستن
75|Re|Rhenium|رينيوم
76|Os|Osmium|أوزميوم
77|Ir|Iridium|إيريديوم
78|Pt|Platinum|بلاتين
79|Au|Gold|ذهب
80|Hg|Mercury|زئبق
81|Tl|Thallium|ثاليوم
82|Pb|Lead|رصاص
83|Bi|Bismuth|بزموت
84|Po|Polonium|بولونيوم
85|At|Astatine|أستاتين
86|Rn|Radon|رادون
87|Fr|Francium|فرانسيوم
88|Ra|Radium|راديوم
89|Ac|Actinium|أكتينيوم
90|Th|Thorium|ثوريوم
91|Pa|Protactinium|بروتكتينيوم
92|U|Uranium|يورانيوم
93|Np|Neptunium|نبتونيوم
94|Pu|Plutonium|بلوتونيوم
95|Am|Americium|أمريسيوم
96|Cm|Curium|كوريوم
97|Bk|Berkelium|بركليوم
98|Cf|Californium|كاليفورنيوم
99|Es|Einsteinium|أينشتاينيوم
100|Fm|Fermium|فرميوم
101|Md|Mendelevium|مندليفيوم
102|No|Nobelium|نوبليوم
103|Lr|Lawrencium|لورنسيوم
104|Rf|Rutherfordium|رذرفورديوم
105|Db|Dubnium|دوبنيوم
106|Sg|Seaborgium|سيبورغيوم
107|Bh|Bohrium|بوريوم
108|Hs|Hassium|هاسيوم
109|Mt|Meitnerium|مايتنريوم
110|Ds|Darmstadtium|دارمشتاتيوم
111|Rg|Roentgenium|رونتجينيوم
112|Cn|Copernicium|كوبرنيسيوم
113|Nh|Nihonium|نيهونيوم
114|Fl|Flerovium|فليروفيوم
115|Mc|Moscovium|موسكوفيوم
116|Lv|Livermorium|ليفرموريوم
117|Ts|Tennessine|تينيسين
118|Og|Oganesson|أوغانيسون"""
# products: Z -> [(arabic, english search term)]
P={
1:[("ماء مقطّر","distilled water"),("بيروكسيد الهيدروجين 3%","hydrogen peroxide 3%")],
2:[("بالونات الهيليوم","helium balloons"),("أسطوانة هيليوم للبالونات","helium tank for balloons")],
3:[("بطاريات ليثيوم AA","lithium AA batteries"),("بطارية شحن متنقلة","power bank")],
5:[("بوراكس للغسيل","borax laundry booster"),("أواني زجاج بوروسيليكات","borosilicate glass food containers")],
6:[("فحم منشّط","activated charcoal"),("أقلام رصاص جرافيت","graphite pencils")],
7:[("سماد نيتروجيني للنباتات","nitrogen plant fertilizer"),("قهوة نيترو باردة","nitro cold brew coffee")],
8:[("ماء مقطّر","distilled water"),("مضخة هواء لحوض السمك","aquarium air pump")],
9:[("معجون أسنان بالفلورايد","fluoride toothpaste"),("مقلاة غير لاصقة","nonstick frying pan")],
10:[("لافتة نيون","neon sign")],
11:[("ملح البحر","sea salt"),("بيكربونات الصوديوم (بيكنج صودا)","baking soda")],
12:[("مكمّل مغنيسيوم","magnesium supplement"),("ملح إبسوم","epsom salt")],
13:[("ورق ألومنيوم","aluminum foil"),("زجاجة ماء ألومنيوم","aluminum water bottle")],
14:[("قوالب خبز سيليكون","silicone baking mat"),("سيليكا جل لامتصاص الرطوبة","silica gel packets")],
15:[("سماد فوسفات","phosphate fertilizer"),("أعواد ثقاب","matches")],
16:[("سماد كبريت للحديقة","garden sulfur"),("صابون الكبريت","sulfur soap")],
17:[("ملح الطعام","table salt"),("أنابيب PVC","PVC pipe")],
18:[("مصباح متوهّج","incandescent light bulb"),("نوافذ زجاج مزدوج","double pane window")],
19:[("بديل ملح بالبوتاسيوم","potassium salt substitute"),("مكمّل بوتاسيوم","potassium supplement")],
20:[("مكمّل كالسيوم","calcium supplement"),("طباشير","sidewalk chalk")],
21:[("مضرب بيسبول سكانديوم","scandium baseball bat")],
22:[("مجوهرات تيتانيوم","titanium jewelry"),("نظارة بإطار تيتانيوم","titanium eyeglass frames"),("واقي شمس بثاني أكسيد التيتانيوم","titanium dioxide sunscreen")],
23:[("مفاتيح ربط كروم فاناديوم","chrome vanadium wrench set")],
24:[("أواني ستانلس ستيل","stainless steel cookware"),("صنبور مطلي بالكروم","chrome faucet")],
25:[("بطاريات قلوية","alkaline batteries"),("مكمّل منغنيز","manganese supplement")],
26:[("مقلاة حديد زهر","cast iron skillet"),("مكمّل حديد","iron supplement")],
27:[("لقم ثقب كوبالت","cobalt drill bits"),("فيتامين ب12","vitamin B12")],
28:[("أواني ستانلس ستيل","stainless steel cookware"),("بطاريات NiMH قابلة للشحن","NiMH rechargeable batteries")],
29:[("أواني طبخ نحاسية","copper cookware"),("كوب نحاسي","copper mug"),("سلك كهرباء نحاسي","copper wire")],
30:[("مكمّل زنك","zinc supplement"),("واقي شمس أكسيد الزنك","zinc oxide sunscreen")],
31:[("شاحن GaN","GaN charger")],
34:[("مكمّل سيلينيوم","selenium supplement"),("شامبو سيلينيوم","selenium sulfide shampoo")],
36:[("مصباح كشّاف كريبتون","krypton flashlight bulb")],
38:[("ملصقات تتوهّج في الظلام","glow in the dark stickers")],
40:[("سكين سيراميك زركونيا","zirconia ceramic knife"),("خاتم زركون","cubic zirconia ring")],
41:[("أقراط نيوبيوم","niobium earrings")],
42:[("شحم موليبدينوم","moly grease"),("إطار دراجة كروم موليبدينوم","chromoly bike frame")],
45:[("مجوهرات مطلية بالروديوم","rhodium plated jewelry")],
46:[("خاتم بالاديوم","palladium ring"),("أقراط بالاديوم","palladium earrings")],
47:[("مجوهرات فضة","sterling silver jewelry"),("ملاعق وأدوات مائدة فضية","silver flatware")],
50:[("علب صفيح للتخزين","tin storage containers"),("قصدير لحام خالٍ من الرصاص","lead free solder")],
53:[("ملح مدعّم باليود","iodized salt"),("مكمّل يود من عشب البحر","kelp iodine supplement")],
54:[("مصابيح سيارة زينون","xenon headlight bulbs")],
57:[("حجر قدّاحة","lighter flint")],
58:[("بودرة أكسيد السيريوم لتلميع الزجاج","cerium oxide polishing powder"),("قضيب إشعال فيروسيريوم","ferrocerium fire starter")],
59:[("نظارات زجاج ديديميوم","didymium glasses")],
60:[("مغناطيس نيوديميوم","neodymium magnets"),("نظارات زجاج ديديميوم","didymium glasses")],
62:[("مغناطيس ساماريوم كوبالت","samarium cobalt magnet")],
63:[("ملصقات تتوهّج في الظلام","glow in the dark stickers")],
74:[("خاتم تنغستن","tungsten ring"),("لقم ثقب كربيد التنغستن","tungsten carbide drill bit")],
77:[("شمعات احتراق إيريديوم","iridium spark plugs")],
78:[("خاتم بلاتين","platinum ring"),("شمعات احتراق بلاتين","platinum spark plugs")],
79:[("مجوهرات ذهب","gold jewelry"),("قلادة ذهب","gold necklace")],
83:[("دواء بيبتو بيسمول","Pepto Bismol"),("بلورة بزموت للزينة","bismuth crystal")],
}
TOX={4,33,35,48,51,56,76,80,81,82}  # toxic: no suggestions
RAD={43,61}|set(range(84,119))
rows=[]
for line in raw.splitlines():
    z,s,en,ar=line.split('|');z=int(z)
    # position
    if z==1:p,g=1,1
    elif z==2:p,g=1,18
    elif z<=10:p=2;g=z-2 if z<=4 else z+8
    elif z<=18:p=3;g=z-10 if z<=12 else z
    elif z<=36:p,g=4,z-18
    elif z<=54:p,g=5,z-36
    elif 57<=z<=71:p,g=9,z-54
    elif 89<=z<=103:p,g=10,z-86
    elif z<=86:p=6;g=z-54 if z<=56 else z-68
    else:p=7;g=z-86 if z<=88 else z-100
    k='rad' if z in RAD else 'tox' if z in TOX else ('ok' if z in P else 'rare')
    rows.append([z,s,en,ar,p,g,k,[list(x) for x in P.get(z,[])]])
open('elements.js','w').write('const ELEMENTS='+json.dumps(rows,ensure_ascii=False)+';\n')
# sanity: unique positions
pos=[(r[4],r[5]) for r in rows];assert len(set(pos))==118,len(set(pos))
print(sum(1 for r in rows if r[6]=='rare'),[r[1] for r in rows if r[6]=='rare'])
