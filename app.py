from flask import Flask, render_template
from timetable import *


app = Flask(__name__)


@app.route('/timetable/<int:student_id>')
def timetable_detail(student_id):
    timetable = getTimeTableById(student_id)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

