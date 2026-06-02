import pandas as pd


def calculate_rsi(closes, period=14):

    close = pd.Series(closes)

    delta = close.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.ewm(
        alpha=1 / period,
        adjust=False
    ).mean()

    avg_loss = loss.ewm(
        alpha=1 / period,
        adjust=False
    ).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (
        100 / (1 + rs)
    )

    return round(
        float(rsi.iloc[-1]),
        2
    )


def get_rsi_score(rsi):

    if 50 <= rsi <= 70:
        return 10

    elif 40 <= rsi < 50:
        return 5

    elif 70 < rsi <= 80:
        return 5

    return 0