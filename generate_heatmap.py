import requests
import matplotlib.pyplot as plt
import numpy as np

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk heatmap
days = np.arange(30)
activity = np.random.randint(0, 100, size=(len(repos), len(days)))

# Buat heatmap dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
plt.imshow(activity, cmap='inferno', aspect='auto')
plt.colorbar(label='Activity Level')
plt.title('Contribution Heatmap', fontsize=16)
plt.xlabel('Days', fontsize=14)
plt.ylabel('Repositories', fontsize=14)
plt.xticks(ticks=np.arange(len(days)), labels=days, fontsize=12)
plt.yticks(ticks=np.arange(len(repos)), labels=[repo['name'] for repo in repos], fontsize=12)
plt.tight_layout()
plt.savefig('heatmap.svg')
