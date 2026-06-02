import json
import os

from config.stocks import STOCKS
from scanner.stock_service import analyze_stock

CACHE_FILE = "cache/market_cache.json"


def refresh_market_cache():

    results = []

    for symbol in STOCKS:

        try:

            result = analyze_stock(symbol)

            results.append(result)

        except Exception as e:

            print(f"Failed: {symbol} -> {e}")

    results.sort(
        key=lambda x: x["afa_score"],
        reverse=True
    )

    results = results[:20]

    os.makedirs("cache", exist_ok=True)

    with open(CACHE_FILE, "w") as f:

        json.dump(results, f)

    return results


def get_market_pulse():

    if not os.path.exists(CACHE_FILE):

        return refresh_market_cache()

    with open(CACHE_FILE, "r") as f:

        return json.load(f)