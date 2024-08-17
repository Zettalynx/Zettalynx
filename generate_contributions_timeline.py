import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk contributions (contoh)
dates = [datetime.now() - timedelta(days=i*10) for i in range(len(repos))]
contributions = np.random.randint(10, 100, size=len(repos))

# Buat timeline graph
plt.plot(dates, contributions, marker='o')
plt.xlabel('Date')
plt.ylabel('Contributions')
plt.title('GitHub Contributions Timeline')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.xticks(rotation=45)
plt.savefig('contributions_timeline.svg')
