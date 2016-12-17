#https://github.com/miguelgrinberg/oreilly-intro-to-flask-video
#
###########################################################

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length



import MySQLdb

application = Flask(__name__)
bootstrap = Bootstrap(application)


class NameForm(Form):
    name = StringField('What is The Server Hostname ?', validators=[Required(),
                                                         Length(1, 16)])
    submit = SubmitField('Enter')


@application.route("/", methods=['GET', 'POST'])

def index():

    name = None
    form = NameForm()  
    if form.validate_on_submit():
     name = form.name.data
    form.name.data = ''

    db = MySQLdb.connect("localhost","ferozkhan","amiferoz69","server")
    cur = db.cursor()
    cur.execute("SELECT * from info where Hostname=name")
    data = cur.fetchall()
    return render_template('index.html', data=data )

if __name__ == "__main__":
   application.run(host='0.0.0.0')
