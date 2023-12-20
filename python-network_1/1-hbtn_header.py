import requests
import sys

if len(sys.argv) > 1:
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(f"X-Request-Id: {request_id}")
        else:
            print("X-Request-Id header not found in the response.")
    else:
        print(f"Request failed with status code {response.status_code}.")
else:
    print("Please provide a URL as an argument.")