/* Barcode → Ayah (deterministic, no randomness). Shared by the app and the build (node).
   Rule: see README "باركود ← آية". */
(function (root) {
  const ABJAD = "ابجدهوزحطيكلمنسعفصقرشتثخذضظغ"; // jummal order, index 1..28
  const JUMMAL = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000];
  const idx = c => ABJAD.indexOf(c) + 1;                 // 1..28
  const band27 = c => ((idx(c) - 1) % 27) + 1;           // mod 27 (غ 28 → 1)
  const digit = c => ((band27(c) - 1) % 9) + 1;          // 1..9 = leading digit of its jummal value
  const red9 = n => (n % 9) || 9;                        // mod 9, 0 → 9 (digital root)
  function upcCheck(s11) { let o = 0, e = 0; for (let i = 0; i < 11; i++) { if (i % 2) e += +s11[i]; else o += +s11[i]; } return (10 - ((o * 3 + e) % 10)) % 10; }
  function normalize(code) {
    let s = String(code || "").replace(/[٠-٩]/g, c => "٠١٢٣٤٥٦٧٨٩".indexOf(c)).replace(/\D/g, "");
    if (s.length === 13 && s[0] === "0") s = s.slice(1);  // EAN-13 with leading 0 = UPC-A
    if (s.length !== 12) return { ok: false, why: "len", s };
    if (upcCheck(s) !== +s[11]) return { ok: false, why: "check", s, want: upcCheck(s) };
    return { ok: true, s };
  }
  // window: 108 letters (12 blocks × 9) starting at the ayah's first letter, continuing into the next ayat (wraps 114:6 → 1:1)
  function windowAt(D, k) { const L = D.L, st = D.S[k], out = []; for (let i = 0; i < 108; i++) out.push(L[(st + i) % L.length]); return out; }
  function scoreWin(w, dg) {
    let blocks = 0, ptr = 0; const hours = [];
    for (let h = 1; h <= 12; h++) {
      const b = w.slice(9 * (h - 1), 9 * h), bsum = b.reduce((a, c) => a + digit(c), 0), bd = red9(bsum);
      const d = red9(+dg[h - 1]), pl = b[d - 1], pd = digit(pl);
      const mb = bd === d, mp = pd === d; blocks += mb; ptr += mp;
      hours.push({ h, from: 9 * (h - 1) + 1, to: 9 * h, raw: +dg[h - 1], d, letters: b.join(""), bsum, bd, mb, pos: 9 * (h - 1) + d, pl, pd, mp });
    }
    return { blocks, ptr, hours };
  }
  // Fast scorer over precomputed digits (Uint8Array of letter digits per stream position)
  function prep(D) { if (D._dg) return; const n = D.L.length, a = new Uint8Array(n); for (let i = 0; i < n; i++) a[i] = digit(D.L[i]); D._dg = a; }
  function best(D, code, topN) {
    prep(D); const A = D._dg, n = A.length, dg = code.split("").map(x => red9(+x)), res = [];
    for (let k = 0; k < D.S.length; k++) {
      const st = D.S[k]; let blocks = 0, ptr = 0;
      for (let h = 0; h < 12; h++) {
        let s = 0; const base = st + 9 * h;
        for (let j = 0; j < 9; j++) s += A[(base + j) % n];
        const d = dg[h]; if (red9(s) === d) blocks++; if (A[(base + d - 1) % n] === d) ptr++;
      }
      res.push([blocks, ptr, k]);
    }
    res.sort((x, y) => y[0] - x[0] || y[1] - x[1] || x[2] - y[2]);   // blocks ↓, pointer ↓, earlier ayah first
    return res.slice(0, topN || 1);
  }
  const api = { ABJAD, JUMMAL, idx, band27, digit, red9, upcCheck, normalize, windowAt, scoreWin, best };
  if (typeof module !== "undefined") module.exports = api; else root.BarcodeAyah = api;
})(this);
