from flask import *
import random as r

app = Flask(__name__)

datas = {
    1:'子寅辰午申戌',
    2:'巳卯丑亥酉未',
    3:'卯丑亥酉未巳',
    4:'子寅辰午申戌',
    5:'丑亥酉未巳卯',
    6:'寅辰午申戌子',
    7:'辰午申戌子寅',
    8:'未巳卯丑亥酉'
}


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/num', methods = ['GET'])
def get_num():
    _up = r.randrange(1,9)
    _down = r.randrange(1,9)
    movement = r.randrange(1,7)

    result = format_word(_up,_down)
    #result = str(_up) + str(_down)
    return result

def calc_mv():
    return

def format_word(u,d):
    # 상괘 가공
    buf_u = datas.get(u)
    buf1 = buf_u[0:3]

    # 하괘 가공
    buf_d = datas.get(d)
    buf2 = buf_d[2:5]
    
    #로깅
    print("buf1 :",buf1)
    print("buf2 :",buf2)
    
    result = ''
    return result

if __name__ == '__main__':
    app.run()