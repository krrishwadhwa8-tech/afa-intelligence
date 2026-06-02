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
        auto_adjust=True
    )

    if df.empty:
        raise Exception(f"No data found for {symbol}")

    close_series = df["Close"].astype(float)

    volume_series = df["Volume"].astype(float)

    high_series = df["High"].astype(float)

    avg_volume = volume_series.tail(30).mean()

    today_volume = volume_series.iloc[-1]

    volume_ratio = today_volume / avg_volume

    close_price = close_series.iloc[-1]

    avg_close_20 = close_series.tail(20).mean()

    sma_50 = close_series.tail(50).mean()

    previous_high = high_series.iloc[-21:-1].max()

    rsi = calculate_rsi(
        close_series.tolist()
    )

    volatility = calculate_volatility(
        close_series.tolist()
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