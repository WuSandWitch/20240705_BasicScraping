import requests

url = 'https://attackmeua-1-d5034960.deta.app/'

r = requests.get(url)

print(r.headers)
print(r.text)