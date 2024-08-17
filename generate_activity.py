import requests
import json

# GitHub username
username = "Zettalynx"

# GitHub API URL untuk aktivitas publik
url = f"https://api.github.com/users/{username}/events/public"
response = requests.get(url)

if response.status_code == 200:
    events = response.json()

    # Ambil 5 aktivitas terbaru
    latest_events = events[:5]

    with open("activity.md", "w") as f:
        f.write("# Recent GitHub Activity\n\n")
        for event in latest_events:
            repo_name = event['repo']['name']
            event_type = event['type']
            event_time = event['created_at']
            f.write(f"- **{event_type}** in [{repo_name}](https://github.com/{repo_name}) at {event_time}\n")
else:
    print(f"Failed to retrieve events: {response.status_code}")
