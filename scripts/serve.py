"""Serve only the app, on localhost, at a stable address."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DevelopmentHandler(SimpleHTTPRequestHandler):
    """Always serve current local sources without touching browser project data."""
    def send_head(self):
        if 'If-Modified-Since' in self.headers:
            del self.headers['If-Modified-Since']
        return super().send_head()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        super().end_headers()

if __name__ == '__main__':
    handler = partial(DevelopmentHandler, directory=str(ROOT / 'dist'))
    print('Tablica taktyczna: http://localhost:8000 (Ctrl+C kończy)', flush=True)
    try:
        ThreadingHTTPServer(('127.0.0.1', 8000), handler).serve_forever()
    except KeyboardInterrupt:
        pass
