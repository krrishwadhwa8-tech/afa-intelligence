def generate_explanation(
    volume_ratio,
    close_price,
    previous_high,
    avg_close_20,
    sma_50
):

    reasons = []

    # Volume

    if volume_ratio >= 2:
        reasons.append(
            f"Volume is {volume_ratio:.1f}x above average, indicating elevated market participation."
        )

    elif volume_ratio >= 1.2:
        reasons.append(
            f"Volume is slightly above average ({volume_ratio:.1f}x)."
        )

    # Breakout

    breakout_percent = (
        (close_price - previous_high)
        / previous_high
    ) * 100

    if breakout_percent > 0:
        reasons.append(
            f"Price is trading {breakout_percent:.2f}% above recent resistance."
        )

    # Momentum

    momentum_percent = (
        (close_price - avg_close_20)
        / avg_close_20
    ) * 100

    if momentum_percent > 0:
        reasons.append(
            f"Positive momentum detected ({momentum_percent:.2f}% above 20-day average)."
        )

    # Trend

    trend_percent = (
        (close_price - sma_50)
        / sma_50
    ) * 100

    if trend_percent > 0:
        reasons.append(
            f"Trading {trend_percent:.2f}% above the 50-day trend line."
        )

    if not reasons:
        reasons.append(
            "No significant technical signals detected at this time."
        )

    return reasons