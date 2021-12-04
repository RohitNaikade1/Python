from flask import *


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/success",methods=['POST'])
def result():
    if request.method=='POST':
        f=request.files['file']
        f.save(f.filename)
        return render_template("result.html",name=f.filename)

if __name__=='__main__':
    app.run(debug=True)