#지니차트 순위/곡제목/가수 출력해보기
# [1] WANNABE / ITZY

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
resp = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(resp.text, 'html.parser')


#곡 제목 리스트 만들기
aTagstitle =  soup.select('td.info > a.title.ellipsis')
title =[]
for i in aTagstitle:
    title.append(i.text.strip())

# 가수 리스트 만들기
aTagsSinger = soup.select('td.info > a.artist.ellipsis')
singer =[]
for i in aTagsSinger:
    singer.append(i.text)

# 1~50순위 리스트 만들기
Rank = list(range(1,51))

#zip함수로 동일한 길이의 리스트 합쳐서 for문으로 출력
for a,b,c in list(zip(Rank,singer,title)):
    print(str(a) + "위 / " + b + "/ " + c)


