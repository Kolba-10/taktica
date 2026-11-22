"""Serve only the app, on localhost, at a stable address."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if __name__ == '__main__':
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT / 'dist'))
    print('Tablica taktyczna: http://localhost:8000 (Ctrl+C kończy)', flush=True)
    try:
        ThreadingHTTPServer(('127.0.0.1', 8000), handler).serve_forever()
    except KeyboardInterrupt:
        pass
