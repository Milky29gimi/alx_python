"""Python script that fetches https://alu-intranet.hbtn.io/status"""
import requests

url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    print("Body response:")
    print("type: <class 'str'>")
    
    for line in response.text.splitlines():
        print(f"\t- {line}")
else:
    print(f"Request failed with status code {response.status_code}")
    