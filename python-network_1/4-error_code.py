import requests
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print("Response body:")
        print(response.text)
else:
    print("Please provide a URL as an argument.")