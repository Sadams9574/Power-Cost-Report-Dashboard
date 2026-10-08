"""Build a single-file Henderson_Commodity_Curves.html with the baseline data inlined,
so it opens directly from disk (no web server needed).

Usage: python3 scripts/build_standalone.py [data/baseline.json] [Henderson_Commodity_Curves.html]
"""
import json
import sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "data/baseline.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "Henderson_Commodity_Curves.html"

html = open("curves.html").read()
data = json.dumps(json.load(open(SRC)), separators=(",", ":")).replace("</", "<\\/")
html = html.replace("<script>\nconst STORE_KEY", f"<script>window.BASELINE_DATA = {data};</script>\n<script>\nconst STORE_KEY", 1)
# The standalone file has no sibling dashboard to link to.
html = html.replace('    <a class="tab" href="index.html" style="text-decoration:none">Cost dashboard</a>\n', "")
assert "window.BASELINE_DATA =" in html
open(OUT, "w").write(html)
print(f"Wrote {OUT} ({len(html) / 1024:.0f} KB)")
