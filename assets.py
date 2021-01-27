from enum import Enum
from typing import List, Optional


class TimeFrame(Enum):
    MINUTE = '1Min'
    FIVE_MINUTE = '5Min'
    FIFTEEN_MINUTE = '15Min'
    DAILY = '1D'


class Asset:
    _symbol: str
    _exchange: str
    _shortable: bool

    def __init__(self, asset):
        self._symbol = asset.symbol
        self._exchange = asset.exchange
        self._shortable = asset.shortable and asset.easy_to_borrow

    def __repr__(self):
        return f'Asset({self._symbol}, {self._exchange})'

    @property
    def symbol(self):
        return self._symbol

    @property
    def exchange(self):
        return self._exchange

    @property
    def shortable(self):
        return self._shortable


class Bar:
    _open: float
    _high: float
    _low: float
    _close: float
    _volume: float
    _time: int

    def __init__(self, bar):
        self._open = bar.o
        self._high = bar.h
        self._low = bar.l
        self._close = bar.c
        self._volume = bar.v
        self._time = bar.t

    @property
    def open(self) -> float:
        return self._open

    @property
    def high(self) -> float:
        return self._high

    @property
    def low(self) -> float:
        return self._low

    @property
    def close(self) -> float:
        return self._close

    @property
    def volume(self) -> float:
        return self._volume

    @property
    def time(self) -> int:
        return self._time

    @property
    def is_green(self) -> bool:
        return self._close > self._open

    @property
    def is_red(self) -> bool:
        return self._close < self._open


class Chart:
    _asset: Asset
    _time_frame: TimeFrame
    _bars: List[Bar]

    def __init__(self, asset: Asset, time_frame: TimeFrame, bars: List[Bar]):
        self._asset = asset
        self._time_frame = time_frame
        self._bars = bars

    @property
    def asset(self) -> Asset:
        return self._asset

    @property
    def time_frame(self) -> TimeFrame:
        return self._time_frame

    @property
    def bars(self) -> List[Bar]:
        return self._bars

    @property
    def last_percent_change(self) -> Optional[float]:
        return (self.bars[-1].close - self.bars[-2].close) / self.bars[-2].close if len(self._bars) >= 2 else None

    def __str__(self):
        change = "N/A" if not self.last_percent_change else f'{self.last_percent_change:.2%}'
        return f'{self.asset.symbol} ({self.time_frame.value}) {change}'
