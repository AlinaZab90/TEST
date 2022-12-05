import requests
import xml.etree.ElementTree as ET

session = requests.Session()

link = "http://dev.getdesk.com/sign_in"

login = requests.get("http://dev.getdesk.com/login").text

root = ET.fromstring(login)
t = root.find(".//input[@name='_token']")
#print(t)
headers = {'X-CSRF-Token':"random"}

datas = {
    'email': '...',
    'password': '...'
}

responce = session.post(link, data = datas, headers = headers).text