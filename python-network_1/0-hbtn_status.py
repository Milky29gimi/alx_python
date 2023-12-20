import requests

url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    print("Status code: 200 OK")
    print("Response body:")
    for line in response.text.splitlines():
        print(f"\t- {line}")
else:
    print(f"Request failed with status code {response.status_code}")
    