from flask import *
from http import HTTPStatus
import datetime as dt
import sqlite3
import random as r

app = Flask(__name__)

# 메모리DB connection 설정과 기본 테이블 생성.
con = sqlite3.connect(':memory:',check_same_thread=False)
cur = con.cursor()
cur.execute("CREATE TABLE Todayfortune(Date data, Content text);")

@app.route('/wtisit')
def process_date():
    global now
    now = dt.datetime.now()
    return jsonify({
        "now": now,
        "status": HTTPStatus.OK
    })

@app.route('/todayis')
def create_fortune():
    ft = ["행복한 날이네요.","건강을 주의하세요.","공부하기 좋은 날이네요.","매사 신중하세요."]
    buf_num = r.randrange(0,3)
    result = ft[buf_num]
    cur.execute("INSERT INTO Todayfortune (Date,Content) VALUES (?,?);",(now,result))
    cur.execute("SELECT * FROM Todayfortune")
    for row in cur:
        print(row)
    cur.close
    return jsonify({
        "result": result,
        "status": HTTPStatus.OK
    })

if __name__ == '__main__':
    app.run('127.0.0.1',port=5010)
