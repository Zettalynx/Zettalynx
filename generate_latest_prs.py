import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/repos/{username}/<repository>/pulls"
response = requests.get(url)
pulls = response.json()

# Simulasi data untuk pull requests (contoh)
titles = [pr['title'] for pr in pulls]
statuses = [1 for _ in pulls]  # Simulasi status

# Buat bar chart
plt.bar(titles, statuses)
plt.xlabel('Pull Requests')
plt.ylabel('Status')
plt.title('Latest Pull Requests')
plt.xticks(rotation=90)
plt.savefig('latest_prs.svg')
