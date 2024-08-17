import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()

# Simulasi data untuk bahasa
languages = {}
for repo in repos:
    lang_url = repo['languages_url']
    lang_response = requests.get(lang_url)
    lang_data = lang_response.json()
    for lang, bytes in lang_data.items():
        languages[lang] = languages.get(lang, 0) + bytes

# Buat bar chart untuk bahasa dengan tema gelap
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
plt.bar(languages.keys(), languages.values(), color='purple')
plt.xlabel('Languages', fontsize=14)
plt.ylabel('Bytes', fontsize=14)
plt.title('Top Languages Used', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('top_languages.svg')
