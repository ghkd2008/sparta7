import pymongo

'''
#sql형태
#파일 > 시트 > 정보
#database > collection > data

즉, 하나의 시트(컬렉션)안에는 같은 종류의 데이터가 들어감
'''

'''
mongodb는 
<하나의 mongodb> 안에 database안에 collection안에 data
'''

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다. localhost서버의 27017포트
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection을 만들고 그 곳에 {'name':'bobby','age':21}를 넣습니다.
'''
db.users.insert_one({'name':'bobby','age':21})  # ==client.dbsparta.users.insert_one({'name':'bobby','age':21})
db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})
'''

#database 조작
'''
CRUD:create (=insert), read(=find), update, delete

'''

#값을 찾아오기
all_users = list(db.users.find())
#-> list타입이니까 for문이나 인덱싱으로 출력하면 됨.
#for user in all_users:
 #   print(user)

#조건부로 찾아오기
'''
all_users = list(db.users.find({'age':21}))
for user in all_users:
    print(user)
'''

#맨처음에 찾아지는 나이 21살 한명만 찾아내기
'''
print(db.users.find_one({'age':21}))
'''

##update하기

#bobby한명만 22살로
#db.users.update_one({'name':'bobby'},{'$set':{'age':22}})

#bobby모두 22살로
#db.users.update_many({'name':'bobby'},{'$set':{'age':22}})


#database에서는 delete는 잘하지 않음.
'''
createdAt, deletedAt이라는 key값을 정해 놓고 value를 주는 경우가 많음,
'''

