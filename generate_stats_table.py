import requests
import numpy as np
from datetime import datetime, timedelta

username = "Zettalynx"

# Ambil data dari GitHub API
repo_url = f"https://api.github.com/users/{username}/repos"
user_url = f"https://api.github.com/users/{username}"

repo_response = requests.get(repo_url)
user_response = requests.get(user_url)

repos = repo_response.json()
user = user_response.json()

# Data
repo_names = [repo['name'] for repo in repos]
stars = [repo['stargazers_count'] for repo in repos]
forks = [repo['forks_count'] for repo in repos]
commits = [repo['size'] for repo in repos]  # Simulasi data commit
recent_prs = ["PR Title"] * len(repos)  # Simulasi PR
recent_issues = ["Issue Title"] * len(repos)  # Simulasi Issue
languages = [repo['language'] for repo in repos]

# Timeline
dates = [datetime.now() - timedelta(days=i*10) for i in range(len(repos))]
contributions = np.random.randint(10, 100, size=len(repos))

# Generate table
table = "| Repository | Stars | Forks | Commits | Latest PR | Recent Issue | Language | Contributions |\n"
table += "|------------|-------|-------|---------|-----------|--------------|----------|---------------|\n"

for i in range(len(repo_names)):
    table += f"| {repo_names[i]} | {stars[i]} | {forks[i]} | {commits[i]} | {recent_prs[i]} | {recent_issues[i]} | {languages[i]} | {contributions[i]} |\n"

# Save to Markdown file
with open("github_stats.md", "w") as file:
    file.write("# GitHub Repository Statistics\n")
    file.write(table)
