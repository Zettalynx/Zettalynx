import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Mengambil data harga Bitcoin selama 1 tahun terakhir
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    'vs_currency': 'usd',
    'days': '365',  # Periode waktu (1 tahun terakhir)
    'interval': 'daily'
}
response = requests.get(url, params=params)
data = response.json()

# Menyiapkan data untuk grafik
dates = [datetime.fromtimestamp(item[0] / 1000) for item in data['prices']]
prices = [item[1] for item in data['prices']]

# Membuat grafik garis dengan background transparan
plt.figure(figsize=(12, 8))
plt.plot(dates, prices, label='Bitcoin Price (USD)', color='orange')

# Menambahkan judul dan label dengan teks putih
plt.title("Bitcoin Price Over the Last 1 Year", color='white')
plt.xlabel("Date", color='white')
plt.ylabel("Price (USD)", color='white')
plt.xticks(rotation=45, color='white')
plt.yticks(color='white')
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Mengatur background transparan
plt.gca().patch.set_facecolor('black')  # Background area plot
plt.gcf().patch.set_facecolor('black')  # Background seluruh figure

# Menyimpan grafik dengan latar belakang transparan
plt.savefig('bitcoin_chart.png', bbox_inches='tight', transparent=True)
