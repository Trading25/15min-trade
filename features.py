import pandas as pd, ta

df = pd.read_csv('btc_15m.csv', parse_dates=['timestamp'])

df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
df['ema_fast'] = ta.trend.EMAIndicator(df['close'], window=9).ema_indicator()
df['ema_slow'] = ta.trend.EMAIndicator(df['close'], window=21).ema_indicator()
df['macd'] = ta.trend.MACD(df['close']).macd()
df['stoch_rsi'] = ta.momentum.StochRSIIndicator(df['close']).stochrsi()

df.dropna(inplace=True)
df.to_csv('btc_15m_features.csv', index=False)
print("Features saved to btc_15m_features.csv")
