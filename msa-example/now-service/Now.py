from flask import *
from http import HTTPStatus
import datetime as dt
import sqlite3

app = Flask(__name__)

# 메모리DB connection 설정.
con = sqlite3.connect(':memory:',check_same_thread=False)

@app.route('/wtisit')
def process_date():
    now = dt.datetime.now()
    return jsonify({
        "now": now,
        "status": HTTPStatus.OK
    })

if __name__ == '__main__':
    app.run('127.0.0.1',port=5010)
