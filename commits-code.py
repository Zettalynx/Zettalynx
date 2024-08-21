import requests
import matplotlib.pyplot as plt

primary_color = '#6e44ff'
secondary_color = '#00ff7f'

def configure_plot(title, x_label, y_label):
    plt.title(title, color='white')
    plt.xlabel(x_label, color='white')
    plt.ylabel(y_label, color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
    plt.gca().patch.set_facecolor('black')
    plt.gcf().patch.set_facecolor('black')

def fetch_github_data(endpoint, params={}):
    url = f"https://api.github.com/{endpoint}"
    response = requests.get(url)
    return response.json()

username = "Zettalynx"
repo = "Zettalynx"

commits_data = fetch_github_data(f'repos/{username}/{repo}/commits')
code_frequency_data = fetch_github_data(f'repos/{username}/{repo}/stats/code_frequency')

plt.figure(figsize=(12, 6))

commits_count = len(commits_data)
additions = sum([week[1] for week in code_frequency_data])
deletions = sum([week[2] for week in code_frequency_data])

plt.bar(["Commits", "Additions", "Deletions"], [commits_count, additions, deletions], color=[primary_color, secondary_color, '#ff4b5c'])

configure_plot("Commits vs Code Frequency", "", "Count")
plt.savefig('github_stats_3.png', bbox_inches='tight', transparent=True)
