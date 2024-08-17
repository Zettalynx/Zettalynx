import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Ambil jumlah commits (contoh simulasi)
repo_names = [repo['name'] for repo in repos]
commits = np.random.randint(100, 1000, size=len(repos))

# Buat bar chart
plt.bar(repo_names, commits)
plt.xlabel('Repositories')
plt.ylabel('Commits')
plt.title('Dynamic Bar Chart')
plt.xticks(rotation=90)
plt.savefig('bar_chart.svg')
