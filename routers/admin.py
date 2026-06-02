from fastapi import APIRouter

from scanner.market_service import refresh_market_cache

router = APIRouter()


@router.get("/refresh-market")
def refresh_market():

    data = refresh_market_cache()

    return {
        "success": True,
        "stocks": len(data)
    }