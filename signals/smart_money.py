from signals.volume import get_volume_score
from signals.breakout import get_breakout_score
from signals.momentum import get_momentum_score
from signals.trend import get_trend_score
from signals.rsi import get_rsi_score
from signals.volatility import (
    get_volatility_score
)

def calculate_score(
    volume_ratio,
    close_price,
    previous_high,
    avg_close_20,
    sma_50,
    rsi,
    volatility
):

    volume_score = get_volume_score(volume_ratio)

    breakout_score = get_breakout_score(
        close_price,
        previous_high
    )

    momentum_score = get_momentum_score(
        close_price,
        avg_close_20
    )

    trend_score = get_trend_score(
        close_price,
        sma_50
    )


    rsi_score = get_rsi_score(rsi)

    volatility_score = (
        get_volatility_score(
            volatility
        )
    )


    total_score = min(
        volume_score
        + breakout_score
        + momentum_score
        +trend_score
        +rsi_score
        + volatility_score,
        100
    )

    

    return {
        "volume_score": volume_score,
        "breakout_score": breakout_score,
        "momentum_score": momentum_score,
        "trend_score": trend_score,
        "rsi_score": rsi_score,
        "volatility_score": volatility_score,
        "total_score": total_score
        
    }