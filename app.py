from flask import Flask, render_template,session,url_for,redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
# importing forms from flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QWERTYUIOWERTYUI'
# initializing the bootstrap
bootstrap = Bootstrap(app)
moment = Moment(app)


"""@app.route('/')
def index():
    return render_template('base.html')
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
            session['name'] = form.name.data
    return redirect(url_for('index'))
return render_template('index.html',)
form = form, name = session.get('name'))

@app.route('/user')
def user():
    return render_template('user.html')


class NameForm(FlaskForm):
    name = StringField('whats your name?', validators=[DataRequired()])
    Lname = StringField('whats your last name?', validators=[DataRequired()])
    submit = SubmitField('submit')
    pass


@app.route('/time', methods=['GET', 'POST'])
def iform():
    name = None
    Lname = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        Lname = form.name.data
        form.name.data = ''
    return render_template('500.html', form=form, name=name)


''''
@app.route('/time')
def time():
    return render_template('500.html', current_time=datetime.utcnow())
'''


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


'''@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
'''

if __name__ == '__main__':
    app.run()
