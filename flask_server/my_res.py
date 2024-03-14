import requests

# res = requests.get('http://127.0.0.1:3000/api/main/1')
res1 = requests.post('http://127.0.0.1:3000/api/main', {'Privet'})
print(res1.json())