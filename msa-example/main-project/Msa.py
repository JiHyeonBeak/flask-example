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
def callSub():
    now = processDate()
    today = processFortune()
    return render_template('main.html',now=now,today=today)

@app.route('/getJoin')
def callJoinPage():
    return render_template('Join.html')

def processDate():
    response = requests.get('http://localhost:5010/wtisit').json()
    #response = response.json()
    print(response)
    return response.get('now')

def processFortune():
    response = requests.get('http://localhost:5010/todayis').json()
    #response = response.json()
    print(response)
    return response.get('result')

@app.route("/shootingdata", methods=['POST'])
def addData():
    rdata = request.form.get("wrapData")
    cur.execute('INSERT INTO MEMOBOARD VALUES(:CONTENT);', {"CONTENT":rdata})
    cur.execute('SELECT * FROM MEMOBOARD')
    for row in cur:
        print(row)
    cur.close
    print("::: check data ::::",rdata)
    return redirect(url_for('callSub',rdata=rdata))

@app.route("/getList")
def getList():
    response = requests.get('http://localhost:5010/getList').json()
    print("::: List :::: ",response)
    return render_template('list.html',list=response.get('list'))

@app.route("/getMembers")
def getMembers():
    response = requests.get('http://localhost:5020/getMembers').json()
    print("::: Members :::: ",response)
    return render_template('memberList.html',members=response.get('members'))

@app.route("/addUser", methods=['POST'])
def addUser():
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://localhost:5020/addUser',
        json={
        "userName": request.form.get("userName"),
        "age": request.form.get('age'),
        "email": request.form.get("email"),
        "introduce": request.form.get("introduce")
        }, 
    headers=headers, timeout=10)
    print("::: addUser Response :::: ",response)
    return render_template('complete.html')

if __name__ == '__main__':
    app.run()
