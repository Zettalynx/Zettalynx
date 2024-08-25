import requests
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import pandas as pd

primary_color = '#6e44ff'
secondary_color = '#00ff7f'

def configure_plot(ax, x_label, y_label):
    ax.set_xlabel(x_label, color='white')
    ax.set_ylabel(y_label, color='white')
    ax.tick_params(colors='white')
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5, axis='y')
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.patch.set_facecolor('black')

def fetch_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        'vs_currency': 'usd',
        'days': '365',
        'interval': 'daily'
    }
    response = requests.get(url, params=params)
    return response.json()

data = fetch_bitcoin_data()
prices = data['prices']
volumes = data['total_volumes']

dates = [datetime.fromtimestamp(price[0] / 1000) for price in prices]
price_values = [price[1] for price in prices]
volume_values = [vol[1] for vol in volumes]

df = pd.DataFrame({'date': dates, 'volume': volume_values})
df.set_index('date', inplace=True)
weekly_volume = df['volume'].resample('W').sum()
weekly_dates = weekly_volume.index

current_date = dates[-1]
current_price = price_values[-1]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [3, 1]})
fig.patch.set_facecolor('black')

ax1.plot(dates, price_values, color=primary_color, linewidth=2)
ax1.axvline(current_date, color=secondary_color, linestyle='--', linewidth=1.5)
ax1.axhline(current_price, color=secondary_color, linestyle='--', linewidth=1.5)
ax1.text(current_date, current_price, f' ${current_price:,.2f}', color=secondary_color, 
         fontsize=12, verticalalignment='bottom', horizontalalignment='left')
configure_plot(ax1, "", "Price (USD)")

ax2.bar(weekly_dates, weekly_volume, color=secondary_color, alpha=0.3, width=5, align='center')
configure_plot(ax2, "Date", "Volume (USD)")

plt.savefig('bitcoin.png', bbox_inches='tight', transparent=True)