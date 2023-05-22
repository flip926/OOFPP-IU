from . import habit
from flask import redirect, render_template, request


@habit.route('/',methods=(['GET']))
def index():
    return render_template("index.html")
@habit.route('/analyse')
def analyse():
    return render_template("analyse.html")

@habit.route('/add',methods=["POST"])
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