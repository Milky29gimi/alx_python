import requests
import sys

if len(sys.argv) > 2:
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info['id']
        print(f"Your GitHub user ID: {user_id}")
    else:
        print(f"Request failed with status code {response.status_code}")
else:
    print("Please provide your GitHub username and personal access token as arguments.")