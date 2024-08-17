import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk contributions (contoh)
dates = [datetime.now() - timedelta(days=i*10) for i in range(len(repos))]
contributions = np.random.randint(10, 100, size=len(repos))

# Buat timeline graph dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
plt.plot(dates, contributions, marker='o', color='lime')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Contributions', fontsize=14)
plt.title('GitHub Contributions Timeline', fontsize=16)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('contributions_timeline.svg')
