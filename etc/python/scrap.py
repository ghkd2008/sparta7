#scraping /crawling
'''
1.홈페이지 들어가 html 가져오기
2. html에서 내가필요한 정보 찾아내기
3. 가져온다
'''

#1.html 가져오기(beautifilsoup4 사용)
import requests
import bs4

resp = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

soup = bs4.BeautifulSoup(resp.text, 'html.parser')

aTags = soup.select('div.tit3 a')
#tit3 클래스를 가진 div 태그를 찾아서 그 하위의 a 태그를 찾아 aTags변수에 저장

for i in aTags:
    print(i.text)
# 즉 a태그들을 다 가져온 후 그 안에 들은 텍스트만 출력한것임. 범위를 0부터 9까지니까 10개의 제목만 출력됨.


