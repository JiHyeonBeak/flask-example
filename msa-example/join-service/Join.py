from flask import *
from http import HTTPStatus
import datetime as dt
import sqlite3
import requests

app = Flask(__name__)
# 메모리 DB. 일회성 접속
con = sqlite3.connect(':memory:',check_same_thread=False)

# DB 생성
cur = con.cursor()
cur.execute("CREATE TABLE HAMONICA_USER(user_name text,age int, email text,introduce text, join_date date );")

@app.route("/addUser", methods=['POST'])
def addUser():
    now = dt.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    cur.execute('INSERT INTO HAMONICA_USER (user_name,age,email,introduce,join_date) VALUES(?,?,?,?,?);',(
        request.get_json()["userName"],
        request.get_json()["age"],
        request.get_json()["email"],
        request.get_json()["introduce"],
        now
    ))
    cur.execute('SELECT * FROM HAMONICA_USER')
    for row in cur:
        print("::: check data ::::",row)
    cur.close
    return jsonify({
        "status": HTTPStatus.OK
    })

@app.route("/getMembers")
def getMembers():
    cur.execute('SELECT * FROM HAMONICA_USER')
    list = cur.fetchall()
    cur.close
    return jsonify({
        "members": list,
        "status": HTTPStatus.OK
    })

if __name__ == '__main__':
    app.run('127.0.0.1',port=5020)
