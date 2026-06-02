from fastapi import APIRouter

from scanner.market_service import (
    get_market_pulse
)

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    market_data = get_market_pulse()

    top_stock = (
        market_data[0]
        if market_data
        else None
    )

    return {
        "platform": "AFA Intelligence",
        "top_stock": top_stock,
        "market_pulse": market_data[:5]
    }