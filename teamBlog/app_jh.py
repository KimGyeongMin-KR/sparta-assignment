from flask import Flask, render_template, request, jsonify, url_for, redirect, session
app = Flask(__name__)

from pymongo import MongoClient

import jwt
import datetime
import hashlib
import json

client = MongoClient('mongodb+srv://test:sparta@cluster0.jbl9otl.mongodb.net/?retryWrites=true&w=majority')
db = client.dbminiproject

SECRET_KEY = 'secret_key'

def checkAdmin(request):
    token = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # payload['name'] = 'admin'
        user_info = db.login.find_one({'username': payload['name']},{'_id':False})
        return user_info['username']
    except:
        return False

@app.route('/')
def home():
    if checkAdmin(request):
        name = checkAdmin(request)
        return render_template('index.html', name = name)
    else:
        print('이름을 확인할 수 없습니다.')
        return render_template('index.html')

@app.route('/create', methods=['GET'])
def createGet():
    # return render_template('create_user.html')# 원채님 작업중
    return render_template('team_introduce.html')
@app.route('/create', methods=['POST'])
def createPost():

    temp = request.form['temp']
    name = request.form['name']
    mbti = request.form['mbti']
    strength = request.form['strength']
    stlye = request.form['style']
    selfIntroduction = request.form['selfIntroduction']

    doc = {
        'temp': temp,
        'name': name,
        'mbti': mbti,
        'strength': strength,
        'style': stlye,
        'selfIntroduction': selfIntroduction,
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success', 'msg':'저장 완료'})

# @app.route('/admin', methods=['GET'])
# def isAdmin():
#     name = checkAdmin(request)
#     if name:
#         return render_template('index.html', name = name)
#     else:
#         return render_template('index.html')
#         # return render_template('admin.html')


@app.route('/admin', methods=['POST'])
def loginAdmin():
    name = request.form['name']
    passw = request.form['password']

    # name = admin, password = 1234
    user = db.login.find_one({'username':name,'password':passw})

    if user is not None:

        payload = {
            'name': name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm = 'HS256')
        return jsonify({'result': 'success', 'token': token})
        # return render_template('index.html', name = name)
    else:
        return jsonify({'result': 'fail', 'msg': 'check id or pw'})
        # return render_template('admin_form.html')
        # return 'Dont Login'

@app.route('/<username>', methods=['GET'])
def detail(username):
    user = db.users.find_one({'name':username})
    if user:
        introduce = {
            'name': user['name'],
            'mbti': user['mbti'],
            'strength': user['strength'],
            'style': user['style'],
        }
        user_temp = user['temp']

        commentList = db.comment.find({'username': username},{'_id':False}).sort('num',-1)
        data = {
            'introduce': introduce,
            'commentList': commentList
        }
        if checkAdmin(request):
            name = checkAdmin(request)
            return render_template(user_temp, name = name, data = data)
        else:
            return render_template(user_temp,data= data)
    else:
        return '없는 팀원입니다.'
        # return jsonify({'result': 'fail', 'msg':'없는 팀원입니다.'})


def getCmtNum(username):
    if db.comment.count_documents({'username': username}) == 0:
        num = 1
        return num
    else:
        num = int(db.comment.find_one({'username': username}, sort=[('num', -1)])['num']) + 1
        return num

# @app.route('/<username>/comment', methods=['GET'])
# def getComment(username):
#     commentList = list(db.comment.find_one({'username': username},{'_id':False}))
#     return jsonify({'comments': commentList})

@app.route('/<username>/comment', methods=['POST'])
def createComment(username):
    num = getCmtNum(username)
    user = db.users.find_one({'name': username})
    name = request.form['name']
    content = request.form['content']

    if user is not None:
        doc = {
            'num': num,
            'username': username,
            'name': name,
            'content': content,
        }

        db.comment.insert_one(doc)
        return jsonify({'result': 'success'})
    else:
        return jsonify({'result': 'wrong path' ,'msg': '잘못된 접근'})

@app.route('/<username>/comment', methods=['DELETE'])
def deleteComment(username):
    num = request.form['num']
    db.comment.delete_one({'username': username, 'num':int(num)})
    return jsonify({'result': 'delete!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
