import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data bahasa pemrograman (contoh)
languages = ['Python', 'JavaScript', 'HTML', 'CSS']
sizes = [50, 30, 10, 10]

# Buat pie chart
plt.pie(sizes, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Top Languages Used')
plt.savefig('top_languages.svg')
