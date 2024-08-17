import requests
import matplotlib.pyplot as plt
import numpy as np

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/events"
response = requests.get(url)
events = response.json()

# Simulasi data untuk heatmap (contoh)
days = np.random.randint(0, 100, size=(12, 7))

# Buat heatmap
plt.imshow(days, cmap='Greens', interpolation='nearest')
plt.title('Contribution Calendar')
plt.colorbar()
plt.savefig('heatmap.svg')
