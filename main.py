from flask import Flask, render_template, request
import redis
app = Flask(__name__)
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    text = request.form['hi']
    print request.form
    r.set('input', text)
    return "You entered \"" + text + "\"."

if __name__ == '__main__':
    app.run(debug=True)
