import os
import requests

def check_server_status(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False


servers = [
    {"name": "The Black Swan", "url": "https://theblackswan.devon.social:5151/"},
    {"name": "Example Server", "url": "https://example.com:5050/"}
]

markdown_template = """<center>
| Server Name | URL | Port | Whitelist | Status |
|-------------|-----|------|-----------|--------|
"""

for server in servers:
    status_image = "online" if check_server_status(server["url"]) else "offline"
    url_encoded = server['url'].replace(":", "%3A").replace("/", "%2F")
    markdown_template += f'| {server["name"]} | [{server["url"].replace("https://", "").replace("/", "")}]({server["url"]}) | {server["url"].split(":")[1]} | No | <img src="https://img.shields.io/website?down_color=lightgrey&down_message={status_image}&style=flat-square&up_color=brightgreen&up_message=online&url={url_encoded}" alt="Server Status"> |\n'

markdown_template += "\n</center>"

# Save to Markdown file
with open("servers_status.md", "w") as md_file:
    md_file.write(markdown_template)

# This code would be part of your CI/CD pipeline
os.system('git add servers_status.md')
os.system('git commit -m "Update server statuses"')
os.system('git push origin main')
