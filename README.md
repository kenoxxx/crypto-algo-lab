<p align="center">
  <img src=".github/assets/baner.png" alt="crypto-algo-lab" width="80%">
</p>

<p align="center">
  <b>Turn crypto trading ideas into real backtests and bots — without drowning in boilerplate.</b>
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

`crypto-algo-lab` is a Python framework for traders and quants who want to turn crypto ideas into numbers fast.  
It gives you ready-made pieces for OHLCV data loading via `ccxt`, a backtest engine, and a clean place for your strategy logic.  

You can:

- ⚙️ Fetch historical candles from multiple exchanges in one line.
- 📈 Run repeatable backtests across symbols and timeframes.
- 🚀 Use the same structure later as a base for simple live bots.

---

## ⚡ Quick start

```bash
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
The data loader uses ccxt and returns a tidy pandas DataFrame with timestamps and open, high, low, close, volume, ready for indicators and research.

📚 Learn more
📈 Data loader: https://github.com/kenoxxx/crypto-algo-lab/wiki/Data-loader

♟ Strategies: https://github.com/kenoxxx/crypto-algo-lab/wiki/Strategies

✅ CI & tests: https://github.com/kenoxxx/crypto-algo-lab/wiki/CI-&-Tests

🤝 Contributing & 📜 License
Contributions (ideas, issues, PRs) are welcome.
MIT license — see LICENSE.txt.