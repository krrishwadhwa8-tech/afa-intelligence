from fastapi import APIRouter
import os

from scanner.market_service import refresh_market_cache

router = APIRouter()


@router.get("/admin/cache-status")
def cache_status():

    path = "cache/market_cache.json"

    return {
        "exists": os.path.exists(path),
        "path": path
    }


@router.get("/admin/refresh-market-cache")
def refresh_cache():

    data = refresh_market_cache()

    return {
        "message": "cache refreshed",
        "stocks": len(data)
    }   