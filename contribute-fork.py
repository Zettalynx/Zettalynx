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

contributors_data = fetch_github_data(f'repos/{username}/{repo}/contributors')
forks_data = fetch_github_data(f'repos/{username}/{repo}/forks')

plt.figure(figsize=(12, 6))

contributors_count = len(contributors_data)
forks_count = len(forks_data)

plt.bar(["Contributors", "Forks"], [contributors_count, forks_count], color=[primary_color, secondary_color])

configure_plot("Contributors vs Forks", "", "Count")
plt.savefig('github_stats_4.png', bbox_inches='tight', transparent=True)
