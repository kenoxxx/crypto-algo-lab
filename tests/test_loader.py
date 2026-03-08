import pandas as pd

from crypto_algo_lab.data.loader import OHLCVRequest


def test_ohlcv_request_defaults():
    req = OHLCVRequest()
    assert req.exchange_id == "binance"
    assert req.symbol == "BTC/USDT"
    assert req.timeframe == "1h"
    assert req.limit == 200
