from flask import *

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/test')
def call_sub():
    return render_template('sub.html')

def process_data():
    return
