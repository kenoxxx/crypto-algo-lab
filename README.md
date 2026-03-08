<p align="center">
  <img src="https://raw.githubusercontent.com/kenoxxx/crypto-algo-lab/main/.github/assets/baner.png" alt="crypto-algo-lab" width="80%">
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

`crypto-algo-lab` is a Python playground for crypto traders and quants: a small, clean framework to go from “idea” → “backtest” → “simple live bot”.[page:5]  
You get ready-made bricks for OHLCV data loading via `ccxt`, a backtest engine and a clear place for your strategy code, so you spend time on edge, not on wiring.[page:1][page:3][page:5]  

Use it if you want:

- ⚙️ To fetch exchange candles in one line and get a tidy pandas DataFrame.
- 📈 To run repeatable backtests across symbols and timeframes.
- 🚀 To have a minimal structure that can grow into real bots.

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
The data loader uses ccxt and returns a clean pandas DataFrame with timestamps and open, high, low, close, volume, ready for indicators and research.[page:1][page:3]

📚 Learn more
📈 Data loader: https://github.com/kenoxxx/crypto-algo-lab/wiki/Data-loader[page:3]

♟ Strategies: https://github.com/kenoxxx/crypto-algo-lab/wiki/Strategies[page:3]

✅ CI & tests: https://github.com/kenoxxx/crypto-algo-lab/wiki/CI-&-Tests[page:4]

🤝 Contributing & 📜 License
Contributions (ideas, issues, PRs) are welcome.[page:5]
MIT license — see LICENSE.txt.[page:5]