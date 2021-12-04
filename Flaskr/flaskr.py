import sqlite3
from flask import *


app = Flask(__name__)

app.config['SECRET_KEY']='dev'
@app.route("/")
def showEntries():
    conn=sqlite3.connect("entries.db")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute("select * from records")
    rows=cur.fetchall()
    return render_template("show_entries.html",entries=rows)

@app.route("/adminpage")
def adminpage():
    if not session.get('logged_in'):
        redirect(url_for('loginPage'))
    return render_template("admin.html")
    
@app.route("/add",methods=['POST'])
def  adminPanel():
    
    with sqlite3.connect("entries.db") as con:
        cur=con.cursor()
        title=request.form['title']
        text=request.form['text']
        cur.execute("insert into entries (title,text) values(?,?) ",(title,text))
        # cur.execute("INSERT into emp (name, email, address) values (?,?,?)",(name,email,address))  
        con.commit()
    return redirect(url_for('showEntries'))


@app.route("/loginPage")
def loginPage():
    return render_template("login.html")

@app.route("/login",methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!= 'rohit@gmail.com':
            error='Invalid username'
        elif request.form['password']!='admin':
            error='Invalid password'
        else:
            session['logged_in']=True
            flash('You are logged in')
            return redirect(url_for('adminpage'))
    return render_template('login.html',error=error)

@app.route("/logout")
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('showEntries'))
if __name__ == '__main__':
    app.run(port=5001,debug=True)