import ccxt
import requests
import numpy as np
import time

def fetch_sol_price():
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('SOL/USDT')
    return ticker['last']

def calculate_rsi(prices, period=14):
    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed >= 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down
    rsi = np.zeros_like(prices)
    rsi[:period] = 100. - 100. / (1. + rs)

    for i in range(period, len(prices)):
        delta = deltas[i - 1]
        up_val = max(delta, 0)
        down_val = -min(delta, 0)
        up = (up * (period - 1) + up_val) / period
        down = (down * (period - 1) + down_val) / period
        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)

    return rsi

def fetch_candles():
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': 'SOLUSDT',
        'interval': '4h',
        'limit': 100
    }
    response = requests.get(url, params=params)
    data = response.json()
    closing_prices = [float(candle[4]) for candle in data]  
    return closing_prices

def main():
    while True:
        try:
            sol_price = fetch_sol_price()
            print(f"Current SOL Price: ${sol_price:.2f}")

            prices = fetch_candles()
            rsi_values = calculate_rsi(prices)
            current_rsi = rsi_values[-1]
            print(f"RSI (4-hour chart): {current_rsi:.2f}")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(1800)  

if __name__ == "__main__":
    main()
