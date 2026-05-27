#!/usr/bin/env python3
"""ei-wiki Markdown vault 的零依赖浏览器预览器。"""

from __future__ import annotations

import argparse
import html
import os
import re
import socketserver
import sys
import urllib.parse
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = ("wiki",)
DEFAULT_PAGE = "wiki/index.md"
GROUP_LABELS = {"wiki": "Wiki"}
NAV_SECTIONS = (
    (
        "入口",
        (
            "wiki/index.md",
            "wiki/map.md",
        ),
    ),
    (
        "概念",
        (
            "wiki/concepts/ontology.md",
            "wiki/concepts/palantir-dynamic-ontology.md",
            "wiki/concepts/data-logic-action.md",
            "wiki/concepts/semantic-layer.md",
            "wiki/concepts/oag.md",
            "wiki/concepts/semantic-compilation.md",
            "wiki/concepts/ontology-relation-types.md",
        ),
    ),
    (
        "机制",
        (
            "wiki/mechanisms/ontology-runtime-loop.md",
            "wiki/mechanisms/data-to-ontology-mapping.md",
            "wiki/mechanisms/logic-execution.md",
            "wiki/mechanisms/governed-action.md",
            "wiki/mechanisms/feedback-and-evolution.md",
        ),
    ),
    (
        "方法",
        (
            "wiki/methods/small-ontology-path.md",
            "wiki/methods/ontology-centered-delivery.md",
            "wiki/methods/field-deployment-engineering.md",
        ),
    ),
    (
        "问题与可能性",
        (
            "wiki/questions.md",
            "wiki/applications/risk.md",
        ),
    ),
)


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for directory in CONTENT_DIRS:
        base = ROOT / directory
        if base.exists():
            files.extend(path for path in base.rglob("*.md") if path.is_file())
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def safe_content_path(rel_path: str) -> Path | None:
    rel_path = urllib.parse.unquote(rel_path).strip("/")
    if not rel_path:
        rel_path = DEFAULT_PAGE
    if not rel_path.endswith(".md"):
        rel_path = f"{rel_path}.md"

    candidate = (ROOT / rel_path).resolve()
    try:
        candidate.relative_to(ROOT / "wiki")
    except ValueError:
        return None
    if not candidate.is_file() or candidate.suffix != ".md":
        return None
    return candidate


def resolve_candidate(current: Path, target: str) -> Path | None:
    target = target.strip()
    if not target:
        return None
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None

    target = target.split("#", 1)[0]
    if target.endswith(".md"):
        candidate = (current.parent / target).resolve()
    elif "/" in target:
        candidate = (ROOT / "wiki" / f"{target}.md").resolve()
    else:
        candidate = (ROOT / "wiki" / f"{target}.md").resolve()

    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def resolve_link(current: Path, target: str) -> str:
    target = target.strip()
    if not target:
        return "#"
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return target

    candidate = resolve_candidate(current, target)
    if candidate is None:
        return "#"
    rel = candidate.relative_to(ROOT).as_posix()
    return f"/page/{urllib.parse.quote(rel)}"


