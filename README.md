# عناصر التلاوة — Quran Elements

PWA that reads the daily Quran Recorder logs live from `mrbugimposter3-ship-it/quran-recorder/logs/YYYY-MM-DD.json` and maps each ayah stamp to a chemical element:
- Surah mapping: Z = ((surah − 1) mod 118) + 1 = surah (surah ≤ 114)
- Ayah mapping: Z = ayah mod 118 (0 → 118)

Shows the day's modal elements, a periodic-table heat map, and curated everyday product types with Walmart/Amazon search links (no scraping, no prices). Refreshes every 10 minutes. `gen.py` builds `elements.js`.

## الإنفاق في سبيل الله · Spending in the way of Allah

> مَّثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمْ فِى سَبِيلِ ٱللَّهِ كَمَثَلِ حَبَّةٍ أَنۢبَتَتْ سَبْعَ سَنَابِلَ فِى كُلِّ سُنۢبُلَةٍۢ مِّا۟ئَةُ حَبَّةٍۢ ۗ وَٱللَّهُ يُضَٰعِفُ لِمَن يَشَآءُ ۗ وَٱللَّهُ وَٰسِعٌ عَلِيمٌ ﴿٢٦١﴾
>
> — سُورَةُ البَقَرَةِ 2:261

> ءَامِنُوا۟ بِٱللَّهِ وَرَسُولِهِۦ وَأَنفِقُوا۟ مِمَّا جَعَلَكُم مُّسْتَخْلَفِينَ فِيهِ ۖ فَٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ وَأَنفَقُوا۟ لَهُمْ أَجْرٌۭ كَبِيرٌۭ ﴿٧﴾
>
> — سُورَةُ الحَدِيدِ 57:7

The app shows a rotating card of ayat on zakat and charity (2:43, 2:245, 2:261, 2:267, 2:274, 9:41, 9:60, 57:7, 61:10–11, 64:16). Text: Tanzil Uthmani via [Al Quran Cloud](https://alquran.cloud) (`quran-uthmani`), used verbatim; generated into `infaq.js`, not typed by hand.

## Tools we use · أدوات نستخدمها

[Postiz](https://postiz.pro/mr-bug) for scheduling social posts. This is a **referral link** (we may earn a commission). It is a tool recommendation, not a charity.

## باركود ← آية · Barcode → Ayah (`barcode.html`)

Type or scan (Chrome on Android, `BarcodeDetector`) a 12-digit UPC-A barcode; the page gives the one ayah it maps to, the 12-hour clock of the match, and a browsable list of food products. Nothing is random: the same barcode always gives the same ayah.

**Rule**
1. Take the ayah's letters in order from the Uthmani text (rasm letters only; marks, dagger alef, small waw/yaa and tatweel are skipped; ٱ أ إ آ ء → ا, ؤ → و, ئ → ي, ة → ه, ى → ي). If the ayah has fewer than 108 letters, keep going into the next ayat (114:6 wraps to 1:1). The basmala prefix of ayah 1 is not counted, except in 1:1.
2. Cut those 108 letters into 12 blocks of 9, one per clock hour: hour 1 = letters 1–9, hour 2 = 10–18, hour 3 = 19–27, hour 4 = 28–36, hour 5 = 37–45 … hour 12 = 100–108.
3. Each letter gets a digit 1–9: its abjad (jummal) index 1–27 taken mod 9, which is the leading digit of its jummal value (ا 1, ي 10 and ق 100 all give 1; ظ 900 gives 9). غ = 1000 is index 28, which is 1 under mod 27, so it gives 1.
4. Block digit = the sum of its 9 letter digits mod 9, with 0 read as 9.
5. Barcode digit *h* (hour *h*) is reduced the same way: mod 9, with 0 read as 9. A **block match** is when it equals block *h*'s digit.
6. The same reduced digit is also a position 1–9 inside block *h*. A **position match** is when the letter in that position has that digit.
7. All 6,236 ayat are tested, each starting at its own first letter. The winner has the most block matches, then the most position matches, then comes first in the mushaf. So every valid barcode lands on exactly one ayah.

**Worked example (past letter 100):** `064100778979` (Kellogg's Mini Wheats, Walmart Canada) maps to **45:34**, with 6/12 block matches and 3/12 position matches. Hour 12 is letters 100–108, which run into 45:35: ا ل د ن ي ا ف ا ل. Their digits are 1+3+4+5+1+1+8+1+3 = 27, and 27 mod 9 = 0, read as 9. The 12th barcode digit is 9, which also reduces to 9, so it's a block match ✓. Position 9 in that block is letter 108, ل (30), whose digit is 3. 3 ≠ 9, so it's not a position match ✗.

The check digit is validated (EAN-13 codes starting with 0 have the 0 removed). The page shows the Uthmani text from `api.alquran.cloud` (`quran-uthmani`), exactly as given, the same source as the infaq card. The match is arithmetic only and carries no tafsir meaning.

**Data:** [Open Food Facts](https://world.openfoodfacts.org) under ODbL/DbCL. Products tagged with a Walmart, Amazon or Costco store (plus the Kirkland Signature brand) and sold in the United States or Canada, keeping only valid 12-digit UPC-A codes. Only product names, brands, stores and countries are stored, with no shopping links. Files: `data/products/pN.json` (sharded by first digit, rows `[upc, name, brand, stores, countries, ayahIndex, blockMatches, positionMatches, kirkland]`), `data/products/index.json` (counts), and `data/letters.json` (letter stream and ayah starts). Rebuild with `tools/fetch.py`, `tools/letters.py`, then `node tools/build.js .`.
