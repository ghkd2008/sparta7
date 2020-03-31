import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#db열기
client = MongoClient('localhost',27017)
db = client.dbsparta.movies

#여러번 실행 되지 않도록 함수에 가둬놈
def scrap_and_insert():
    # URL을 읽어서 HTML를 받아오고,
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    movies = soup.select('#old_content > table > tbody > tr')

    # movies (tr들) 의 반복문을 돌리기
    rank = 1
    for movie in movies:
        # movie 안에 a 가 있으면,
        a_tag = movie.select_one('td.title > div > a')
        if a_tag is not None:
            title = a_tag.text
            star = movie.select_one('td.point').text
            print(rank,title,star)
            #프린트 후에 DB에 넣기
            db.insert_one({'rank': rank, 'title': title, 'score':star})
            rank += 1


#DB에서 자료 한개씩 모두 리스트 형태로 가져오기, 한 줄씩 프린트
def find_and_print():
    all_movies = list(db.find())
    for movie in all_movies:
        print(movie)
# 이렇게 하면 랭크, 제목, 평점까지 다 가져옴

def find_print():
    # "어벤져스: 엔드게임" 영화의 평점 출력하기
    avengers = db.find_one({"title":"어벤져스: 엔드게임"})
    print(avengers["score"])

def same():
    #"어벤져스: 엔드게임"와 같은 평점 영화 찾기
    avengers = db.find_one({"title":"어벤져스: 엔드게임"})
    movies = list(db.find())
    for i in movies:
        if i["score"] == avengers["score"]:
            print(i["title"],i["score"])

def sameScoreZero():
# "어벤져스: 엔드게임"와 같은 평점 영화 찾아서 평점을 0으로 바꾸기
    avengers = db.find_one({"title": "어벤져스: 엔드게임"})
    movies = list(db.find())
    for i in movies:
        if i["score"] == avengers["score"]:
            db.update_many({'score':avengers["score"]},{'$set':{'score':0}})
    #만약    db.update_one({'score':avengers["score"]},{'$set':{'score':0}})하면,
    #어벤저스랑 평점이 같은 영화들 중 제일 먼저 검색된 한 개만 0점으로 바뀜.









