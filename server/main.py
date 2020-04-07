# Web API with python and flask
import flask
from flask import jsonify
from flask_cors import CORS
from xpinyin import Pinyin
import db

app = flask.Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
#app.config["DEBUG"] = True

@app.route('/api/hanzi/<id>', methods=['GET'])
def gethanzi(id=0):
    r = db.get_data(db.sql_connection(), (id,))
    a = {}
    for i in r:        
        a["id"] = i[0]
        a["hanzi"] = i[1]
        a["type"] = i[2]
        a["learned"] = i[3]
        a["passed"] = i[4]        
    return jsonify(a)


@app.route('/hanzi', methods=['POST'])
def updatehanzi(data):
    d = (data["hanzi"], data["type"],
         data["learned"], data["passed"], data["id"])
    r = db.update_data(db.sql_connection(), d)
    return r

# 获取汉字或词的拼音
@app.route('/api/pinyin/<string:q>', methods=['GET'])
def pinyin(q):
    p = Pinyin()
    return jsonify(p.get_pinyin(q, tone_marks='marks'))

app.run(host='0.0.0.0', port=5000, debug=True)
