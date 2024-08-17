import requests
import matplotlib.pyplot as plt
import numpy as np

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk commit history (contoh)
repo_names = [repo['name'] for repo in repos]
commits = np.random.randint(100, 1000, size=len(repos))

# Buat commit history graph
plt.plot(repo_names, commits, marker='o')
plt.xlabel('Repositories')
plt.ylabel('Commits')
plt.title('Commit History Graph')
plt.xticks(rotation=90)
plt.savefig('commit_history.svg')
