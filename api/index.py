import sys
import os


backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
sys.path.insert(0, os.path.abspath(backend_dir))

from fastapi import Request
from main import app

@app.api_route("/debug", methods=["GET", "POST"])
@app.api_route("/api/debug", methods=["GET", "POST"])
@app.api_route("/api/index.py/debug", methods=["GET", "POST"])
async def debug_endpoint(request: Request):
    return {
        "url_path": request.url.path,
        "scope_path": request.scope.get("path"),
        "headers": {k: v for k, v in request.headers.items() if "auth" not in k.lower()}
    }

@app.api_route("/{full_path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"])
async def catch_all_debug(request: Request, full_path: str):
    return {
        "caught_path": full_path,
        "url_path": request.url.path,
        "scope_path": request.scope.get("path"),
        "method": request.method
    }
