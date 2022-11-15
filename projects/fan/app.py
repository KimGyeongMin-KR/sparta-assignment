from unicodedata import name
from pymongo import MongoClient
client = MongoClient('mongodb+srv://kim:rlarudals@cluster0.dwgjq8c.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/list', methods=['GET'])
def showList():
   cheerList = list(db.cheerList.find({}, {'_id' : False}))
   return jsonify({'result':'success', 'cheerList': cheerList})

@app.route('/cheer', methods=['POST'])
def createCheer():
    name = request.form['name']
    content = request.form['content']
    db.cheerList.insert_one({'name' : name, 'content': content})
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
   
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)