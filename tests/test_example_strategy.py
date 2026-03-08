import pandas as pd

from crypto_algo_lab.strategies.example_ma_cross import MACrossStrategy


def test_generate_signals_runs():
    data = pd.DataFrame({"close": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    strat = MACrossStrategy()
    signals = strat.generate_signals(data)
    assert len(signals) == len(data)
