import requests
respons = requests.post ("http://dev.getdesk.com")
print(respons.text)