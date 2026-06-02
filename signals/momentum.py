def get_momentum_score(
    current_close,
    avg_close_20
):

    momentum_percent = (
        (current_close - avg_close_20)
        / avg_close_20
    ) * 100

    if momentum_percent >= 10:
        return 20

    elif momentum_percent >= 7:
        return 15

    elif momentum_percent >= 5:
        return 10

    elif momentum_percent >= 2:
        return 5

    return 0