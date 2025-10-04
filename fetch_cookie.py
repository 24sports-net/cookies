import requests
import json

SOURCE_URL = "https://pkll.xojiv79335.workers.dev/"

try:
    response = requests.get(SOURCE_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    cookie_value = data[0]['cookie']
    cookie_json = {"cookieHeader": cookie_value}

    with open("cookie.json", "w") as f:
        json.dump(cookie_json, f, indent=2)

    print("cookie.json updated successfully!")

except Exception as e:
    print(f"Error fetching or writing cookie: {e}")
