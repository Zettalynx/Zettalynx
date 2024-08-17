import requests
import matplotlib.pyplot as plt

# Mengatur tema dark
plt.style.use('dark_background')

# Username GitHub
username = "Zettalynx"
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
data = response.json()

# Data yang akan divisualisasikan
labels = ['Public Repos', 'Followers', 'Following', 'Gists']
values = [data['public_repos'], data['followers'], data['following'], data['public_gists']]

# Membuat bar chart dengan tema dark
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='cyan')
plt.title(f'{username} GitHub Stats', color='white')
plt.xlabel('Categories', color='white')
plt.ylabel('Count', color='white')
plt.xticks(color='white')
plt.yticks(color='white')
plt.savefig('stats.png', transparent=True)
