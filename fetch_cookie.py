import requests
import json

SOURCE_URL = "https://pkll.xojiv79335.workers.dev/"

try:
    response = requests.get(SOURCE_URL, timeout=10)
    response.raise_for_status()  # Raises HTTPError if not 200

    data = response.json()

    # Check if data is a non-empty list
    if isinstance(data, list) and len(data) > 0 and "cookie" in data[0]:
        cookie_value = data[0]["cookie"]
    else:
        raise ValueError("No valid cookie found in the response.")

    cookie_json = {"cookieHeader": cookie_value}

    with open("cookie.json", "w") as f:
        json.dump(cookie_json, f, indent=2)

    print("cookie.json updated successfully!")

except Exception as e:
    print(f"Error fetching or writing cookie: {e}")
    exit(0)  # Exit 0 so GitHub Actions doesn’t fail the workflow
