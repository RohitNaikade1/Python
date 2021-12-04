from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
app.config['SECRET_KEY']='0fc697d3c5fdf1bdb0f2ba38'
db=SQLAlchemy(app)


from Market import routes