from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/')
def he():
    return 'hello again'

@app.route('/addprofile/')
def prof():
    return render_template('myProfile.html')
#Create mapping /addprofile/
@app.route('/profile/')
def pro():
    nm=request.args.get("nm")
    resi=request.args.get("resi")
    em = request.args.get("em")
    password = request.args.get("password")
    dob = request.args.get("dob")
    # male = request.args.get("Male")
    # female = request.args.get("Female")
    return render_template('html.html',name_html=nm,resi_html=resi,email_html=em,password_html=password,dob_html=dob)

if __name__ == '__main__':
    app.run(debug=True)
