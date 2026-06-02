import statistics


def calculate_volatility(closes):

    returns = []

    for i in range(1, len(closes)):

        daily_return = (
            (closes[i] - closes[i - 1])
            / closes[i - 1]
        ) * 100

        returns.append(daily_return)

    return round(
        statistics.stdev(returns),
        2
    )


def get_volatility_score(volatility):

    if volatility <= 1:
        return 10

    elif volatility <= 2:
        return 8

    elif volatility <= 3:
        return 5

    elif volatility <= 4:
        return 2

    return 0