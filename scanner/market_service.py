from config.stocks import STOCKS
from scanner.stock_service import analyze_stock


def get_market_pulse():

    results = []

    for symbol in STOCKS:

        try:

            result = analyze_stock(symbol)

            results.append(result)

        except Exception:
            pass

    results.sort(
        key=lambda x: x["afa_score"],
        reverse=True
    )

    return results[:20]