import requests
import json
import os

SOURCE_URL = "https://pkll.xojiv79335.workers.dev/"

try:
    response = requests.get(SOURCE_URL, timeout=10)
    response.raise_for_status()

    data = response.json()

    # Check if we have at least one item with a cookie
    if isinstance(data, list) and len(data) > 0 and "cookie" in data[0]:
        cookie_value = data[0]["cookie"]
        cookie_json = {"cookieHeader": cookie_value}

        # Write or overwrite cookie.json
        with open("cookie.json", "w") as f:
            json.dump(cookie_json, f, indent=2)

        print("cookie.json updated successfully!")
    else:
        print("No valid cookie found in the response. Skipping update.")

except Exception as e:
    print(f"Error fetching or writing cookie: {e}")
