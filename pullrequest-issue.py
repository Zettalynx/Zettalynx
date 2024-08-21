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

pulls_data = fetch_github_data(f'repos/{username}/{repo}/pulls')
issues_data = fetch_github_data(f'repos/{username}/{repo}/issues')

plt.figure(figsize=(12, 6))

pulls_count = len(pulls_data)
issues_count = len(issues_data)

plt.bar(["Pull Requests", "Issues"], [pulls_count, issues_count], color=[primary_color, secondary_color])

configure_plot("Pull Requests vs Issues", "", "Count")
plt.savefig('github_stats_2.png', bbox_inches='tight', transparent=True)
