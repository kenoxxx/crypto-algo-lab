import pandas as pd

from crypto_algo_lab.data.loader import OHLCVRequest, fetch_ohlcv
from crypto_algo_lab.strategies.example_ma_cross import MACrossStrategy
from crypto_algo_lab.backtester.engine import run_simple_backtest


def main() -> None:
    # Fetch recent market data (e.g. from Binance)
    request = OHLCVRequest(exchange_id="binance", symbol="BTC/USDT", timeframe="1h", limit=300)
    data = fetch_ohlcv(request)

    strategy = MACrossStrategy()
    signals = strategy.generate_signals(data)
    result = run_simple_backtest(data, signals)

    print(result.tail())
    print("Total return:", result.total_return)


if __name__ == "__main__":
    main()
