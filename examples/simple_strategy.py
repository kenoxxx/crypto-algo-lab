import pandas as pd

from crypto_algo_lab.strategies.example_ma_cross import MACrossStrategy
from crypto_algo_lab.backtester.engine import run_simple_backtest


def main() -> None:
    data = pd.DataFrame(
        {"close": [100, 101, 102, 103, 102, 101, 100, 99, 100, 101]}
    )
    data.index = pd.RangeIndex(len(data))

    strategy = MACrossStrategy()
    signals = strategy.generate_signals(data)
    result = run_simple_backtest(data, signals)

    print(result.tail())
    print("Total return:", result.total_return)


if __name__ == "__main__":
    main()
