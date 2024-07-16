import json
import os
import time
from jvs.data.data_loader import DataLoader
from jvs.strategy.my_strategy import MyStrategy
from jvs.trader.trader import Trader


def load_config(exchange_name: str):
    config_path = os.path.join('config', 'config.json')
    with open(config_path) as config_file:
        all_configs = json.load(config_file)

    if exchange_name not in all_configs:
        raise ValueError(f"配置文件中未找到交易所: {exchange_name}")

    return all_configs[exchange_name]


def main():
    exchange_name = 'binance'  # 根据需要修改
    config = load_config(exchange_name)

    # 初始化数据加载器并获取数据
    data_loader = DataLoader(exchange_name, config)
    since = int(time.time() - 30 * 24 * 60 * 60) * 1000  # 30天前的时间戳（毫秒）
    df = data_loader.get_klines('BTC/USDT', '1h', since)

    # 应用策略
    strategy = MyStrategy(df)
    df['moving_average'] = strategy.apply_moving_average(20)
    df['rsi'] = strategy.apply_rsi(14)
    print(df.head())

    # 示例: 使用RSI确定交易信号
    latest_rsi = df['rsi'].iloc[-1]
    trader = Trader(exchange_name, config)

    if latest_rsi < 30:
        # RSI < 30 表示超卖，买入信号
        trader.place_order('BTC/USDT', 0.001, 'buy')
    elif latest_rsi > 70:
        # RSI > 70 表示超买，卖出信号
        trader.place_order('BTC/USDT', 0.001, 'sell')


if __name__ == "__main__":
    main()
