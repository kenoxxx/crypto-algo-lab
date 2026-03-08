import pandas as pd


class SimpleBacktestResult(pd.DataFrame):
    @property
    def total_return(self) -> float:
        return float(self["equity"].iloc[-1] - 1.0)


def run_simple_backtest(
    ohlcv: pd.DataFrame,
    signals: pd.Series,
    fee: float = 0.001,
) -> SimpleBacktestResult:
    """Very simple long/flat backtest with starting equity = 1.0."""
    equity = 1.0
    positions = []
    equities = []

    returns = ohlcv["close"].pct_change().fillna(0.0)

    for ret, sig in zip(returns, signals):
        if sig != 0:
            equity *= (1.0 - fee)
        if sig > 0:
            equity *= (1.0 + ret)
        positions.append(sig)
        equities.append(equity)

    df = SimpleBacktestResult({"equity": equities, "position": positions}, index=ohlcv.index)
    return df

