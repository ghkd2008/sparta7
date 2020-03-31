import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#db열기
client = MongoClient('localhost',27017)
db = client.dbsparta.bike

def insert_and_print():
    print("따릉이 현황")

    resp = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99")
    respjson = resp.json()
    for i in respjson["rentBikeStatus"]["row"]:
        print(i["stationName"][5:] + "(" + str(i["parkingBikeTotCnt"]) + "/" + i["rackTotCnt"] + ")")
        db.insert_one({"stationName":i["stationName"][5:],"bikeExist":i["parkingBikeTotCnt"], "rack":i["rackTotCnt"] })

def find_and_print():
    allBikes = list(db.find())
    for i in allBikes:
        station =i["stationName"]
        bike =i["bikeExist"]
        rack =i["rack"]
        print(station, bike, rack)


find_and_print()

