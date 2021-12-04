import pyupbit
import numpy as np

#ohlcv (open, high, low, close, volumn)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-ETH", count=30)
df['range'] = (df['high'] - df['low']) * 0.36
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.001
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")