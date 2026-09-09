import sys
import os

from fastapi import Request

backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
sys.path.insert(0, os.path.abspath(backend_dir))

from main import app

@app.middleware("http")
async def normalize_path(request: Request, call_next):
    original = request.headers.get("x-matched-path") or request.headers.get("x-forwarded-uri")
    if original:
        path = original
    else:
        path = request.scope.get("path", "")

    for prefix in ["/api/index.py", "/api/index"]:
        if path.startswith(prefix):
            path = path[len(prefix):] or "/"
            break

    request.scope["path"] = path
    return await call_next(request)
