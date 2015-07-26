import json
from flask import Flask, render_template, request, jsonify
from wtforms import Form, StringField, DecimalField, ValidationError, widgets, SelectField, BooleanField, RadioField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
import os

app = Flask(__name__)

@app.route('/')
def index():
    form = MainForm()
    fields = form._fields
    fields.pop("height")
    fields.pop("weight")
    
    return render_template('index.html', form=form, fields=fields)

@app.route('/', methods=['POST'])
def post():
    inputs = request.form
    outputs = {'foo':'bar', 'spam':'eggs'}
    result_dict = {}
    result_dict['inputs'] = inputs
    result_dict['outputs'] = outputs
    return jsonify(result_dict)
    # json = request.json
    # return jsonify(json)
    # weight = float(request.form['weight'])
    # height = float(request.form['height'])
    # if weight == ''and height == '':
    #     return "You must enter a weight and a height."
    # elif weight == '':
    #     return "You must enter a weight."
    # elif height == '':
    #     return "You must enter a height."
    # else:
    #     bmi = (weight * 703)/(height**2)
    #     # return "You entered " + weight + " and " + height + " and your BMI is " + bmi + "."
    #     return "Your BMI is {0}".format(bmi)

@app.route('/api/results', methods=['POST'])
def api():
    json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4, separators=(',', ': '))


class MainForm(Form):
    height = DecimalField('height', validators=[Required()])
    weight = DecimalField('weight', validators=[Required()])
    smoking = SelectField('smoking habits', choices=[(0, 'never'), (1, 'light'), (2, 'frequent')])
    drinking = SelectField('drinking habits', choices=[(0, 'never'), (1, 'light'), (2, 'frequent')])
    substances = SelectField('substance habits', choices=[(0, 'never'), (1, 'light'), (2, 'frequent')])
    familyillness = SelectField('does anyone in your immediate family have a life-threatening illness?', choices=[(-1, 'Please select an option'), (0, 'no'), (1, 'yes')])
    familydiabetes = SelectField('is anyone in your immediate family diabetic?', choices=[(-1, 'Please select an option'), (0, 'no'), (1, 'yes')])
    familyheart = SelectField('is there is a history of heart disease in your family?', choices=[(-1, 'Please select an option'), (0, 'no'), (1, 'yes')])

if __name__ == '__main__':
    port = int(os.environ.get("POST", 5000))
    app.run(host='0.0.0.0', port=8080, debug=True)
