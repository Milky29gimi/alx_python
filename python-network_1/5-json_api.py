import requests
import sys

url = 'http://0.0.0.0:5000/search_user'

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

payload = {'q': letter}
response = requests.post(url, data=payload)

try:
    json_data = response.json()
    if json_data:
        print(f"[{json_data['id']}] {json_data['name']}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")