import yfinance as yf

from signals.smart_money import calculate_score
from signals.verdict import get_verdict
from signals.explainer import generate_explanation
from signals.rsi import calculate_rsi
from signals.volatility import calculate_volatility


def analyze_stock(symbol):

    df = yf.download(
        symbol,
        period="60d",
        progress=False,
        auto_adjust=False
    )

    if df.empty:
        raise Exception(f"No data for {symbol}")

    # Convert all columns safely to Series
    close = df["Close"].squeeze()
    volume = df["Volume"].squeeze()
    high = df["High"].squeeze()

    avg_volume = volume.tail(30).mean()

    today_volume = volume.iloc[-1]

    volume_ratio = today_volume / avg_volume

    close_price = close.iloc[-1]

    avg_close_20 = close.tail(20).mean()

    sma_50 = close.tail(50).mean()

    previous_high = high.iloc[-21:-1].max()

    close_series = close.tolist()

    rsi = calculate_rsi(close_series)

    volatility = calculate_volatility(close_series)

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

    return {
        "symbol": symbol,
        "afa_score": score["total_score"],
        "verdict": verdict,

        "volume_score": score["volume_score"],
        "momentum_score": score["momentum_score"],
        "trend_score": score["trend_score"],
        "breakout_score": score["breakout_score"],

        "rsi": round(rsi, 2),
        "rsi_score": score["rsi_score"],

        "volatility": round(volatility, 2),
        "volatility_score": score["volatility_score"],

        "reasons": reasons
    }