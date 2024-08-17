import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
user = response.json()

# Simulasi data untuk badge
followers = user.get('followers', 0)

# Buat badge dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(10, 2))
plt.text(0.5, 0.5, f'Followers: {followers}', color='lightgreen', fontsize=20, ha='center', va='center')
plt.axis('off')
plt.title('GitHub Profile Badge', fontsize=16)
plt.savefig('profile_badge.svg')
