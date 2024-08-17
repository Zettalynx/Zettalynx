import requests
import matplotlib.pyplot as plt
import numpy as np

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Ambil jumlah commits (contoh simulasi)
repo_names = [repo['name'] for repo in repos]
commits = np.random.randint(100, 1000, size=len(repos))

# Buat bar chart dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
plt.bar(repo_names, commits, color='cyan')
plt.xlabel('Repositories', fontsize=14)
plt.ylabel('Commits', fontsize=14)
plt.title('Dynamic Bar Chart', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('bar_chart.svg')
