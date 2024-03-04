import requests
from bs4 import BeautifulSoup

response = requests.get("https://parivahan.gov.in/parivahan//en/content/mparivahan/khgx")

print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
print(soup.prettify())

# print(response.status_code)

# if response.status_code == 404 :
#     print("You Are Encountering a 404 Error")
