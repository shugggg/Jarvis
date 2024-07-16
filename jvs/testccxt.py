import ccxt
import pandas as pd


# exchange = ccxt.okx ({
#     'timeout': 30000,
# })

# import time
# from my_project.data.data_loader import DataLoader
# from my_project.strategy.my_strategy import MyStrategy
# from my_project.trader.trader import Trader

exchange = ccxt.binance({
    'timeout':15000,
    'enableRateLimit':True,
    'proxies': {'https': "http://127.0.0.1:7890", 'http': "http://127.0.0.1:7890"}
})

exchange.load_markets()
symbol = 'BTC/USDT'


print(exchange.fetch_ohlcv("BTC/USDT", timeframe='1m'))



# todo 1. 行情数据
# todo 1. 收益概率
# todo 1. 日志信息
