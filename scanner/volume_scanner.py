import yfinance as yf

symbol = "RELIANCE.NS"

print(f"\nAnalyzing {symbol}...\n")

df = yf.download(
    symbol,
    period="30d",
    progress=False,
    auto_adjust=False
)

avg_volume = float(df["Volume"].mean())
today_volume = float(df["Volume"].iloc[-1])

ratio = today_volume / avg_volume

print(f"Average Volume : {avg_volume:,.0f}")
print(f"Today's Volume : {today_volume:,.0f}")
print(f"Volume Ratio   : {ratio:.2f}x")

if ratio > 2:
    print("\n🚨 ALERT: Unusual Volume Activity Detected!")
else:
    print("\n✅ Volume appears normal.")