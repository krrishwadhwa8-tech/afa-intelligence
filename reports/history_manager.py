import pandas as pd
from datetime import datetime


def save_history(results):

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    rows = []

    for stock in results:

        rows.append({
            "date": today,
            "symbol": stock["symbol"],
            "score": round(stock["total_score"],2)
        })

    df = pd.DataFrame(rows)

    df.to_csv(
        "data/history.csv",
        mode="a",
        header=False,
        index=False
    )