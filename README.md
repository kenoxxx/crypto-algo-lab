<p align="center">
  <img src="https://raw.githubusercontent.com/kenoxxx/crypto-algo-lab/main/.github/assets/banner.png" alt="crypto-algo-lab" width="80%">
</p>

<p align="center">
  <b>Open-source framework for researching, backtesting, and running algorithmic crypto trading strategies.</b>
</p>

<p align="center">
  <a href="https://github.com/kenoxxx/crypto-algo-lab/actions">
    <img src="https://github.com/kenoxxx/crypto-algo-lab/actions/workflows/tests.yml/badge.svg" alt="CI status">
  </a>
  <a href="https://github.com/kenoxxx/crypto-algo-lab/blob/main/LICENSE.txt">
    <img src="https://img.shields.io/github/license/kenoxxx/crypto-algo-lab.svg" alt="License">
  </a>
  <a href="https://github.com/kenoxxx/crypto-algo-lab/stargazers">
    <img src="https://img.shields.io/github/stars/kenoxxx/crypto-algo-lab.svg?style=social" alt="GitHub stars">
  </a>
</p>

---

## ✨ What is crypto-algo-lab?

`crypto-algo-lab` is a Python framework that helps you go from idea → backtest → live crypto bot with minimal boilerplate.[page:5]  
It gives you clean building blocks for data loading, strategy logic, and execution so you can focus on the edge, not on plumbing.[page:5]  

Use it if you want:

- A simple way to fetch OHLCV from multiple exchanges via `ccxt`.
- A reusable backtesting loop for different strategies, symbols, and timeframes.
- A project structure that can grow into production-ready bots.

---

## 🧱 Architecture

```mermaid
flowchart LR
    A[Exchange APIs (Binance, Bybit, OKX...)] --> B[Data Loader (ccxt OHLCV)]
    B --> C[Backtest Engine]
    C --> D[Strategy Logic]
    D --> E[Metrics & Reports]
    C --> F[Live Execution (future)]
Data loader – unified OHLCV fetcher built on top of ccxt with a consistent interface.[page:1][page:3]

Backtest engine – iterates over candles and simulates orders, fills, PnL, and equity curve.[page:3]

Strategies – small components with clear entry/exit rules, reusable in backtests and live trading.[page:3]

More in the Wiki: Data loader, Strategies, CI & Tests.[page:3][page:4]

🚀 Quick start
bash
git clone https://github.com/kenoxxx/crypto-algo-lab.git
cd crypto-algo-lab

pip install -e .
pytest
Run an example strategy:

bash
python examples/basic_strategy.py
📊 From data to backtest
python
from crypto_algo_lab.data.loader import fetch_ohlcv
from crypto_algo_lab.strategy.example import ExampleStrategy
from crypto_algo_lab.backtest.engine import BacktestEngine

df = fetch_ohlcv(
    exchange_id="binance",
    symbol="BTC/USDT",
    timeframe="1h",
    start="2024-01-01",
    end="2024-02-01",
)

strategy = ExampleStrategy(symbol="BTC/USDT", timeframe="1h")
engine = BacktestEngine(strategy=strategy, data=df)

results = engine.run()
print(results.summary())
The data loader wraps ccxt and returns a pandas DataFrame with timestamp index and open, high, low, close, volume columns.[page:1][page:3]

✅ CI & tests
GitHub Actions runs the test suite on every push and pull request.[page:5]
Tests cover data loading, strategy execution, and utilities, with preference for mocks/fixtures instead of real exchange calls.[page:1][page:4][page:5]

Details: CI & Tests.[page:4]

🤝 Contributing & License
Contributions are welcome — ideas, issues, and pull requests.[page:5]
The project is released under the MIT License — see LICENSE.txt.[page:5