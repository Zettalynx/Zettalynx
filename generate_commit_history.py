import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk commit history
dates = [datetime.now() - timedelta(days=i*7) for i in range(len(repos))]
commits = np.random.randint(10, 50, size=len(repos))

# Buat commit history graph dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
plt.plot(dates, commits, marker='o', color='cyan')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Commits', fontsize=14)
plt.title('Commit History', fontsize=16)
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.DayLocator())
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('commit_history.svg')
