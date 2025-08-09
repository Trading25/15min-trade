import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('btc_15m_features.csv', parse_dates=['timestamp'])

df['target'] = (df['close'].shift(-1) > df['close']).astype(int)

X = df[['rsi', 'ema_fast', 'ema_slow', 'macd', 'stoch_rsi']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'model.pkl')
print("Model trained and saved to model.pkl")
