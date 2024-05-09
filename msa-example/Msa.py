from flask import *
import datetime as dt

app = Flask(__name__)

@app.route('/')
def call_sub():
    now = process_date()
    return render_template('sub.html',now=now)

def process_date():
    return dt.datetime.now()

# 최종 웹서버 실행 함수
if __name__ == '__main__':
    app.run()
