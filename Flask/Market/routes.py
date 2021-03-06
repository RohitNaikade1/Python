from market import app
from flask import render_template
from Market.models import Item
from Market.forms import RegisterForm
@app.route('/')
def home():

    return render_template('home.html')

@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html',items=items)

@app.route('/register')
def register_page():
    form=RegisterForm()
    return render_template('register.html',form=form)