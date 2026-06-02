def get_trend_score(
    close_price,
    sma_50
):

    trend_percent = (
        (close_price - sma_50)
        / sma_50
    ) * 100

    if trend_percent >= 15:
        return 20

    elif trend_percent >= 10:
        return 15

    elif trend_percent >= 5:
        return 10

    elif trend_percent >= 2:
        return 5

    return 0