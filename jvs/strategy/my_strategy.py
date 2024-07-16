import pandas as pd
import pandas_ta as ta

class MyStrategy:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def apply_moving_average(self, window: int):
        """应用简单移动平均线到数据

        参数:
            window (int): 移动平均线的窗口大小.

        返回:
            pd.Series: 移动平均线序列.
        """
        return self.data['close'].rolling(window=window).mean()

    def apply_rsi(self, period: int):
        """应用相对强弱指数 (RSI) 到数据

          参数:
              period (int): RSI计算的周期.

          返回:
              pd.Series: RSI序列.
          """
        rsi = ta.rsi(self.data['close'], length=period)
        return rsi
