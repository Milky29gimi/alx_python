"""Check"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)

request = response.headers.get('X-Request-Id')
print(request)