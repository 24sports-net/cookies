import requests, json, re

URL = "https://pkll.xojiv79335.workers.dev/"
FILE_PATH = "cookie.json"
TARGET_CHANNEL = "Star Sports Select 1 HD"

# Fetch JSON
r = requests.get(URL)
data = r.json()

# Find the target channel
channel = next((c for c in data if c.get("channel_name") == TARGET_CHANNEL), None)
if not channel:
    print(f"Channel '{TARGET_CHANNEL}' not found")
    exit(0)

# Extract hdnea cookie from channel_url
url = channel.get("channel_url", "")
match = re.search(r"(hdnea=[^&]+)", url)
if not match:
    print("hdnea cookie not found")
    exit(0)

cookie_value = match.group(1)

# Save to JSON
with open(FILE_PATH, "w") as f:
    json.dump({"cookieHeader": cookie_value}, f, indent=4)

print(f"cookie.json created successfully: {cookie_value}")
