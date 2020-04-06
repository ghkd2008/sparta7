from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework1.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    email_receive = request.form['email_give']
    phone_receive = request.form['phone_give']

    order = {
        'name':name_receive,
        'count':count_receive,
        'email':email_receive,
        'phone':phone_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result':'success', 'msg': '주문이 성공적으로 작성되었습니다!'})


@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)