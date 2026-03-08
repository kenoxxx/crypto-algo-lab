from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

import ccxt
import pandas as pd


ExchangeId = Literal["binance", "bybit", "kucoin"]


@dataclass
class OHLCVRequest:
    exchange_id: ExchangeId = "binance"
    symbol: str = "BTC/USDT"
    timeframe: str = "1h"
    limit: int = 200


def _create_exchange(exchange_id: ExchangeId) -> ccxt.Exchange:
    if not hasattr(ccxt, exchange_id):
        raise ValueError(f"Unsupported exchange_id: {exchange_id}")
    exchange_cls = getattr(ccxt, exchange_id)
    exchange = exchange_cls()
    exchange.load_markets()
    return exchange


def fetch_ohlcv(request: Optional[OHLCVRequest] = None) -> pd.DataFrame:
    """Fetch OHLCV data from a spot exchange using ccxt."""
    req = request or OHLCVRequest()
    exchange = _create_exchange(req.exchange_id)

    raw = exchange.fetch_ohlcv(req.symbol, req.timeframe, limit=req.limit)
    df = pd.DataFrame(
        raw, columns=["timestamp", "open", "high", "low", "close", "volume"]
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    df.set_index("timestamp", inplace=True)
    return df
