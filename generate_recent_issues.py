import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
repo_name = "Zettalynx"  # Ganti dengan nama repository kamu
url = f"https://api.github.com/repos/{username}/{repo_name}/issues"
response = requests.get(url)

# Cek apakah permintaan berhasil
if response.status_code == 200:
    issues = response.json()
    if isinstance(issues, list):
        titles = [issue['title'] for issue in issues]
        statuses = [1 for _ in issues]

        # Buat bar chart dengan tema gelap
        plt.style.use('dark_background')
        plt.figure(figsize=(12, 8))
        plt.bar(titles, statuses, color='orange')
        plt.xlabel('Issues', fontsize=14)
        plt.ylabel('Status', fontsize=14)
        plt.title('Recent Issues', fontsize=16)
        plt.xticks(rotation=90, fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()
        plt.savefig('recent_issues.svg')
    else:
        print("Error: Unexpected data format.")
else:
    print(f"Error: Failed to fetch data. Status code: {response.status_code}")
