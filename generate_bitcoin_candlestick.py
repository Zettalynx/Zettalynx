import requests
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import datetime
import pandas as pd

# Mengambil data harga Bitcoin selama 1 tahun terakhir
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    'vs_currency': 'usd',
    'days': '365',  # Periode waktu 1 tahun
    'interval': 'daily'  # Mengubah interval menjadi bulanan
}
response = requests.get(url, params=params)
data = response.json()

# Mengambil harga dan tanggal
timestamps = [item[0] / 1000 for item in data['prices']]
prices = [item[1] for item in data['prices']]

# Menggunakan harga penutupan untuk semua harga
df = pd.DataFrame({
    'Date': pd.to_datetime(timestamps, unit='s'),
    'Open': prices,
    'High': prices,
    'Low': prices,
    'Close': prices
})

df.set_index('Date', inplace=True)
df.index.name = 'Date'

# Menyiapkan grafik candlestick
plt.figure(figsize=(12, 6))
mpf.plot(df, type='candle', style='charles', title='Bitcoin Price Over the Last 1 Year',
         ylabel='Price (USD)', datetime_format='%Y-%m',
         figratio=(12,6), figscale=1.2, title_kwargs={'color': 'white'},
         ylabel_kwargs={'color': 'white'}, volume=False)

# Mengatur tema dark background
plt.gca().set_facecolor('black')
plt.gcf().patch.set_facecolor('black')
plt.title('Bitcoin Price Over the Last 1 Year', color='white')
plt.xlabel('Date', color='white')
plt.ylabel('Price (USD)', color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.grid(True, color='white', linestyle='--', linewidth=0.5)

# Simpan gambar grafik dengan background transparan
plt.savefig('bitcoin_candlestick_chart.png', bbox_inches='tight', transparent=True)
