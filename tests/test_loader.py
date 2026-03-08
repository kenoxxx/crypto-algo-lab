from crypto_algo_lab.data.loader import OHLCVRequest, fetch_ohlcv


def test_fetch_ohlcv_runs_smoke():
    req = OHLCVRequest(limit=10)
    df = fetch_ohlcv(req)
    # smoke test: we at least get a DataFrame with expected columns
    assert set(["open", "high", "low", "close", "volume"]).issubset(df.columns)

