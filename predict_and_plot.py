import pandas as pd, joblib, matplotlib.pyplot as plt

df = pd.read_csv('btc_15m_features.csv', parse_dates=['timestamp'])
model = joblib.load('model.pkl')

X = df[['rsi', 'ema_fast', 'ema_slow', 'macd', 'stoch_rsi']]
preds = model.predict(X)
probs = model.predict_proba(X)[:, 1]

plt.figure(figsize=(14, 6))
plt.plot(df['timestamp'], df['close'], label='Close Price', color='blue')

for i in range(len(df)):
    color = 'g' if preds[i] == 1 else 'r'
    plt.arrow(df['timestamp'][i], df['close'][i], 0, (df['close'].max() - df['close'].min())*0.02*(1 if preds[i] else -1),
              color=color, head_width=0.0005)

plt.title('BTC/USDT Next Candle Prediction')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.savefig('prediction_plot.png')
print("Prediction plot saved to prediction_plot.png")
