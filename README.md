# Power-Cost-Report-Dashboard
## Commodity Curves (`curves.html`)

Spreads each cost code's hours across its fixed Start/Finish dates from **Sheet1 of `Henderson_BL_Creation.xlsx`** and lets you pick and stamp a curve per code.

- **Curves:** Standard and Bell are the workbook's own Weights formulas (holiday factors applied). Linear, Front, Mid, Mid-back, Back, and Custom (set the peak %) are added on top. Change any code's curve in the man-hour table's Curve column. Changes save automatically.
- **Man-hour table by cost code:** for every code, rows of weekly hours, then % (weekly or cumulative % of the hours shown, or each code's own %), then manpower (FTE at 60 hrs/week). Filter by Productive / Non-productive / Both or pick cost codes. At the bottom are subtotals, total hours, weekly and cumulative % complete (plus the entire workbook's cumulative % when filtered), and total manpower.
- **BL date changes:** Start and Finish are editable in the table. Changing them respreads that code's hours over the new working weeks (holiday weeks still apply). Dates that differ from the original Sheet1 baseline are highlighted, hovering shows the BL date, and ↺ sets the row back to the BL dates. Exports include both the current and the BL dates.
- **Graphs:** weekly hours bars and cumulative % lines, built from exactly the rows the table shows.
- **Saving:** **Save HTML with my curves** downloads a copy of the page with every change built in. The table exports to CSV.

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
