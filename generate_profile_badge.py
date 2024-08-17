import requests

# Ambil data dari GitHub API
username = "Zettalynx"
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
user_data = response.json()

# Simulasi data untuk badge (contoh)
followers = user_data['followers']

# Buat SVG badge
svg_content = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="50">
  <style>
    .title {{ font: bold 20px sans-serif; fill: #333; }}
  </style>
  <text x="10" y="30" class="title">Followers: {followers}</text>
</svg>
"""
with open('profile_badge.svg', 'w') as file:
    file.write(svg_content)
