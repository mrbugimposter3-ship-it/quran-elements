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
