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

    return {
        "symbol": symbol,
        "afa_score": score["total_score"],
        "verdict": verdict,
        "volume_score": score["volume_score"],
        "momentum_score": score["momentum_score"],
        "trend_score": score["trend_score"],
        "breakout_score": score["breakout_score"],
        "rsi": rsi,
        "rsi_score": score["rsi_score"],
        "volatility": volatility,
        "volatility_score": score["volatility_score"],
        "reasons": reasons
    }