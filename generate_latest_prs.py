import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
repo_name = "Zettalynx"  # Ganti dengan nama repository kamu
url = f"https://api.github.com/repos/{username}/{repo_name}/pulls"
response = requests.get(url)

# Cek apakah permintaan berhasil
if response.status_code == 200:
    pulls = response.json()
    if isinstance(pulls, list):
        titles = [pr['title'] for pr in pulls]
        statuses = [1 for _ in pulls]

        # Buat bar chart dengan tema gelap
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 8))
        plt.bar(titles, statuses, color='magenta')
        plt.xlabel('Pull Requests', fontsize=14)
        plt.ylabel('Status', fontsize=14)
        plt.title('Latest Pull Requests', fontsize=16)
        plt.xticks(rotation=90, fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.savefig('latest_prs.svg')
    else:
        print("Error: Unexpected data format.")
else:
    print(f"Error: Failed to fetch data. Status code: {response.status_code}")
