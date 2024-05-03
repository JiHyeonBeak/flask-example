from flask import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def hello_world():
    return render_template('hello.html')
