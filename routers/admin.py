from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/admin/cache-status")
def cache_status():

    path = "cache/market_cache.json"

    return {
        "exists": os.path.exists(path),
        "path": path
    }