import sys
import os


backend_dir = os.path.join(os.path.dirname(__file__), "..", "backend")
sys.path.insert(0, os.path.abspath(backend_dir))

from fastapi import Request
from main import app

@app.middleware("http")
async def extract_vercel_path(request: Request, call_next):
    real_path = request.query_params.get("__path")
    if real_path:
        while "//" in real_path:
            real_path = real_path.replace("//", "/")
        request.scope["path"] = real_path
    return await call_next(request)
