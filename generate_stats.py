import requests
import matplotlib.pyplot as plt

# Username GitHub
username = "Zettalynx"
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
data = response.json()

# Data yang akan divisualisasikan
labels = ['Public Repos', 'Followers', 'Following', 'Gists']
values = [data['public_repos'], data['followers'], data['following'], data['public_gists']]

# Membuat bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='skyblue')
plt.title(f'{username} GitHub Stats')
plt.savefig('stats.png')
