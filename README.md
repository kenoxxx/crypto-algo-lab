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
