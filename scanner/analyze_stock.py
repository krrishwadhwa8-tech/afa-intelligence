import sys
from signals.verdict import get_verdict
import yfinance as yf
from signals.rsi import calculate_rsi
from signals.smart_money import calculate_score
from signals.explainer import generate_explanation
from signals.volatility import (
    calculate_volatility
)

if len(sys.argv) < 2:

    print(
        "Usage: python -m scanner.analyze_stock SYMBOL"
    )

    sys.exit()

symbol = sys.argv[1]

df = yf.download(
    symbol,
    period="1y",
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

close_series = (
    df["Close"]
    .iloc[:, 0]
    .tolist()
)

rsi = calculate_rsi(close_series)

volatility = calculate_volatility(
    close_series
)

score = calculate_score(
    volume_ratio,
    close_price,
    previous_high,
    avg_close_20,
    sma_50,
    rsi,
    volatility
)




verdict = get_verdict(
    score["total_score"]
)

reasons = generate_explanation(
    volume_ratio,
    close_price,
    previous_high,
    avg_close_20,
    sma_50
)

print("=" * 40)

print(
    "AFA Intelligence Stock Analysis"
)

print("=" * 40)

print()

print(f"Stock: {symbol}")

print()

print(
    f"Total Score : "
    f"{score['total_score']:.2f}"
)

print(
    f"Volume      : "
    f"{score['volume_score']:.2f}"
)

print(
    f"Momentum    : "
    f"{score['momentum_score']:.2f}"
)

print(
    f"Trend       : "
    f"{score['trend_score']:.2f}"
)

print(
    f"Breakout    : "
    f"{score['breakout_score']:.2f}"
)

print(
    f"RSI         : "
    f"{rsi:.2f}"
)

print(
    f"RSI Score   : "
    f"{score['rsi_score']:.2f}"
)

print(
    f"Volatility  : "
    f"{volatility:.2f}"
)

print(
    f"Vol Score   : "
    f"{score['volatility_score']:.2f}"
)

print("\nReasons:")

for reason in reasons:

    print(
        f"✓ {reason}"
    )

print()

print(
    f"Verdict: {verdict}"
)