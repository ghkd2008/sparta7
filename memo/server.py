from flask import Flask, render_template, request, jsonify
import requests
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup



def scrap_site(url,comment):
    #url에 html을 가져온다 (requests)
    response = requests.get(url)
    html = response.text

    #meta태그를 찾는다 (Beautifulsoup4)
    soup = BeautifulSoup(html, 'html.parser')

    if soup.select_one('meta[property="og:url"]') is None:
        return False
    if soup.select_one('meta[property="og:image"]') is None:
        return False
    if soup.select_one('meta[property="og:title"]') is None:
        return False
    if soup.select_one('meta[property="og:description"]') is None:
        return False

    #<meta property="og:url" content="..."/>
    address = soup.select_one('meta[property="og:url"]')['content']

    #<meta property="og:image" content="..."/>
    image = soup.select_one('meta[property="og:image"]')['content']

    #<meta property="og:title" content="..."/>
    title = soup.select_one('meta[property="og:title"]')['content']

    #<meta property="og:description" content="..." />
    description = soup.select_one('meta[property="og:description"]')['content']


    # 각각의 content를 찾아와서
    data = {
        'url': address,
        'image': image,
        'title': title,
        'description': description,
        'comment': comment
    }

    #db에 저장한다 (pymongo)
    client = MongoClient('localhost',27017)
    db = client.dbsparta.memo
    db.insert_one(data)
    return True

def start_server():
    server = Flask("메모장서버")

    @server.route('/')
    def home():
        return render_template('memoindex.html')

    @server.route('/post', methods= ['GET'])
    def get_posts():
        #db에 연결한다
        client = MongoClient('localhost', 27017)
        db = client.dbsparta.memo

        #db에서 모든 포스트를 가져온다
        posts =list(db.find({},{'_id':0}))
        #json으로 만들어서 내보낸다
        return jsonify(posts)

    @server.route('/post', methods= ['POST'])
    def post():
        # url하고 comment 얻기
        if 'url' not in request.form or 'comment' not in request.form:
            result =  {'status':'error', 'message':'url하고 comment를 넣어주세요'}
            return jsonify(result)

        url = request.form['url']
        comment = request.form['comment']

        result = scrap_site(url,comment)

        # scrap_site(url,comment) 실행
        # 결과 보내주기
        if result is True:
            result = {'status':'ok', 'message':'저장되었습니다'}
            return jsonify(result)

        result = {'status':'fail', 'message':'지원하지 않는 사이트입니다'}
        return jsonify(result)

    server.run('0.0.0.0', port = 5000, debug =True)

start_server()
