import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for key, value in data.items():
        print(f"- {key}: {value}")
else:
    print(f"Error: {response.status_code}")