import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk pie chart (contoh)
labels = [repo['name'] for repo in repos]
sizes = [repo['size'] for repo in repos]

# Buat pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Activity Pie Chart')
plt.savefig('pie_chart.svg')
