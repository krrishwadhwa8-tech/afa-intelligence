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

    try:

        close = df["Close"].squeeze()
        volume = df["Volume"].squeeze()
        high = df["High"].squeeze()

        avg_volume = float(
            volume.tail(30).mean()
        )

        today_volume = float(
            volume.iloc[-1]
        )

        if avg_volume <= 0:
            raise Exception(
                f"Invalid average volume for {symbol}"
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

            except:
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

        values = [
            volume_ratio,
            close_price,
            avg_close_20,
            sma_50,
            previous_high,
            rsi,
            volatility
        ]

        for value in values:

            if (
                value is None
                or math.isnan(value)
                or math.isinf(value)
            ):
                raise Exception(
                    f"Invalid numeric value: {value}"
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

    except Exception as e:

        raise Exception(
            f"{symbol}: {str(e)}"
        )