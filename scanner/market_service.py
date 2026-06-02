from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)

from config.stocks import STOCKS
from scanner.stock_service import analyze_stock


market_cache = []


def refresh_market_cache():

    global market_cache

    results = []

    with ThreadPoolExecutor(
        max_workers=20
    ) as executor:

        futures = {
            executor.submit(
                analyze_stock,
                symbol
            ): symbol
            for symbol in STOCKS
        }

        for future in as_completed(
            futures
        ):

            symbol = futures[future]

            try:

                result = future.result()

                if result:

                    results.append(
                        result
                    )

            except Exception as e:

                print(
                    f"Failed: {symbol} -> {e}"
                )

    results.sort(
        key=lambda x: x["afa_score"],
        reverse=True
    )

    market_cache = results[:50]

    print(
        f"Market cache refreshed: "
        f"{len(market_cache)} stocks"
    )

    return market_cache


def get_market_pulse():

    global market_cache

    if not market_cache:

        print(
            "Cache empty. Building..."
        )

        refresh_market_cache()

    return market_cache