from flask import *
import datetime as dt
import sqlite3
import requests

app = Flask(__name__)
# 메모리 DB. 일회성 접속
con = sqlite3.connect(':memory:',check_same_thread=False)

# DB 생성
cur = con.cursor()
cur.execute("CREATE TABLE MEMOBOARD(CONTENT text);")

@app.route('/')
def call_sub():
    now = process_date()
    today = process_fortune()
    return render_template('main.html',now=now,today=today)

def process_date():
    response = requests.get('http://localhost:5010/wtisit').json()
    #response = response.json()
    print(response)
    return response.get('now')

def process_fortune():
    response = requests.get('http://localhost:5010/todayis').json()
    #response = response.json()
    print(response)
    return response.get('result')

@app.route("/shootingdata", methods=['POST'])
def add_data():
    rdata = request.form.get("wrapData")
    cur.execute('INSERT INTO MEMOBOARD VALUES(:CONTENT);', {"CONTENT":rdata})
    cur.execute('SELECT * FROM MEMOBOARD')
    for row in cur:
        print(row)
    cur.close
    print("::: check data ::::",rdata)
    return redirect(url_for('call_sub',rdata=rdata))

if __name__ == '__main__':
    app.run()
