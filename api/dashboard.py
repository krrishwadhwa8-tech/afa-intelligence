from fastapi import APIRouter

from scanner.market_service import get_market_pulse
from utils.market_status import get_market_status

router = APIRouter()


@router.get("/dashboard")
def dashboard():

    stocks = get_market_pulse()

    hero_stock = stocks[0] if stocks else None

    return {
        "market": get_market_status(),
        "hero_stock": hero_stock,
        "top_stocks": stocks[:5]
    }