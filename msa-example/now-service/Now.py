from flask import *
import datetime as dt
import sqlite3

app = Flask(__name__)

# 메모리DB connection 설정.
con = sqlite3.connect(':memory:',check_same_thread=False)

@app.route('/wtisit')
def process_date():
    return dt.datetime.now()

if __name__ == '__main__':
    app.run()