def inline_markdown(text: str, current: Path) -> str:
    escaped = html.escape(text)

    def wikilink(match: re.Match[str]) -> str:
        raw = match.group(1)
        target, _, label = raw.partition("|")
        candidate = resolve_candidate(current, target)
        label = label or (page_title(candidate) if candidate else target)
        return f'<a href="{resolve_link(current, target)}">{html.escape(label)}</a>'

    def markdown_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = html.unescape(match.group(2))
        href = resolve_link(current, target)
        return f'<a href="{href}">{label}</a>'

    escaped = re.sub(r"\[\[([^\]]+)\]\]", wikilink, escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", markdown_link, escaped)
    return escaped


def render_table(lines: list[str], current: Path) -> str | None:
    if len(lines) < 2 or not all(line.strip().startswith("|") for line in lines[:2]):
        return None
    separator = lines[1].strip().strip("|")
    if not re.fullmatch(r"\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*", separator):
        return None

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    headers = cells(lines[0])
    body = lines[2:]
    output = ["<table><thead><tr>"]
    output.extend(f"<th>{inline_markdown(cell, current)}</th>" for cell in headers)
    output.append("</tr></thead><tbody>")
    for line in body:
        output.append("<tr>")
        output.extend(f"<td>{inline_markdown(cell, current)}</td>" for cell in cells(line))
        output.append("</tr>")
    output.append("</tbody></table>")
    return "".join(output)


def markdown_to_html(markdown: str, current: Path) -> str:
    output: list[str] = []
    lines = markdown.splitlines()
    index = 0
    if lines and lines[0].strip() == "---":
        index = 1
        while index < len(lines) and lines[index].strip() != "---":
            index += 1
        if index < len(lines):
            index += 1
    in_code = False
    code_lines: list[str] = []
    list_stack: list[str] = []

    def close_lists() -> None:
        while list_stack:
            output.append(f"</{list_stack.pop()}>")

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines = []
                in_code = False
            else:
                close_lists()
                in_code = True
            index += 1
            continue

        if in_code:
            code_lines.append(line)
            index += 1
            continue

        if not stripped:
            close_lists()
            index += 1
            continue

        if stripped.startswith("|"):
            table_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            table = render_table(table_lines, current)
            if table:
                close_lists()
                output.append(table)
            else:
                output.extend(f"<p>{inline_markdown(row, current)}</p>" for row in table_lines)
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            close_lists()
            level = len(heading.group(1))
            text = inline_markdown(heading.group(2), current)
            anchor = re.sub(r"[^a-z0-9]+", "-", html.unescape(heading.group(2)).lower()).strip("-")
            output.append(f'<h{level} id="{anchor}">{text}</h{level}>')
            index += 1
            continue

        quote = re.match(r"^>\s*(.+)$", stripped)
        if quote:
            close_lists()
            output.append(f"<blockquote>{inline_markdown(quote.group(1), current)}</blockquote>")
            index += 1
            continue

        bullet = re.match(r"^[-*]\s+(.+)$", stripped)
        ordered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if bullet or ordered:
            tag = "ul" if bullet else "ol"
            if not list_stack or list_stack[-1] != tag:
                close_lists()
                output.append(f"<{tag}>")
                list_stack.append(tag)
            item = bullet.group(1) if bullet else ordered.group(1)
            output.append(f"<li>{inline_markdown(item, current)}</li>")
            index += 1
            continue

        close_lists()
        paragraph = [stripped]
        index += 1
        while index < len(lines) and lines[index].strip() and not re.match(
            r"^(#{1,6})\s+|^[-*]\s+|^\d+\.\s+|^>\s+|^```|^\|", lines[index].strip()
        ):
            paragraph.append(lines[index].strip())
            index += 1
        output.append(f"<p>{inline_markdown(' '.join(paragraph), current)}</p>")

    close_lists()
    if in_code:
        output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
    return "\n".join(output)


def page_title(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except UnicodeDecodeError:
        pass
    return path.stem.replace("-", " ").replace("_", " ")


def render_sidebar(active: Path) -> str:
    sections: list[str] = []
    for label, rel_paths in NAV_SECTIONS:
        sections.append(f"<h2>{html.escape(label)}</h2><ul>")
        for rel_path in rel_paths:
            path = ROOT / rel_path
            if not path.exists():
                continue
            rel = path.relative_to(ROOT).as_posix()
            href = f"/page/{urllib.parse.quote(rel)}"
            klass = "active" if path == active else ""
            link_label = page_title(path)
            sections.append(f'<li><a class="{klass}" href="{href}">{html.escape(link_label)}</a></li>')
        sections.append("</ul>")
    return "\n".join(sections)


def render_page(path: Path) -> bytes:
    rel = path.relative_to(ROOT).as_posix()
    body = markdown_to_html(path.read_text(encoding="utf-8"), path)
    title = page_title(path)
    sidebar = render_sidebar(path)
    source_path = html.escape(rel)
    document = f"""<!doctype html>
<html lang="en">
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
      <h1><a href="/page/{DEFAULT_PAGE}">企业智能 wiki</a></h1>
      {sidebar}
    </nav>
    <main>
      <div class="source">{source_path}</div>
      {body}
    </main>
  </div>
</body>
</html>"""
    return document.encode("utf-8")


class WikiHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.handle_request(send_body=True)

    def do_HEAD(self) -> None:
        self.handle_request(send_body=False)

    def handle_request(self, send_body: bool) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ("/", "/page"):
            self.redirect(f"/page/{DEFAULT_PAGE}")
            return
        if parsed.path.startswith("/page/"):
            path = safe_content_path(parsed.path.removeprefix("/page/"))
            if path is None:
                self.respond(HTTPStatus.NOT_FOUND, "未找到".encode("utf-8"), "text/plain; charset=utf-8", send_body)
                return
            self.respond(HTTPStatus.OK, render_page(path), "text/html; charset=utf-8", send_body)
            return
        self.respond(HTTPStatus.NOT_FOUND, "未找到".encode("utf-8"), "text/plain; charset=utf-8", send_body)

    def log_message(self, format: str, *args: object) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))

    def redirect(self, location: str) -> None:
        self.send_response(HTTPStatus.FOUND)
        self.send_header("Location", location)
        self.end_headers()

    def respond(self, status: HTTPStatus, body: bytes, content_type: str, send_body: bool = True) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if send_body:
            self.wfile.write(body)


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def main() -> int:
    parser = argparse.ArgumentParser(description="在浏览器中预览 ei-wiki Markdown。")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8765, type=int)
    parser.add_argument("--port-tries", default=20, type=int, help="顺序尝试的端口数量。")
    args = parser.parse_args()

    os.chdir(ROOT)
    last_error: OSError | None = None
    for port in range(args.port, args.port + max(args.port_tries, 1)):
        try:
            with ReusableTCPServer((args.host, port), WikiHandler) as server:
                print(f"正在预览 ei-wiki：http://{args.host}:{port}/")
                print("按 Ctrl-C 停止。")
                try:
                    server.serve_forever()
                except KeyboardInterrupt:
                    print()
                return 0
        except OSError as error:
            last_error = error
            if error.errno != 48:
                raise
    if last_error:
        print(f"无法绑定预览端口：{last_error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
