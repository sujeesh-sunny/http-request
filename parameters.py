import requests

params = {
    "name":"sujeesh",
    "age" : 25,
    "password" : "sujeesh sunny"
}

response = requests.get("https://httpbin.org/get",params = params)

print(response.url)
print(response.json())