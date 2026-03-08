import pandas as pd

from crypto_algo_lab.backtester.engine import run_simple_backtest


def test_run_simple_backtest_runs():
    data = pd.DataFrame({"close": [100, 101, 102, 103, 102, 101, 100]})
    data.index = pd.RangeIndex(len(data))
    signals = pd.Series([0, 1, 1, 1, 0, 0, 0], index=data.index)

    result = run_simple_backtest(data, signals)

    assert "equity" in result.columns
    assert len(result) == len(data)
