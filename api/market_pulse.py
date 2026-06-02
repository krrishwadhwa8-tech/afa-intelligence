from fastapi import APIRouter

from scanner.market_service import (
    get_market_pulse
)

router = APIRouter()


@router.get("/market-pulse")
def market_pulse():

    return {
        "top_stocks": get_market_pulse()
    }