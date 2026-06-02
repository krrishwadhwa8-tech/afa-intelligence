import math
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
        raise Exception(
            f"No data for {symbol}"
        )

    if len(df) < 50:
        raise Exception(
            f"Not enough history for {symbol}"
        )

    # Handle Yahoo Finance MultiIndex safely

    close = df["Close"]

    if hasattr(close, "columns"):
        close = close.iloc[:, 0]

    volume = df["Volume"]

    if hasattr(volume, "columns"):
        volume = volume.iloc[:, 0]

    high = df["High"]

    if hasattr(high, "columns"):
        high = high.iloc[:, 0]

    close = close.dropna()
    volume = volume.dropna()
    high = high.dropna()

    if len(close) < 50:
        raise Exception(
            f"Insufficient close data for {symbol}"
        )

    avg_volume = float(
        volume.tail(30).mean()
    )

    today_volume = float(
        volume.iloc[-1]
    )

    if avg_volume <= 0:
        raise Exception(
            f"Invalid volume data for {symbol}"
        )

    volume_ratio = (
        today_volume / avg_volume
    )

    close_price = float(
        close.iloc[-1]
    )

    avg_close_20 = float(
        close.tail(20).mean()
    )

    sma_50 = float(
        close.tail(50).mean()
    )

    previous_high = float(
        high.iloc[-21:-1].max()
    )

    close_series = []

    for value in close.tolist():

        try:

            value = float(value)

            if (
                not math.isnan(value)
                and not math.isinf(value)
            ):
                close_series.append(
                    value
                )

        except Exception:
            pass

    if len(close_series) < 30:
        raise Exception(
            f"Invalid close series for {symbol}"
        )

    try:
        rsi = calculate_rsi(
            close_series
        )
    except Exception:
        rsi = 50

    try:
        volatility = (
            calculate_volatility(
                close_series
            )
        )
    except Exception:
        volatility = 1

    # Final NaN protection

    values = {
        "volume_ratio": volume_ratio,
        "close_price": close_price,
        "avg_close_20": avg_close_20,
        "sma_50": sma_50,
        "previous_high": previous_high,
        "rsi": rsi,
        "volatility": volatility
    }

    for name, value in values.items():

        if (
            value is None
            or math.isnan(float(value))
            or math.isinf(float(value))
        ):
            raise Exception(
                f"{name} is invalid"
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

        "rsi": round(rsi, 2),
        "rsi_score": score["rsi_score"],

        "volatility": round(
            volatility,
            2
        ),
        "volatility_score": score[
            "volatility_score"
        ],

        "reasons": reasons
    }