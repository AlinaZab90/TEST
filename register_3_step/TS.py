import requests
from lxml import etree
from io import StringIO

session = requests.Session()
login = session.get("http://dev.getdesk.com/login").text

parser = etree.HTMLParser()
tree   = etree.parse(StringIO(login), parser)

r = tree.xpath(".//input[@name='_token']")


headers = {'X-CSRF-Token':r[0].attrib['value']}

datas = {
    'email': '...',
    'password': '...'
}

response= session.post("http://dev.getdesk.com/sign_in", data = datas, headers = headers).text

response = session.post("http://dev.getdesk.com/xhr/office")
print(response.status_code)
print(response.text)

