from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # 任意の秘密鍵

class BMIForm(FlaskForm):
    height = FloatField('身長を入力してください(例：1.7m)', validators=[DataRequired()])
    weight = FloatField('体重を入力してください(例：70kg)', validators=[DataRequired()])
    submit = SubmitField('BMIを計算する')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = BMIForm()
    bmi = None
    if form.validate_on_submit():
        height = form.height.data
        weight = form.weight.data
        bmi = weight / ( height ** 2)  # BMIを計算
    return render_template('index.html', form=form, bmi=bmi)

if __name__ == '__main__':
    app.run()
