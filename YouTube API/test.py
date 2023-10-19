import requests
BASE = "http://127.0.0.1:5000/"
data = [{"likes": 78, "name": "Aastha", "views": 1000},
        {"likes": 100, "name": "Nandini", "views": 1200},
        {"likes": 150, "name": "Pari", "views":1500}]

for i in range(len(data)):
    response = requests.put(BASE + "video/"+ str(i), data[i])
    print(response.json())



input()
response = requests.patch(BASE + "video/1",{"name":"NANDINI", "likes":1000})

print(response.json())
response = requests.get(BASE + "video/1")

print(response.json())