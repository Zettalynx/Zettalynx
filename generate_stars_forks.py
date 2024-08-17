import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Ambil data stars dan forks
stars = [repo['stargazers_count'] for repo in repos]
forks = [repo['forks_count'] for repo in repos]
repo_names = [repo['name'] for repo in repos]

# Buat bar chart untuk stars dan forks dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
plt.bar(repo_names, stars, color='blue', label='Stars')
plt.bar(repo_names, forks, color='red', alpha=0.5, label='Forks')
plt.xlabel('Repositories', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.title('Stars and Forks', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig('stars_forks.svg')
