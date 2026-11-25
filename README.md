# CASIO VZ-1 Owner's Manual — modern edition

Rebuilt from a scan of the original manual. **Source of truth = plain text in git.**

```
chapters/*.md          prose + tables (Markdown, python-markdown flavour), ordered by filename
figures/make_figures.py every diagram as code (pure Python -> SVG); edit data or geometry there
assets/style.css       screen + print styling
build.py               renders dist/vz1-manual.html (single self-contained file)
OPEN_POINTS.md         uncertain transcriptions / contradictions (also last chapter of the manual)
```

## Build

```bash
pip install -r requirements.txt
python build.py            # HTML
python build.py --pdf      # optional PDF (pip install weasyprint); or print the HTML from a browser
```

## Editing

* Add a figure: write a function decorated with `@fig` in `figures/make_figures.py`, then reference it in Markdown with `{{fig:function_name|Caption}}`.
* Keys are written `<kbd>NAME</kbd>`; spec bars as `<div class="spec">…</div>`; notes as `!!! note`.
* Chapter headings without numbers: `# Title {.nonum}`.
* When resolving an open point, update `chapters/99-open-points.md` **and** `OPEN_POINTS.md`.

Not affiliated with CASIO. VZ-1 is a trademark of CASIO COMPUTER CO., LTD.
