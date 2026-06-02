from datetime import datetime, timedelta

from config.stocks import STOCKS
from scanner.stock_service import analyze_stock


CACHE = {
    "data": None,
    "last_update": None
}

CACHE_MINUTES = 5


def get_market_pulse():

    global CACHE

    # Return cached data if still fresh
    if (
        CACHE["data"] is not None
        and CACHE["last_update"] is not None
        and datetime.now() - CACHE["last_update"] < timedelta(minutes=CACHE_MINUTES)
    ):
        print("Using cached market pulse")
        return CACHE["data"]

    print("Refreshing market pulse...")

    results = []

    for symbol in STOCKS:

        try:

            result = analyze_stock(symbol)

            if result:
                results.append(result)

        except Exception as e:

            print(f"Failed for {symbol}: {e}")

    results.sort(
        key=lambda x: x["afa_score"],
        reverse=True
    )

    top_results = results[:20]

    CACHE["data"] = top_results
    CACHE["last_update"] = datetime.now()

    return top_results