# عناصر التلاوة — Quran Elements

PWA that reads the daily Quran Recorder logs live from `mrbugimposter3-ship-it/quran-recorder/logs/YYYY-MM-DD.json` and maps each ayah stamp to a chemical element:
- Surah mapping: Z = ((surah − 1) mod 118) + 1 = surah (surah ≤ 114)
- Ayah mapping: Z = ayah mod 118 (0 → 118)

Shows the day's modal elements, a periodic-table heat map, and curated everyday product types with Walmart/Amazon search links (no scraping, no prices). Refreshes every 10 minutes. `gen.py` builds `elements.js`.
