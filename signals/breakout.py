def get_breakout_score(
    close_price,
    previous_high
):

    breakout_percent = (
        (close_price - previous_high)
        / previous_high
    ) * 100

    if breakout_percent >= 5:
        return 20

    elif breakout_percent >= 3:
        return 15

    elif breakout_percent >= 2:
        return 10

    elif breakout_percent >= 1:
        return 5

    return 0