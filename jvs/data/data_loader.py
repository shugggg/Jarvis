

# data_loader.py（数据加载器）
# 作用：从币安API获取市场数据。
# 主要功能：通过API调用获取历史K线数据，并将其整理为Pandas DataFrame格式，方便后续的策略分析和回测。
# 适用场景：需要获取特定交易对的历史数据进行分析和策略测试时使用。

import ccxt
import pandas as pd


class DataLoader:
    def __init__(self, exchange_name: str, config: dict):
        exchange_class = getattr(ccxt, exchange_name)
        self.client = exchange_class({
            'apiKey': config['api_key'],
            'secret': config['api_secret'],
            'timeout': 15000,
            'enableRateLimit': True,
            'proxies': config['proxies']
        })

    def get_klines(self, symbol: str, timeframe: str, since: int) -> pd.DataFrame:
        """从交易所获取历史K线数据

        参数:
            symbol (str): 获取数据的交易对.
            timeframe (str): K线的时间间隔.
            since (int): K线数据的起始时间（毫秒）.

        返回:
            pd.DataFrame: 包含K线数据的DataFrame.
        """
        ohlcv = self.client.fetch_ohlcv(symbol, timeframe, since)
        df = pd.DataFrame(ohlcv, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume'
        ])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
