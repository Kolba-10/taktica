"""Bundle the editable source into one portable HTML file."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def bundle():
    source = ROOT / 'dist'
    html = (source / 'index.html').read_text(encoding='utf-8')
    css = (source / 'style.css').read_text(encoding='utf-8')
    js = (source / 'app.js').read_text(encoding='utf-8')
    assert html.count('<link rel="stylesheet" href="style.css">') == 1
    assert html.count('<script src="app.js"></script>') == 1
    return html.replace('<link rel="stylesheet" href="style.css">', '<style>' + css + '</style>').replace('<script src="app.js"></script>', '<script>' + js + '</script>')

if __name__ == '__main__':
    output = ROOT / 'build' / 'Tablica_taktyczna.html'
    output.parent.mkdir(exist_ok=True)
    output.write_text(bundle(), encoding='utf-8')
    print(output)
