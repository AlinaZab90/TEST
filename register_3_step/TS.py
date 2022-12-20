from pickle import FALSE
import requests
from lxml import etree
from io import StringIO
import json


session = requests.Session()
login = session.get("http://dev.getdesk.com/login").text

parser = etree.HTMLParser()
tree   = etree.parse(StringIO(login), parser)

r = tree.xpath(".//input[@name='_token']")


headers = {'X-CSRF-Token':r[0].attrib['value']}

datas = {
    'email': 'alina.zabaidulina@mail.ru',
    'password': 'hxt6LtkLpNFBcWu'
}

response= session.post("http://dev.getdesk.com/sign_in", data = datas, headers = headers).text

#office = session.post("http://dev.getdesk.com/xhr/office")
#print(office.status_code)
#office_id = json.loads(office.text)["id"]

office_id = 165
url_space ='http://dev.getdesk.com/xhr/office/{office}/space'.format(office=office_id)
space = {
    "id":2,
    "name":"Jjj",
    "desc":"Hh",
    "count":1,
    "places":1,
    "comforts":
    [
        {"groupId":1,
        "groupName":"Private offices amenities",
        "group":[
            {"id":4,
            "name":"Scanner",
            "checked":False},
            {"id":3,
            "name":"Printer",
            "checked":False},
            {"id":77,
            "name":"Flipchart",
            "checked":False},
            {"id":80,
            "name":"Сoffee machine",
            "checked":False},
            {"id":64,
            "name":"Microphone",
            "checked":False},
            {"id":62,
            "name":"Fax",
            "checked":False},
            {"id":61,
            "name":"Have a PC",
            "checked":False},
            {"id":58,
            "name":"Video conferencing equipment",
            "checked":False},
            {"id":68,
            "name":"Headphones",
            "checked":False},
            {"id":5,
            "name":"Photocopier",
            "checked":False},
            {"id":71,
            "name":"TV",
            "checked":False}
            ]
        }
     ],
    "type":"Private cabinet",
    "priceFields":{"price":[{"id":1,"value":0,"currency":"$","disabled":False},{"id":2,"value":0,"currency":"$","disabled":True}],"priceDiscount":[{"id":3,"value":0,"currency":"$","disabled":True},{"id":4,"value":0,"currency":"$","disabled":True},{"id":5,"value":0,"currency":"$","disabled":True},{"id":6,"value":0,"currency":"$","disabled":True},{"id":7,"value":0,"currency":"$","disabled":True}]},
    "images":[],
    "disabled":False}

#print(space.keys())
#print(space.items())

#response_space = session.post(url_space, json= space)
#print(response_space.text)
#type_id = json.loads(response_space.text)["id"]
type_id = 321







