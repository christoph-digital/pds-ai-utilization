"""Build the Artifact page from pds/pds-ai-utilization/index.html:
strip the document skeleton, inline the SVG logo, and encode every
non-ASCII character so the page renders correctly whatever charset the host assumes."""
import re, base64, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
src = root / "source"
html = (src / "index.html").read_text("utf-8")

# fonts: replace the Google Fonts link (+ preconnects) with the embedded woff2 faces
fonts_css = (root / "source" / "fonts" / "embedded.css").read_text()
html = re.sub(r'\s*<link rel="preconnect"[^>]*>', "", html)
html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*">',
              "<style>\n" + fonts_css + "\n</style>", html, count=1)
assert "fonts.googleapis" not in html

def inline(m):
    b64 = base64.b64encode((root / m.group(1)).read_bytes()).decode()
    return f'src="data:image/svg+xml;base64,{b64}"'
html = re.sub(r'src="(assets/[^"]+\.svg)"', inline, html)

# 1) standalone file: complete document, opens offline by double-click, identical on every screen
(root / "index.html").write_text(html, encoding="utf-8")

# 2) artifact page: skeleton stripped, ASCII-only
head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
head = re.sub(r"\s*<meta[^>]*>", "", head)
txt = head.strip() + "\n" + body.strip() + "\n"

def css_esc(s):  return "".join(c if ord(c) < 128 else "\\%x " % ord(c) for c in s)
def js_esc(s):   return "".join(c if ord(c) < 128 else ("\\u%04x" % ord(c) if ord(c) <= 0xffff else "\\u{%x}" % ord(c)) for c in s)
def html_esc(s): return "".join(c if ord(c) < 128 else "&#x%X;" % ord(c) for c in s)

out = []
for part in re.split(r"(<style>.*?</style>|<script>.*?</script>)", txt, flags=re.S):
    if part.startswith("<style>"):    out.append(css_esc(part))
    elif part.startswith("<script>"): out.append(js_esc(part))
    else:                             out.append(html_esc(part))
res = "".join(out)
assert all(ord(c) < 128 for c in res)
(root / "artifact.html").write_text(res, encoding="ascii")
print("built", len(res), "bytes; slides:", res.count('<section class="slide'))
