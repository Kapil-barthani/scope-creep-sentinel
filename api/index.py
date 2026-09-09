import sys
import os

from fastapi import Request

backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
sys.path.insert(0, os.path.abspath(backend_dir))

from main import app

@app.middleware("http")
async def normalize_path(request: Request, call_next):
    path = request.scope.get("path", "")
    for prefix in ["/api/index.py", "/api/index", "/api"]:
        if path.startswith(prefix) and path != prefix:
            request.scope["path"] = path[len(prefix):] or "/"
            break
        elif path == prefix:
            request.scope["path"] = "/"
            break
    return await call_next(request)
