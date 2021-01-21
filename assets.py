from enum import Enum
from typing import List, Optional


class TimeFrame(Enum):
    MINUTE = '1Min'
    FIVE_MINUTE = '5Min'
    FIFTEEN_MINUTE = '15Min'
    DAILY = '1D'


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
    def open(self):
        return self._open

    @property
    def high(self):
        return self._high

    @property
    def low(self):
        return self._low

    @property
    def close(self):
        return self._close

    @property
    def volume(self):
        return self._volume

    @property
    def time(self):
        return self._time

    @property
    def is_green(self):
        return self._close > self._open

    @property
    def is_red(self):
        return self._close < self._open


class Chart:
    _symbol: str
    _time_frame: TimeFrame
    _bars: List[Bar]

    def __init__(self, symbol: str, time_frame: TimeFrame, bars: List[Bar]):
        self._symbol = symbol
        self._time_frame = time_frame
        self._bars = bars

    @property
    def symbol(self):
        return self._symbol

    @property
    def time_frame(self):
        return self._time_frame

    @property
    def bars(self):
        return self._bars

    @property
    def last_percent_change(self) -> Optional[float]:
        return (self.bars[-1].close - self.bars[-2].close) / self.bars[-2].close if len(self._bars) >= 2 else None

    def __str__(self):
        change = "N/A" if not self.last_percent_change else f'{self.last_percent_change:.2%}'
        return f'{self.symbol} ({self.time_frame}) Last Change: {change}'


class Asset:
    symbol: str
    exchange: str
    shortable: bool

    def __init__(self, asset):
        self.symbol = asset.symbol
        self.exchange = asset.exchange
        self.shortable = asset.shortable and asset.easy_to_borrow

    def __repr__(self):
        return f'Asset({self.symbol}, {self.exchange})'
