from flask import Flask,redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import create_app
app =create_app()





#Routes

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/analyse')
def analyse():
    return render_template("analyse.html")

#Route for adding habits to the database

@app.route('/add',methods=["POST"])
def add_habit():
    name = request.form.get("name")
    periodicity = request.form.get("periodicity")
    if name !='' and periodicity!='':
        #submission = Habit(name=name,periodicity=periodicity)
        #db.session.add(submission)
        #db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)