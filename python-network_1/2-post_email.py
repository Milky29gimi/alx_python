import requests
import sys

if len(sys.argv) > 2:
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Response body:")
        print(response.text)
    else:
        print(f"Request failed with status code {response.status_code}.")
else:
    print("Please provide both a URL and an email address as arguments.")