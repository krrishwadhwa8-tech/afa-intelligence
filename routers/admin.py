from fastapi import APIRouter

from scanner.market_service import (
    refresh_market_cache,
    get_market_pulse
)

router = APIRouter()


@router.get("/market-pulse")
def market_pulse():

    return {
        "top_stocks": get_market_pulse()
    }


@router.get("/admin/refresh-market-cache")
def refresh_cache():

    data = refresh_market_cache()

    return {
        "message": "cache refreshed",
        "stocks": len(data)
    }


@router.get("/admin/cache-status")
def cache_status():

    data = get_market_pulse()

    return {
        "cached_stocks": len(data)
    }