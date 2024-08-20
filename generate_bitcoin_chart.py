import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Mengambil data harga Bitcoin selama 30 hari terakhir
url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    'vs_currency': 'usd',
    'days': '30',
    'interval': 'daily'
}
response = requests.get(url, params=params)
data = response.json()

# Menyiapkan data untuk grafik
dates = [datetime.fromtimestamp(item[0] / 1000) for item in data['prices']]
prices = [item[1] for item in data['prices']]

# Membuat grafik garis
plt.figure(figsize=(10, 6))
plt.plot(dates, prices, label='Bitcoin Price (USD)', color='orange')

# Menambahkan judul dan label
plt.title("Bitcoin Price Over the Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()

# Simpan gambar grafik
plt.savefig('bitcoin_chart.png')
