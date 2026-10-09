# Power-Cost-Report-Dashboard
## Commodity Curves (`curves.html`)

Spreads each cost code's hours across its fixed Start/Finish dates from **Sheet1 of `Henderson_BL_Creation.xlsx`** and lets you pick and stamp a curve per code.

- **Curves:** Standard and Bell are the workbook's own Weights formulas (holiday factors applied). Linear, Front, Mid, Mid-back, Back, and Custom (set the peak %) are added on top. Change any code's curve in the man-hour table's Curve column. Changes save automatically.
- **Man-hour table by cost code:** weekly hours and manpower (FTE at 60 hrs/week) for every code, with Productive / Non-productive / Both and cost code picker filters, and subtotals and totals at the bottom.
- **Graphs:** weekly hours bars and cumulative % lines, built from exactly the rows the table shows. With picked codes, the entire workbook is shown for comparison.
- **% complete table by cost code:** built from the man-hour table, with the same filters. Show weekly % or cumulative % of the hours shown (each week's column adds up to the total), or each code's own % complete.
- **Saving:** **Save HTML with my curves** downloads a copy of the page with every change built in. Both tables export to CSV.

Refresh the data after editing the workbook:

```
python3 scripts/extract_baseline.py Henderson_BL_Creation.xlsx data/baseline.json
```

The script checks its weekly spread against the workbook's calculated values and reports any mismatch.

Serve the folder (for example with `python3 -m http.server`) and open `curves.html`.

**Single-file version:** `Henderson_Commodity_Curves.html` has the data built in, so you can open it straight from disk or email it. Rebuild it after refreshing the data:

```
python3 scripts/build_standalone.py
```
