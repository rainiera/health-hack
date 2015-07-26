from flask import Flask, render_template, request
import os

app = Flask(__name__)

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
        bmi = (weight * 703)/(height**2)
        # return "You entered " + weight + " and " + height + " and your BMI is " + bmi + "."
        return "Your BMI is {0}".format(bmi)

if __name__ == '__main__':
    port = int(os.environ.get("POST", 5000))
    app.run(host='0.0.0.0', port=8080, debug=True)

