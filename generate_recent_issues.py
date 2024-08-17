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

    # Pastikan issues adalah list
    if isinstance(issues, list):
        titles = [issue['title'] for issue in issues]
        statuses = [1 for _ in issues]  # Simulasi status

        # Buat bar chart
        plt.bar(titles, statuses)
        plt.xlabel('Issues')
        plt.ylabel('Status')
        plt.title('Recent Issues')
        plt.xticks(rotation=90)
        plt.savefig('recent_issues.svg')
    else:
        print("Error: Unexpected data format.")
else:
    print(f"Error: Failed to fetch data. Status code: {response.status_code}")
