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
    'interval': 'daily'
}
response = requests.get(url, params=params)
data = response.json()

# Menyiapkan data untuk grafik
dates = [datetime.fromtimestamp(item[0] / 1000) for item in data['prices']]
prices = [item[1] for item in data['prices']]

# Membuat data dummy untuk Open, High, Low, dan Close
df = pd.DataFrame({
    'Date': dates,
    'Open': prices,
    'High': [price + (price * 0.05) for price in prices],  # Harga tertinggi sedikit lebih tinggi dari harga penutupan
    'Low': [price - (price * 0.05) for price in prices],   # Harga terendah sedikit lebih rendah dari harga penutupan
    'Close': prices
})

df.set_index('Date', inplace=True)

# Membuat grafik candlestick
plt.figure(figsize=(12, 6))
mpf.plot(df, type='candle', style='charles', title='Bitcoin Price Over the Last 1 Year',
         ylabel='Price (USD)', datetime_format='%Y-%m', 
         figratio=(12,6), figscale=1.2)

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