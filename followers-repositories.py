import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Warna tema
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

followers_data = fetch_github_data(f'users/{username}/followers')
repos_data = fetch_github_data(f'users/{username}/repos')

plt.figure(figsize=(12, 6))

dates = [datetime.now()]
followers_count = [len(followers_data)]
repos_count = [len(repos_data)]

plt.plot(dates, followers_count, label='Followers', color=primary_color)
plt.plot(dates, repos_count, label='Repos', color=secondary_color)

configure_plot("Followers vs Repos", "Date", "Count")
plt.legend()
plt.savefig('github_stats_1.png', bbox_inches='tight', transparent=True)
