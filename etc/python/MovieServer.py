#DB 연결
import pymongo
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import flask

def load_all_movies():
    client = MongoClient('localhost',27017)
    #MongoClient는 Pymongo 안에 있는 애임 ALt + Ent로 import 해주면 됨.
    db = client.dbsparta.movies  #db안의 dbsparta안의 movies 끌어옴
    return list(db.find({},{'_id':0})) #_id는 빼고 불러옴. 0을 쓰면 안가져와.


def find_movie_by_title(t): #타이틀이 무언가 일때 그 무언가를 불러옴
    if t == None:      #/movies까지만 입력했을 때는 전체 불러오게 하는 코드
        return load_all_movies()
    client = MongoClient('localhost',27017)
    db = client.dbsparta.movies
    return list(db.find({'title':t},{'_id':0})) #DB에서는 cursor형식으로 돼있어서 리스트로 가져와야함.

def find_movie_by_rank(r):
    if r == None:
        return load_all_movies()
    client = MongoClient('localhost', 27017)
    db = client.dbsparta.movies
    return list(db.find({'rank': int(r)}, {'_id': 0}))



def write_movie(movie):
    #형태는 {"rank" :1, "score" :"10.0", "title" : "제목"}
    client = MongoClient('localhost', 27017)
    db = client.dbsparta.movies
    db.insert_one(movie)

#flask 이용하여 서버 만들기 ////GET 방식
#http://localhost:5000
def runServer():
    server = Flask('무비서버')


    @server.route('/')    #반드시 run하기 전에 만들어줘야 함.
    def home():
        return render_template('movies.html')

    #GET 방식
    @server.route('/movies', methods = ['GET']) #GET이 디폴트값. 따라서 안써도 무방.
    def movies():
        title_found =[]
        rank_found= []

        title = request.args.get('title') #flask의 request import필요. parameter를 title로 사용
        rank = request.args.get('rank') #parameter를 rank로 사용
                                        #즉, http://localhost:5000/movies?title=무언가
                                        #즉, http://localhost:5000/movies?rank=무언가
        if title is None and rank is None:
            return jsonify(load_all_movies())

        if title is not None:
            title_found = find_movie_by_title(title)

        if rank is not None:
            rank_found = find_movie_by_rank(rank)

        found = title_found + rank_found
        return jsonify(found)

    '''
    http://localhost:5000/movies 까지만 입력하면 전체영화 json형태로 가져오고
    http://localhost:5000/movies?title=원더 하면 제목이 '원더'만 가져오고
    http://localhost:5000/movies?rank=3 하면 rank가 3인것만 가져오고
    
    http://localhost:5000/movies?title=원더&rank=7 
    즉, 제목과 랭크를 올바르게 불러오면 똑같은거 두개 출력
    
    http://localhost:5000/movies?title=원더&rank=3
    즉, 제목이 원더인 영화와 랭크가 3인 영화 두개 출력.
    '''

    #POST 방식
    @server.route('/movies', methods=['POST'])
    # 주소로 접근했을 때, 접근불가
    def add_movie():
        title = request.form['title']
        rank = request.form['rank']
        score = request.form['score']

        if title is None or rank is None or score is None:
            result = {"message": "parameter is not filled", "result": "error"}
            return jsonify(result)

        movie = {'rank': int(rank), 'title': title, 'score': score}
        write_movie(movie)

        result = {'message': 'OK!', 'result':'success'}
        return jsonify(result)




    server.run('0.0.0.0', port = 5000, debug=True)

runServer()



