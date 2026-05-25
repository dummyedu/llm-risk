#!/usr/bin/env python3
"""Build the ei-wiki Markdown vault into a static GitHub Pages site."""

from __future__ import annotations

import argparse
import html
import os
import shutil
import urllib.parse
from pathlib import Path

import wiki_preview


ROOT = wiki_preview.ROOT
DEFAULT_PAGE = ROOT / wiki_preview.DEFAULT_PAGE
DEFAULT_OUTPUT = ROOT / "site"


def output_rel_for(source_path: Path) -> Path:
    rel = source_path.relative_to(ROOT / "wiki")
    if rel == Path("index.md"):
        return Path("index.html")
    return rel.with_suffix(".html")


def output_path_for(source_path: Path, output_dir: Path) -> Path:
    return output_dir / output_rel_for(source_path)


def quote_href(href: str) -> str:
    return urllib.parse.quote(href.replace(os.sep, "/"), safe="/#.:?=&%-")


def static_href(current: Path, target: Path, output_dir: Path) -> str:
    current_output = output_path_for(current, output_dir)
    target_output = output_path_for(target, output_dir)
    rel = os.path.relpath(target_output, start=current_output.parent)
    return quote_href(rel)


def resolve_static_link(current: Path, target: str, output_dir: Path) -> str:
    target = target.strip()
    if not target:
        return "#"
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return target

    target_path, separator, anchor = target.partition("#")
    candidate = wiki_preview.resolve_candidate(current, target_path)
    if candidate is None and target_path.startswith("wiki/"):
        candidate_path = (ROOT / target_path).resolve()
        try:
            candidate_path.relative_to(ROOT / "wiki")
        except ValueError:
            candidate_path = None
        if candidate_path and candidate_path.is_file():
            candidate = candidate_path
    if candidate is None:
        return "#"

    href = static_href(current, candidate, output_dir)
    if separator:
        href = f"{href}#{urllib.parse.quote(anchor)}"
    return href


def render_sidebar(active: Path, output_dir: Path) -> str:
    sections: list[str] = []
    for label, rel_paths in wiki_preview.NAV_SECTIONS:
        sections.append(f"<h2>{html.escape(label)}</h2><ul>")
        for rel_path in rel_paths:
            path = ROOT / rel_path
            if not path.exists():
                continue
            href = static_href(active, path, output_dir)
            klass = "active" if path == active else ""
            link_label = wiki_preview.page_title(path)
            sections.append(f'<li><a class="{klass}" href="{href}">{html.escape(link_label)}</a></li>')
        sections.append("</ul>")
    return "\n".join(sections)


def render_page(path: Path, output_dir: Path) -> str:
    original_resolve_link = wiki_preview.resolve_link
    wiki_preview.resolve_link = lambda current, target: resolve_static_link(current, target, output_dir)
    try:
        body = wiki_preview.markdown_to_html(path.read_text(encoding="utf-8"), path)
    finally:
        wiki_preview.resolve_link = original_resolve_link

    rel = path.relative_to(ROOT).as_posix()
    title = wiki_preview.page_title(path)
    sidebar = render_sidebar(path, output_dir)
    source_path = html.escape(rel)
    home_href = static_href(path, DEFAULT_PAGE, output_dir)
    return f"""<!doctype html>
<html lang="zh-Hans">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} - 企业智能 wiki</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f7f5;
      --panel: #ffffff;
      --text: #1f2933;
      --muted: #667085;
      --line: #d7d9dd;
      --link: #0b5cad;
      --active: #e6f0fb;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    .layout {{
      display: grid;
      grid-template-columns: minmax(220px, 300px) minmax(0, 1fr);
      min-height: 100vh;
    }}
    nav {{
      border-right: 1px solid var(--line);
      background: var(--panel);
      padding: 18px 16px 32px;
      overflow: auto;
      position: sticky;
      top: 0;
      height: 100vh;
    }}
    nav h1 {{
      font-size: 18px;
      margin: 0 0 18px;
    }}
    nav h2 {{
      color: var(--muted);
      font-size: 12px;
      letter-spacing: 0;
      margin: 20px 0 6px;
      text-transform: uppercase;
    }}
    nav ul {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    nav li {{ margin: 2px 0; }}
    nav a {{
      border-radius: 6px;
      color: var(--text);
      display: block;
      overflow-wrap: anywhere;
      padding: 5px 7px;
      text-decoration: none;
    }}
    nav a:hover, nav a.active {{
      background: var(--active);
      color: var(--link);
    }}
    main {{
      max-width: 980px;
      padding: 34px 42px 80px;
      width: 100%;
    }}
    .source {{
      color: var(--muted);
      font-size: 13px;
      margin-bottom: 18px;
    }}
    h1, h2, h3, h4, h5, h6 {{
      line-height: 1.25;
      margin: 1.35em 0 .55em;
    }}
    h1 {{ font-size: 34px; margin-top: 0; }}
    h2 {{ border-bottom: 1px solid var(--line); padding-bottom: 4px; }}
    a {{ color: var(--link); }}
    code {{
      background: #eef1f4;
      border-radius: 4px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: .92em;
      padding: .1em .3em;
    }}
    pre {{
      background: #111827;
      border-radius: 8px;
      color: #f9fafb;
      overflow: auto;
      padding: 14px 16px;
    }}
    pre code {{
      background: transparent;
      color: inherit;
      padding: 0;
    }}
    table {{
      border-collapse: collapse;
      display: block;
      overflow-x: auto;
      width: 100%;
    }}
    th, td {{
      border: 1px solid var(--line);
      padding: 7px 9px;
      text-align: left;
      vertical-align: top;
    }}
    th {{ background: #eef1f4; }}
    blockquote {{
      border-left: 4px solid var(--line);
      color: var(--muted);
      margin-left: 0;
      padding-left: 16px;
    }}
    @media (max-width: 780px) {{
      .layout {{ grid-template-columns: 1fr; }}
      nav {{ height: auto; position: static; }}
      main {{ padding: 24px 20px 60px; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <nav>
      <h1><a href="{home_href}">企业智能 wiki</a></h1>
      {sidebar}
    </nav>
    <main>
      <div class="source">{source_path}</div>
      {body}
    </main>
  </div>
</body>
</html>
"""


def build_site(output_dir: Path) -> int:
    output_dir = output_dir.resolve()
    try:
        output_dir.relative_to(ROOT)
    except ValueError as error:
        raise SystemExit(f"Output directory must be inside the repository: {output_dir}") from error

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    (output_dir / ".nojekyll").write_text("", encoding="utf-8")

    pages = wiki_preview.iter_markdown_files()
    for page in pages:
        output_path = output_path_for(page, output_dir)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(render_page(page, output_dir), encoding="utf-8")

    print(f"Built {len(pages)} pages into {output_dir.relative_to(ROOT)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build static HTML for GitHub Pages.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output directory, default: site")
    args = parser.parse_args()
    return build_site(Path(args.output))


if __name__ == "__main__":
    raise SystemExit(main())
