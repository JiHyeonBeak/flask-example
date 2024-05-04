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

datas2 = {
    1:[11,15,17,18,58,78,38,31],
    2:[22,26,28,27,67,87,47,42],
    3:[33,37,35,36,76,56,16,13],
    4:[44,48,46,45,85,65,25,24],
    5:[55,51,53,54,14,34,74,75],
    6:[66,62,64,63,23,43,83,86],
    7:[77,73,71,72,32,12,52,57],
    8:[88,84,82,81,41,21,61,68],
}


@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/num', methods = ['GET'])
def get_num():
    _up = r.randrange(1,9)
    _down = r.randrange(1,9)
    movement = r.randrange(1,7)

    movs = calc_mv()
    result = format_word(_up,_down)
    house,se= calc_gue(_up,_down)
    
    # 로깅
    print("house :",house)
    print("se :",se)
    
    return render_template('hello.html', gues=result, mov=movs)

def calc_gue(u,d):
    strs = int(str(u)+str(d))
    print("strs : ",strs)
    for k, v in datas2.items():
        for j in range(len(v)):
            if v[j] == strs:
                d = k
                se = j+1
    return d,se

def calc_mv():
    return

def format_word(u,d):
    # 하괘 가공
    buf_u = datas.get(u)
    buf1 = buf_u[0:3]

    # 상괘 가공
    buf_d = datas.get(d)
    buf2 = buf_d[2:5]
    
    #로깅
    print("buf1 :",buf1)
    print("buf2 :",buf2)
    
    bufs = buf1+buf2
    print("bufs :",bufs)

    keyword = []
    for i in range(1,7):
        print("i :",i)
        keyword += bufs[-i]
    print("result :",keyword)
    return keyword

if __name__ == '__main__':
    app.run()