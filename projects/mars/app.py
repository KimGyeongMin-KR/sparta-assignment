
from pymongo import MongoClient
client = MongoClient('mongodb+srv://kim:rlarudals@cluster0.dwgjq8c.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }

    db.orders.insert_one(doc)

    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    all_users = list(db.orders.find({}, {'_id' : False}))

    return jsonify({'users': all_users})

if __name__ == '__main__':
   app.run('0.0.0.0', port=8000, debug=True)




# @app.route('/')
# def home():
#     return render_template('index.html')


# @app.route("/mars", methods=["POST"])
# def web_mars_post():
#     name_receive = request.form['name_give']
#     address_receive = request.form['address_give']
#     size_receive = request.form['size_give']

#     doc = {
#         'name': name_receive,
#         'address': address_receive,
#         'size': size_receive
#     }
#     db.mars.insert_one(doc)


#     return jsonify({'msg': '주문 완료!'})

# @app.route("/mars", methods=["GET"])
# def web_mars_get():
#     return jsonify({'msg': 'GET 연결 완료!'})
