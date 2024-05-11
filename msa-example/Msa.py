from flask import *
import datetime as dt

app = Flask(__name__)

@app.route('/')
def call_sub():
    now = process_date()
    return render_template('main.html',now=now)

def process_date():
    return dt.datetime.now()

@app.route("/shootingdata", methods=['POST'])
def add_data():
    rdata = request.form.get("wrapData")
    return redirect(url_for('call_sub',rdata=rdata))

if __name__ == '__main__':
    app.run()
