from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

#데이터 넣기
'''
db.users.insert_one({'name':'A','age':'1'})
db.users.insert_one({'name':'B','age':'2'})
'''

#데이터 보기
#print(list(db.users.find({},{'_id':0})))

#데이터 수정하기
#db.users.update_many({'name':'bobby'},{'$set':{'name':'bob'}})
db.users.update_one({'name':'bob'},{'$set':{'age':'10'}})