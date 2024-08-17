import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Ambil jumlah stars dan forks (contoh simulasi)
repo_names = [repo['name'] for repo in repos]
stars = [repo['stargazers_count'] for repo in repos]
forks = [repo['forks_count'] for repo in repos]

# Buat bar chart
plt.bar(repo_names, stars, label='Stars')
plt.bar(repo_names, forks, bottom=stars, label='Forks')
plt.xlabel('Repositories')
plt.ylabel('Count')
plt.title('Repository Stars and Forks')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('stars_forks.svg')
