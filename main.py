from flask import Flask, render_template, request
import redis
app = Flask(__name__)
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    if weight == ''and height == '':
        return "You must enter a weight and a height."
    elif weight == '':
        return "You must enter a weight."
    elif height == '':
        return "You must enter a height."
    else:
        print request.form
        print type(weight)
        print type(height)
        bmi = (weight * 703)/(height**2)
        print type(bmi)
        r.set('rw', weight)
        r.set('rh', height)
        r.set('rbmi', bmi)

        # return "You entered " + weight + " and " + height + " and your BMI is " + bmi + "."
        return "Your BMI is {0}".format(bmi)

if __name__ == '__main__':
    app.run(debug=True)
    