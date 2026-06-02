def generate_report(results):

    top_stock = results[0]

    report = []

    report.append(
        "================================="
    )

    report.append(
        "AFA Intelligence Market Report"
    )

    report.append(
        "================================="
    )

    report.append("")

    report.append(
        f"Top Stock: {top_stock['symbol']}"
    )

    report.append(
        f"Score: {top_stock['total_score']:.2f}"
    )

    report.append("")

    report.append("Reasons:")

    for reason in top_stock["reasons"]:
        report.append(
            f"✓ {reason}"
        )

    report.append("")

    report.append("Top 3 Stocks:")

    for i, stock in enumerate(
        results[:3],
        start=1
    ):
        report.append(
            f"{i}. {stock['symbol']} "
            f"({stock['total_score']:.2f})"
        )

    return "\n".join(report)