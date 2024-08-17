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

    # Pastikan pulls adalah list
    if isinstance(pulls, list):
        titles = [pr['title'] for pr in pulls]
        statuses = [1 for _ in pulls]  # Simulasi status

        # Buat bar chart
        plt.bar(titles, statuses)
        plt.xlabel('Pull Requests')
        plt.ylabel('Status')
        plt.title('Latest Pull Requests')
        plt.xticks(rotation=90)
        plt.savefig('latest_prs.svg')
    else:
        print("Error: Unexpected data format.")
else:
    print(f"Error: Failed to fetch data. Status code: {response.status_code}")
