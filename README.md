# Power-Cost-Report-Dashboard
## Commodity Curves (`curves.html`)

Spreads each cost code's hours across its fixed Start/Finish dates from **Sheet1 of `Henderson_BL_Creation.xlsx`** and lets you pick and stamp a curve per code.

- **Curves:** Standard and Bell are the workbook's own Weights formulas (holiday factors applied). Linear, Front, Mid, Mid-back, Back, and Custom (peak % and shape sliders) are added on top.
- **Charts:** weekly hours or manpower (FTE at 60 hrs/week), plus cumulative % complete compared with the workbook curve.
- **Productive vs non-productive:** filter and subtotal by Activity Category (`PD-*` = productive, `NP-*` = non-productive). The project baseline % complete is earned on productive hours only.
- **Stamping:** stamped curves are saved in the browser. Export or import them as JSON, and export weekly hours, cumulative %, or project % complete as CSV.

Refresh the data after editing the workbook:

```
python3 scripts/extract_baseline.py Henderson_BL_Creation.xlsx data/baseline.json
```

The script checks its weekly spread against the workbook's calculated values and reports any mismatch.

Serve the folder (for example with `python3 -m http.server`) and open `curves.html`.
