import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

# Untuk grafik candlestick, kita butuh harga pembukaan, penutupan, tertinggi, dan terendah
# Menggunakan harga penutupan sebagai harga pembukaan dan penutupan, dan rentang harga sebagai tertinggi dan terendah
df = pd.DataFrame({
    'Date': dates,
    'Open': prices,
    'High': prices,
    'Low': prices,
    'Close': prices
})

df.set_index('Date', inplace=True)
df.index.name = 'Date'

# Mengatur format tanggal pada x-axis
plt.figure(figsize=(12, 6))
mpf.plot(df, type='candle', style='charles', title='Bitcoin Price Over the Last 1 Year', 
         ylabel='Price (USD)', datetime_format='%Y-%m', 
         figratio=(12,6), figscale=1.2, style='dark_background', 
         title_kwargs={'color': 'white'}, ylabel_kwargs={'color': 'white'})

# Simpan gambar grafik dengan background transparan
plt.savefig('bitcoin_candlestick_chart.png', bbox_inches='tight', transparent=True)
