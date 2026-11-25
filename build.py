#!/usr/bin/env python3
"""Render the manual: chapters/*.md + figures -> dist/vz1-manual.html (single file).
Usage: python build.py [--pdf]      (pdf needs `pip install weasyprint`)
Requires: pip install markdown
Figure syntax in Markdown:  {{fig:name|Caption text}}  (name = function in figures/make_figures.py)"""
import re, sys, subprocess, pathlib
import markdown

ROOT = pathlib.Path(__file__).parent
DIST = ROOT / "dist"

def main():
    subprocess.run([sys.executable, str(ROOT / "figures" / "make_figures.py")], check=True)
    md_text = "\n\n".join(p.read_text(encoding="utf-8") for p in sorted((ROOT / "chapters").glob("*.md")))
    figs, n = {}, [0]
    def stash(m):
        n[0] += 1
        name, cap = m.group(1), (m.group(2) or "").strip()
        svg = (ROOT / "figures" / "svg" / f"{name}.svg").read_text(encoding="utf-8")
        tok = f"FIGTOKEN{n[0]}X"
        figs[tok] = f'<figure id="fig-{name}">{svg}<figcaption><b>Figure {n[0]}.</b> {cap}</figcaption></figure>'
        return f"\n\n{tok}\n\n"
    md_text = re.sub(r"\{\{fig:([\w-]+)(?:\|([^}]*))?\}\}", stash, md_text)
    md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "toc", "admonition", "sane_lists"],
                           extension_configs={"toc": {"toc_depth": "1-2", "permalink": False}})
    body = md.convert(md_text)
    for tok, html in figs.items():
        body = body.replace(f"<p>{tok}</p>", html)
    css = (ROOT / "assets" / "style.css").read_text(encoding="utf-8")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>CASIO VZ-1 Owner's Manual (modern edition)</title>
<style>{css}</style></head><body><nav id="toc"><h2>Contents</h2>{md.toc}</nav><main>{body}</main></body></html>"""
    DIST.mkdir(exist_ok=True)
    out = DIST / "vz1-manual.html"
    out.write_text(page, encoding="utf-8")
    print("wrote", out)
    if "--pdf" in sys.argv:
        from weasyprint import HTML
        HTML(string=page).write_pdf(DIST / "vz1-manual.pdf"); print("wrote PDF")

if __name__ == "__main__":
    main()
