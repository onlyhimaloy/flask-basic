#https://github.com/miguelgrinberg/oreilly-intro-to-flask-video
#
###########################################################

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
from flask_mysqldb import MySQL

application = Flask(__name__)



application.config['SECRET_KEY'] = 'top secret!'
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferozkhan:amiferoz69@localhost/server'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
bootstrap = Bootstrap(application)
db = SQLAlchemy(application)




class NameForm(Form):
    name = StringField('What is The Server Hostname ?', validators=[Required(),
                                                         Length(1, 16)])
    submit = SubmitField('Enter')


class info(db.Model):
    __tablename__ = 'info'
       # return '<User {0}>'.format(self.name)
    P_Id = db.Column(db.Integer, primary_key=True)

@application.route("/", methods=['GET', 'POST'])

    name = None  
    form = NameForm()
    if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
    info.query.filter_by(Hostname=name).all():
            
    return render_template('index.html', form=form, name=name, data=data )

if __name__ == "__main__":
   application.run(host='0.0.0.0')
