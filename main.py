import json
from flask import Flask, render_template, request, jsonify, redirect, url_for
from wtforms import Form, DecimalField, SelectField
from wtforms.validators import Required
import os

app = Flask(__name__)

@app.route('/')
def index():
    form = MainForm()
    fields = form._fields
    fields.pop("height")
    fields.pop("weight")
    print fields

    return render_template('index.html', form=form, fields=fields)

@app.route('/', methods=['POST'])
def post():
    inputs = request.form
    weight = float(inputs['weight'])
    height = float(inputs['height'])
    bmi = (weight * 703)/(height**2)
    outputs = {'foo':'bar', 'spam':'eggs', 'TODO':'the algorithm', 'bmi':bmi}
    result_dict = {}
    result_dict['inputs'] = inputs
    result_dict['outputs'] = outputs
    return jsonify(result_dict)

class MainForm(Form):
    height = DecimalField('height', validators=[Required()])
    weight = DecimalField('weight', validators=[Required()])
    ages = [(-1, "Please select your age range"), (0, 'Under 20'), (1, '20-25'), (2, '26-35'), (3, '36-45'), (4, '46-55'), (5, '56-70'), (6, 'Over 70')]
    age = SelectField('what is your age?', choices=ages)
    smoking = SelectField('smoking habits', choices=[(0, 'never'), (1, 'light'), (2, 'frequent')])
    drinking = SelectField('drinking habits', choices=[(0, 'never'), (1, 'light'), (2, 'frequent')])
    substances = SelectField('substance habits', choices=[(0, 'never'), (1, 'light'), (2, 'frequent')])
    familyillness = SelectField('does anyone in your immediate family have a life-threatening illness?', choices=[(-1, 'Please select an option'), (0, 'no'), (1, 'yes')])
    familydiabetes = SelectField('is anyone in your immediate family diabetic?', choices=[(-1, 'Please select an option'), (0, 'no'), (1, 'yes')])
    familyheart = SelectField('is there is a history of heart disease in your family?', choices=[(-1, 'Please select an option'), (0, 'no'), (1, 'yes')])

if __name__ == '__main__':
    # port = int(os.environ.get("POST", 5000))
    app.run(host='0.0.0.0', port=8080)
