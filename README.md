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

## 🧱 Architecture at a glance

```mermaid
flowchart LR
    A[Exchange APIs<br/>Binance, Bybit, OKX...] --> B[Data Loader<br/>(ccxt OHLCV)]
    B --> C[Backtest Engine]
    C --> D[Strategy Logic]
    D --> E[Metrics & Reports]
    C --> F[Live Execution<br/>(future)]
Data loader – unified OHLCV fetcher built on top of ccxt with a consistent interface.[page:1][page:3]

Backtest engine – iterates over candles and simulates orders, fills, PnL, and equity curve.[page:3]

Strategies – small, focused components with clear entry/exit rules that can be reused in backtests and live.[page:3]

See the Wiki for more:

Data loader[page:3]

Strategies[page:3]

CI & Tests[page:4]

🚀 Quick start
Clone the repo and install in editable mode:

bash
git clone https://github.com/kenoxxx/crypto-algo-lab.git
cd crypto-algo-lab

# (optional) create and activate virtualenv
# python -m venv .venv
# source .venv/bin/activate  # Linux / macOS
# .venv\Scripts\activate     # Windows

pip install -e .
pytest  # run tests to make sure everything passes
Run an example strategy:

bash
python examples/basic_strategy.py
📊 Example: from data to backtest
The data loader wraps ccxt and returns a pandas DataFrame with timestamp index and open, high, low, close, volume columns.[page:1][page:3]

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
Swap symbol/timeframe to explore different markets.

Replace ExampleStrategy with your own logic.

Reuse the same strategy class later in a live trading runner.

🧬 Data loader (ccxt-based)
Key points:

Uses ccxt under the hood to fetch OHLCV candles from supported exchanges like Binance/Bybit/OKX (depending on what you wire up).[page:1][page:3]

You configure exchange_id, symbol, timeframe, start, end and get a clean DataFrame for research or backtesting.[page:1][page:3]

Basic usage:

python
from crypto_algo_lab.data.loader import fetch_ohlcv

df = fetch_ohlcv(
    exchange_id="binance",
    symbol="ETH/USDT",
    timeframe="15m",
    start="2024-03-01",
    end="2024-03-07",
)
More details and tips (including API errors, HTTP 451, mocking in tests) are in the wiki:
👉 Data loader[page:3]

♟ Strategies
Strategies in crypto-algo-lab are designed to be:

Small and composable units of logic.

Easy to backtest across many markets and timeframes.

Reusable for both research notebooks and live trading code.[page:3]

Typical structure:

Init: parameters (symbol, timeframe, risk per trade).

on_bar/on_tick: read the latest data point and decide open/hold/close.

Helpers: entry/exit conditions, risk and position sizing.

See the dedicated Wiki page with patterns and examples:
👉 Strategies[page:3]

✅ CI & tests
The project ships with a GitHub Actions workflow that automatically runs the test suite on every push and pull request.[page:5]
Tests cover data loading, strategy execution, and utilities to keep the framework stable as it evolves.[page:1][page:4][page:5]

Highlights:

Workflow file under .github/workflows/*.yml sets up Python, installs deps, runs pytest.[page:4][page:5]

Where possible, tests avoid hard dependencies on real exchanges (using mocks/fixtures).[page:4]

Live API calls (if any) are kept to a minimal set of smoke tests, and can be skipped when HTTP errors like 451 occur.[page:1][page:4]

More: 👉 CI & Tests[page:4]

🗺️ Roadmap
Planned directions:

More example strategies (trend-following, mean-reversion, volatility breakout).

Additional exchanges and instruments wired via ccxt.

Live trading runner with risk management, logging, and monitoring.

Performance dashboards and automated report generation.

If you have ideas or requests, open an issue or PR.

🤝 Contributing
Contributions are welcome — ideas, issues, and pull requests.[page:5]

Read the Code of Conduct:
https://github.com/kenoxxx/crypto-algo-lab/blob/main/CODE_OF_CONDUCT.md[page:5]

Check CONTRIBUTING.md for guidelines:
https://github.com/kenoxxx/crypto-algo-lab/blob/main/CONTRIBUTING.md[page:5]

If you build a cool strategy or exchange integration, consider sharing it back!

📄 License
crypto-algo-lab is released under the MIT License — see LICENSE.txt.[page:5]
You can use it in both personal and commercial projects.[page:5