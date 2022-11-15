import hashlib
from flask import Flask, redirect, url_for
from pymongo import MongoClient, ASCENDING
import jwt
import datetime

client = MongoClient('mongodb+srv://kim:rlarudals@cluster0.dwgjq8c.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.blog
db_user = db.user
db_comment = db.commentList

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
SECRET_KEY = 'secret_key'

def checkAdmin(request):
    try:
        token = request.cookies.get('mytoken')
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_info = db_user.find_one({'name':payload['name']})
        return user_info['name']
    except:
        return False

@app.route('/')
def home():
    name = checkAdmin(request)
    if name:
        return render_template('index.html', name=name)
    else:
        return render_template('index.html')

@app.route('/<username>', methods=['GET'])
def detail(username):
    user = db_user.find_one({'name' : username})
    if user:
        user_temp =  user['temp']
        introduce = {
            'name' : user['name'],
            'mbti' : user['mbti'],
            'strength' : user['strength'],
            'style' : user['style'],
        }
        commentList = db_comment.find({'username' : username}, {'_id':False}).sort('num',-1)
        data = {
            'introduce' : introduce,
            'commentList' : commentList
        }
        if checkAdmin(request):
            name = checkAdmin(request)
            return render_template(user_temp, name=name, data = data)
        else:
            return render_template(user_temp, data = data)
    else:
        return jsonify({'result':'fail', 'msg': '그런 팀원은 없어용'})

# @app.route('/admin', methods=['GET'])
# def isAdmin():
#     name = checkAdmin(request)
#     if name:
#         return render_template('index.html', name=name)
#     else:
#         return render_template('admin_form.html')

##### 토큰에 로그인 정보를 담는 것의 단점####
@app.route('/admin', methods=['POST'])
def loginAdmin():
    name = request.form['name']
    password = request.form['password']
    
    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = db_user.find_one({'name':name, 'password': pw_hash})
    if user:
        payload = {
            'name' : name,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm = 'HS256')
        return jsonify({'result':'success', 'token': token})
    else:
        return jsonify({'result' : 'fail', 'msg':'check id or pw'})

@app.route('/admin/post', methods=['GET'])
def createGet():
   return render_template('create_user.html')

@app.route('/create', methods=['POST'])
def createPost():
   temp = request.form['temp']
   name = request.form['name']
   mbti = request.form['mbti']
   strength = request.form['strength']
   style = request.form['style']

   doc = {
      'temp': temp,
      'name': name,
      'mbti': mbti,
      'strength': strength,
      'style': style,
   }
   db.users.insert_one(doc)
   return jsonify({'msg': '저장 완료!'})


def getCmtNum(username):
    """
    commentList의 댓글 중 num의 숫자 중 가장 큰 수 + 1을 보내는 함수
    """
    if db_comment.count_documents({'username':username}) == 0:
        num = 1
    else:
        num = int(db_comment.find_one({'username':username}, sort=[('num',-1)])['num']) +1
    return num

@app.route('/<username>/comment', methods=['POST'])
def createComment(username):
    """
    댓글 기능을 처리하는 함수.
    num = 댓글들의 숫자 중에 가장 큰 숫자 + 1
    username = 댓글을 남기는 대상의 이름
    name = 댓글을 남기는 이름
    content = 댓글 내용
    """
    num = getCmtNum(username)
    user = db_user.find_one({'name': username})
    name = request.form['name']
    content = request.form['content']
    
    if user:
        doc = {
            'num' : num,
            'username' : username,
            'name' : name,
            'content' : content
        }
        db_comment.insert_one(doc)
        return jsonify({'result':'success'})
    else:
        return jsonify({'result':'Wrong Path', 'msg': '잘못된 접근입니다.'})

@app.route('/<username>/comment', methods=['DELETE'])
def deleteComment(username):
    num = request.form['num']
    print(num, username, db_comment.find_one({'username':username, 'num':int(num)}))
    db_comment.delete_one({'username':username, 'num':int(num)})
    return jsonify({'result': 'delete!'})

@app.route('/api/<username>', methods=['GET'])
def apiDetail(username):
    user = db_user.find_one({'name' : username})
    print(user)
    if user:
        user = dict(user)
        introduce = {
            'name' : user['name'],
            'mbti' : user['mbti'],
            'strength' : user['strength'],
            'style' : user['style'],
        }
        commentList = db_comment.find({'username' : username}, {'_id':False}).sort('num',-1)
        data = {
            'introduce' : introduce,
            'commentList' : commentList
        }
        return jsonify({data : data})
    else:
        return jsonify({'result':'fail', 'msg': '그런 팀원은 없어용'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=8000,debug=True)

##########################################
#######checkAdmin(request) 사용전 ##########
##########################################


# @app.route('/api/admin', methods=['GET'])
# def apiAdmin():
#     token = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         user_info = db_user.find_one({'name':payload['name']})
#         return jsonify({'result':'success', 'name':user_info['name']})
#     except jwt.ExpiredSignatureError:
#         return jsonify({'result': 'fail'})
#     except jwt.exceptions.DecodeError:
#         return jsonify({'result': 'fail'})

# @app.route('/')
# def home():
#     token = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         user_info = db_user.find_one({'name':payload['id']})
#         return render_template('index.html', name=user_info['id'],nam = 'asdf')
#     except:
#         return render_template('index.html')

# doc = {
#     'name' : '관리자짱',
#     'password' : hashlib.sha256('admin12'.encode('utf-8')).hexdigest()
# }
# db_user.inser_one(doc)

# @app.route('/admin', methods=['GET'])
# def isAdmin():
#     token = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         user_info = db_user.find_one({'name':payload['name']})
#         return render_template('index.html', name=user_info['name'])
#     except jwt.ExpiredSignatureError:
#         return render_template('admin_form.html')
#     except jwt.exceptions.DecodeError:
#         return render_template('admin_form.html')

# @app.route('/<username>', methods=['GET'])
# def detail(username):
#     """
#     """
#     user = db_user.find_one({'name' : username})
#     if user:
#         user = dict(user)
#         user_temp =  user['temp']
#         introduce = {
#             'name' : user['name'],
#             'mbti' : user['mbti'],
#             'strength' : user['strength'],
#             'style' : user['style'],
#         }
#         commentList = db_comment.find({'username' : username}, {'_id':False}).sort('num',-1)
#         data = {
#             'introduce' : introduce,
#             'commentList' : commentList
#         }
#         # return render_template(user_temp, data = data)
#         token = request.cookies.get('mytoken')
#         try:
#             payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#             user_info = db_user.find_one({'name':payload['name']})
#             return render_template(user_temp, name=user_info['name'], data = data)
#         except:
#             return render_template(user_temp, data = data)
#     else:
#         return jsonify({'result':'fail', 'msg': '그런 팀원은 없어용'})