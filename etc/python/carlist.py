#네이버 자동차 리스트 출력해보기
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
resp = requests.get('https://auto.naver.com/cmpr/cmprMain.nhn',headers=headers)

text = BeautifulSoup(resp.text, 'html.parser')

carNameTag = text.select('dt > a > strong')
carName =[]
for i in carNameTag:
    carName.append(i.text)
#print(carName)

carCateTag = text.select('div.model_popular > div.list > ul > li > a > span')
#carCateTag = text.select('#container > div.model_popular > div.list > ul > li:nth-child(1) > a > span')
carCate = []
for i in carCateTag:
    carCate.append(i.text)

i=0
for a in carCate:
    print(a)
    for b in carName[i:i+7]:
        print(b)
    print()
    i+=7


'''
    for b in carName:
        b=carName[i:i+6]
        print(b)
    i+7
'''



