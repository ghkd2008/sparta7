import requests
'''
def name(a):
    print(a)


r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
name("시작")
for row in rjson['RealtimeCityAir']['row']:
    # 0.02 이상만 출력
    if row['NO2'] >= 0.02:
        print(row["MSRSTE_NM"], ":", row['NO2'])
name("끝")
'''
# ctrl +alt + l : 자동줄맞춤


print("따릉이 현황")

resp = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/bikeList/1/99")
respjson = resp.json()
for i in respjson["rentBikeStatus"]["row"]:
    print(i["stationName"][5:] + "(" + str(i["parkingBikeTotCnt"]) + "/" + i["rackTotCnt"] + ")")

