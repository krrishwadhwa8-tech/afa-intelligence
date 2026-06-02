import yfinance as yf
import pandas as pd
from signals.explainer import generate_explanation
from signals.smart_money import calculate_score
from reports.history_manager import save_history
from reports.report_generator import generate_report
from config.stocks import STOCKS
from reports.json_export import export_dashboard_json

stocks = STOCKS

results = []

for symbol in stocks:

    try:

        df = yf.download(
            symbol,
            period="60d",
            progress=False,
            auto_adjust=False
        )

        avg_volume = (
            df["Volume"]
            .tail(30)
            .mean()
            .iloc[0]
        )

        today_volume = (
            df["Volume"]
            .iloc[-1]
            .iloc[0]
        )

        volume_ratio = (
            today_volume / avg_volume
        )

        close_price = (
            df["Close"]
            .iloc[-1]
            .iloc[0]
        )

        avg_close_20 = (
            df["Close"]
            .tail(20)
            .mean()
            .iloc[0]
        )

        sma_50 = (
            df["Close"]
            .tail(50)
            .mean()
            .iloc[0]
        )

        previous_high = (
            df["High"]
            .iloc[-21:-1]
            .max()
            .iloc[0]
        )



        score = calculate_score(
            volume_ratio,
            close_price,
            previous_high,
            avg_close_20,
            sma_50
        )

        reasons = generate_explanation(
            volume_ratio,
            close_price,
            previous_high,
            avg_close_20,
            sma_50
        )

        results.append({
            "symbol": symbol,

            "total_score": score["total_score"],
    
            "volume_score": score["volume_score"],
            "breakout_score": score["breakout_score"],
            "momentum_score": score["momentum_score"],
            "trend_score": score["trend_score"],

            "reasons": reasons
        })

    except Exception as e:
        print(
            f"Error with {symbol}: {e}"
        )

results.sort(
    key=lambda x: x["total_score"],
    reverse=True
)


save_history(results)

export_dashboard_json(results)

report = generate_report(results)

print("\n")
print(report)

print("\n=== TOP SMART MONEY STOCKS ===\n")

for stock in results:

    print("\n" + "=" * 40)

    print(stock["symbol"])

    print(
        f"Total Score : "
        f"{stock['total_score']:.1f}"
    )

    print(
        f"Volume      : "
        f"{stock['volume_score']:.1f}"
    )

    print(
        f"Breakout    : "
        f"{stock['breakout_score']:.1f}"
    )

    print(
        f"Momentum    : "
        f"{stock['momentum_score']:.1f}"
    )

    print(
        f"Trend       : "
        f"{stock['trend_score']:.1f}"
    )

    print("\nReasons:")

    for reason in stock["reasons"]:
        print(f"  ✓ {reason}")

df_results = pd.DataFrame(results)

df_results.to_csv(
    "data/rankings.csv",
    index=False
)

print("\nResults saved to data/rankings.csv")