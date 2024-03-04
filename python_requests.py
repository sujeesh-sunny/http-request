import requests
responses = requests.get("https://api.postalpincode.in/pincode/679333")
print(responses)
if responses.status_code == 200 :
    print("it's working")