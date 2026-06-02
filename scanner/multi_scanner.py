import yfinance as yf

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    "SBIN.NS",
    "ITC.NS",
    "LT.NS"
]

results = []

for symbol in stocks:
    try:
        df = yf.download(
            symbol,
            period="30d",
            progress=False,
            auto_adjust=False
        )

        avg_volume = df["Volume"].mean().iloc[0]
        today_volume = df["Volume"].iloc[-1].iloc[0]

        ratio = today_volume / avg_volume

        results.append({
            "symbol": symbol,
            "ratio": ratio
        })

    except Exception as e:
        print(f"Error processing {symbol}: {e}")

results.sort(
    key=lambda x: x["ratio"],
    reverse=True
)

print("\n=== Volume Ranking ===\n")

for stock in results:
    print(
        f"{stock['symbol']:15} "
        f"{stock['ratio']:.2f}x"
    )