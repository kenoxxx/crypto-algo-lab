from dataclasses import dataclass
from typing import Optional

import pandas as pd


@dataclass
class MACrossConfig:
    fast: int = 10
    slow: int = 20


class MACrossStrategy:
    def __init__(self, config: Optional[MACrossConfig] = None) -> None:
        self.config = config or MACrossConfig()

    def generate_signals(self, ohlcv: pd.DataFrame) -> pd.Series:
        close = ohlcv["close"]
        fast_ma = close.rolling(self.config.fast).mean()
        slow_ma = close.rolling(self.config.slow).mean()

        raw = (fast_ma > slow_ma).astype(int)
        signal = raw.diff().fillna(0)
        return signal
