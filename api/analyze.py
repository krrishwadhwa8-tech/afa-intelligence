from fastapi import APIRouter

from scanner.stock_service import (
    analyze_stock
)

router = APIRouter()


@router.get("/analyze/{symbol}")
def analyze(symbol: str):

    return analyze_stock(symbol)