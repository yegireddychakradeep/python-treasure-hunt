from flask import request, redirect, url_for,render_template,Response, g

from flask import Flask
from flask import *
import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret key"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
# db = SQLAlchemy(app)

# class table(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     password = db.Column(db.String(12), nullable=False)
#     email = db.Column(db.String(20), nullable=False)



@app.route('/')
def hello():
    session['score']=0
    return render_template('homepage.html')

















@app.route('/login', methods=['POST','GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Validate user's login information
#     user = table.query.filter_by(username=username).first()
    if  (user =="root" and password=="root"):
        return render_template("dashboard.html")
    else:
        
        return render_template('createaccount.html')
    
    
@app.route('/create', methods=['GET','POST'])
def create():
    return render_template('createaccount.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password=request.form['confirm_password']
        email = request.form['email']
#         entry = table(username=username,  password = password, email = email )
#         db.session.add(entry)
#         db.session.commit()
    return render_template('dashboard.html')
        # # Validate the form data
        # if password==confirm_password:
        #     return "Account created"
        # else:
        #     return "passwords do not match"
        # # Insert the data into the database
    


@app.route('/puzzle1',methods=['GET','POST'])
def dashboard():
    
    return render_template('puzzle1.html')



@app.route('/puzzleans1',methods=['POST','GET'])
def puzzleans1():
    answer = request.form['answer']
    if answer.lower() == 'ashwathama':
        session['score'] += 5
        return render_template("puzzle2.html")
    else:
        return render_template("puzzle2.html")


@app.route('/puzzleans2',methods=['POST','GET'])
def puzzleans2():
    answer = request.form['answer2']
    if answer.lower() == 'barbarik':
        session['score'] += 10
        return render_template("puzzle3.html")
    else:
        return render_template("puzzle3.html")
    

@app.route('/puzzleans3',methods=['POST','GET'])
def puzzleans3():
    answer = request.form['answer3']
    if answer.lower() == 'narayanastra':
        session['score'] += 15
    score=session['score']
    if ((score==5) or (score==10) or (score==15) or (score==0)):
        return render_template("bye.html",yourscore=score)
    else:
        return render_template("puzzle4.html")
    

@app.route('/puzzleans4',methods=['POST','GET'])
def puzzleans4():
    answer = request.form['answer4']
    if answer.lower() == 'drona':
        session['score'] += 20
        return render_template("puzzle5.html")
    else:
        return render_template("puzzle5.html")  


    
@app.route('/puzzleans5',methods=['POST','GET'])
def puzzleans5():
    answer = request.form['answer5']
    if answer.lower() == 'shantanu':
        session['score'] += 25
    score=session["score"]
    if ((score==20) or (score==25) ):
        return render_template("bye.html",yourscore=score)
    else:
        return render_template("final.html",yourscore=score)
          

@app.route("/end",methods=["POST","GET"])
def end():
    return render_template("homepage.html")  


@app.route("/end2",methods=["POST","GET"])
def end2():
    return render_template("homepage.html")  

     


if __name__ == '__main__':
    app.run(debug=True)
