import requests
import matplotlib.pyplot as plt

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/issues"
response = requests.get(url)
issues = response.json()

# Simulasi data untuk issues (contoh)
titles = [issue['title'] for issue in issues]
counts = [1 for _ in issues]  # Simulasi counts

# Buat bar chart
plt.bar(titles, counts)
plt.xlabel('Issues')
plt.ylabel('Count')
plt.title('Recent Issues Opened')
plt.xticks(rotation=90)
plt.savefig('recent_issues.svg')
