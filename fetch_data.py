import ccxt, pandas as pd, time

symbol = 'BTC/USDT'
timeframe = '15m'
limit = 1000
exchange = ccxt.binance()

since = exchange.parse8601('2024-01-01T00:00:00Z')
ohlcv = []
since_timestamp = since
while True:
    candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=since_timestamp, limit=limit)
    if not candles:
        break
    ohlcv.extend(candles)
    since_timestamp = candles[-1][0] + 1
    if len(candles) < limit:
        break

df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.to_csv('btc_15m.csv', index=False)
print(f"Saved {len(df)} candles to btc_15m.csv")
