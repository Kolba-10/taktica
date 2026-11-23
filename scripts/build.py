"""Bundle the editable source into one portable HTML file."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def bundle():
    source = ROOT / 'dist'
    html = (source / 'index.html').read_text(encoding='utf-8')
    css = (source / 'style.css').read_text(encoding='utf-8')
    js = (source / 'app.js').read_text(encoding='utf-8')
    assert html.count('<link rel="stylesheet" href="style.css">') == 1
    scripts = re.findall(r'<script src="app\.js(?:\?[^"<>]*)?"></script>', html)
    assert len(scripts) == 1
    return html.replace('<link rel="stylesheet" href="style.css">', '<style>' + css + '</style>').replace(scripts[0], '<script>' + js + '</script>')

if __name__ == '__main__':
    output = ROOT / 'build' / 'Tablica_taktyczna.html'
    output.parent.mkdir(exist_ok=True)
    output.write_text(bundle(), encoding='utf-8')
    print(output)
