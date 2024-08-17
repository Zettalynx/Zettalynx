import requests
import matplotlib.pyplot as plt
import numpy as np

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk pie chart
sizes = np.random.randint(1, 100, size=len(repos))
labels = [repo['name'] for repo in repos]

# Buat pie chart dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=plt.cm.viridis(np.linspace(0, 1, len(repos))))
plt.title('Repository Distribution', fontsize=16)
plt.savefig('pie_chart.svg')
