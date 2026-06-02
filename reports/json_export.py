import json


def export_dashboard_json(results):

    top_stock = results[0]

    data = {
        "top_stock": top_stock["symbol"],
        "top_score": round(
            top_stock["total_score"], 2
        ),
        "reasons": top_stock["reasons"],
        "top_3": [
            stock["symbol"]
            for stock in results[:3]
        ]
    }

    with open(
        "data/dashboard.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )