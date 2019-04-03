import requests
req=requests.get("https://www.facebook.com")
print(req.content)
