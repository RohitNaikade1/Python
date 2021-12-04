from flask import *

app=Flask(__name__)

@app.route("/")
def customer():
    return render_template('customer.html')


@app.route("/success",methods=['POST','GET'])
def success():
    if request.method=='POST':
        result=request.form
        return render_template("result.html",result=result)

if __name__=='__main__':
    app.run(port=5002,debug=True)


