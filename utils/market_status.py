from datetime import datetime
import pytz


def get_market_status():
    india = pytz.timezone("Asia/Kolkata")
    now = datetime.now(india)

    weekday = now.weekday()

    if weekday >= 5:
        return {
            "is_open": False,
            "status": "Market Closed"
        }

    market_open = now.replace(
        hour=9,
        minute=15,
        second=0,
        microsecond=0
    )

    market_close = now.replace(
        hour=15,
        minute=30,
        second=0,
        microsecond=0
    )

    if market_open <= now <= market_close:
        return {
            "is_open": True,
            "status": "Market Open"
        }

    return {
        "is_open": False,
        "status": "Market Closed"
    }