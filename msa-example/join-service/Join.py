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
def add_user():
    now = dt.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    cur.execute('INSERT INTO HAMONICA_USER (user_name,age,email,introduce,join_date) VALUES(?,?,?,?,?);',(
        request.form.get('userName', type=str),
        request.form.get('age', type=int),
        request.form.get('email', type=str),
        request.form.get('introduce', type=str),
        now
    ))
    cur.execute('SELECT * FROM HAMONICA_USER')
    for row in cur:
        print("::: check data ::::",row)
    cur.close
    return jsonify({
        "status": HTTPStatus.OK
    })

if __name__ == '__main__':
    app.run('127.0.0.1',port=5020)
