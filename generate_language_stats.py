import requests
import json

def get_language_stats(username, repo):
    url = f"https://api.github.com/repos/{username}/{repo}/languages"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}

def generate_markdown(stats, repo):
    total = sum(stats.values())
    markdown = f"### Language Stats for [{repo}](https://github.com/{username}/{repo})\n\n"
    markdown += "| Language | Percentage |\n"
    markdown += "|----------|------------|\n"
    for language, count in stats.items():
        percentage = (count / total) * 100
        markdown += f"| {language} | {percentage:.2f}% |\n"
    return markdown

if __name__ == "__main__":
    username = "Zettalynx"
    repo = "Zettalynx"
    stats = get_language_stats(username, repo)
    if stats:
        markdown_content = generate_markdown(stats, repo)
        with open("language_stats.md", "w") as f:
            f.write(markdown_content)
    else:
        print("Failed to retrieve language stats.")
