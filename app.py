from flask import Flask, render_template
from society_data import *
from timetable import *
from student import *
from data_collator import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/timetable/<int:student_id>')
def timetable_detail(student_id):
    timetable = compileTimesForStudent(student_id)
    #print(timetable)
    if (timetable != "NULL"):
        return render_template("timetable.html", timetable=timetable)
    else:
        return render_template('no_timetable.html')

@app.route('/societies/<int:society_id>')
def society_detail(society_id):
    
    society = getSocietyById(society_id)

    if (society != "NULL"): 
        return render_template('society.html', society=society)
    else:
        return render_template('no_society.html')
    

@app.route('/societies')
def society_list():
    allSocs = getFullSocietyData()
    return render_template("societies.html", allSocs=allSocs)

@app.route('/timetable')
def timetable():
    return render_template("timetable_pick.html")

@app.route('/student-info')
def student():
    render_template("student.html")

@app.route('/student-info/<int:student_id>')
def student_details(student_id):
    student = getStudentById(student_id)

    if (student != "NULL"):
        return render_template("student.html", student=student)
    else:
        return render_template('no_student.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
