from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://jungletest:test@3.34.185.1', 27017)
db = client.alonememo2

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')
## 메모 get으로 읽어보내기
@app.route("/memo", methods=["GET"])
def readMemo():
    result = list(db.memo.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'memos': result})
## post로 얻어온 값을 DB에 작성
@app.route("/memo", methods=["POST"])
def writeMemo():
    title = request.form["title"]
    contents = request.form["contents"]
    result = db.memo.insert_one({"title" : title, "contents" : contents})
    return jsonify({'result': 'success'})
## post로 얻어온 값을 DB에 수정
@app.route("/memoUpdate", methods=["POST"])
def memoUpdate():
    memoNum = int(request.form["cardNum"])
    title = request.form["title"]
    contents = request.form["contents"]
    memoList = list(db.memo.find({}, {'title': 0 , 'contents': 0}))
    result = db.memo.update_one(memoList[memoNum], {"$set": {"title": title , 'contents' : contents}})
    return jsonify({'result': 'success'})
## post로 얻어온 값으로 데이터베이스에 있는 메모 삭제
@app.route("/memoDelete", methods=["POST"])
def memoDelete():
    memoNum = int(request.form["cardNum"])
    memoList = list(db.memo.find({}, {'title': 0 , 'contents': 0}))
    result = db.memo.delete_one(memoList[memoNum])
    return jsonify({'result': 'success'})

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)