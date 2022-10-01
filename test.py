import requests

r = requests.get('http://127.0.0.1:8000/main/correlation/')
print(r)
# print(r.content.decode('utf-8'))