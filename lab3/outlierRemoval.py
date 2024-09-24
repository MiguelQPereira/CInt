import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# Load DataFrame
df = pd.read_csv('EURUSD_Daily_Ask_2018.12.31_2019.10.05v2.csv', delimiter=';')

df['Volume'] = df['Volume'].str.replace(',', '.')
df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')


df['Time (UTC)'] = pd.to_datetime(df['Time (UTC)'], format='%Y.%m.%d %H:%M:%S')

df['rollingAvg'] = df['Volume'].rolling(window=50).mean()

plt.figure(figsize=(10,6))
plt.subplot(211)
plt.plot(df['Time (UTC)'], df['Open'], label='Open', marker='o')
plt.plot(df['Time (UTC)'], df['High'], label='High', marker='o')
plt.plot(df['Time (UTC)'], df['Low'], label='Low', marker='o')
plt.plot(df['Time (UTC)'], df['Close'], label='Close', marker='o')

plt.subplot(212)
plt.plot(df['Time (UTC)'], df['Volume'], label='Volume', marker='o')
plt.plot(df['Time (UTC)'], df['rollingAvg'], label='Rolling Average', linestyle='--')

plt.title('Volume Over Time')
plt.xlabel('Time')
plt.ylabel('Volume')
plt.legend()

plt.show()