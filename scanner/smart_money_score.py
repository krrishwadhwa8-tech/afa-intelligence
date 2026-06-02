import yfinance as yf

symbol = "RELIANCE.NS"

df = yf.download(
    symbol,
    period="60d",
    progress=False,
    auto_adjust=False
)

# Volume Score
avg_volume = df["Volume"].tail(30).mean().iloc[0]
today_volume = df["Volume"].iloc[-1].iloc[0]

volume_ratio = today_volume / avg_volume

volume_score = min(volume_ratio * 25, 50)

# Breakout Score
close_price = df["Close"].iloc[-1].iloc[0]

previous_high = (
    df["High"]
    .iloc[-21:-1]
    .max()
    .iloc[0]
)

breakout_score = 50 if close_price > previous_high else 0

# Final Score
smart_money_score = volume_score + breakout_score

print("\n=== Smart Money Analysis ===\n")

print(f"Stock              : {symbol}")
print(f"Volume Ratio       : {volume_ratio:.2f}x")
print(f"Volume Score       : {volume_score:.1f}/50")
print(f"Breakout Score     : {breakout_score}/50")

print(f"\nSmart Money Score  : {smart_money_score:.1f}/100")