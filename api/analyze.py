from fastapi import APIRouter, HTTPException

from scanner.stock_service import analyze_stock

router = APIRouter()


@router.get("/analyze/{symbol}")
def analyze(symbol: str):

    try:
        # Clean input
        symbol = symbol.upper().strip()

        # Automatically support Indian NSE stocks
        if not symbol.endswith(".NS") and not symbol.endswith(".BO"):
            symbol = f"{symbol}.NS"

        return analyze_stock(symbol)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )