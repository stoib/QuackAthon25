from flask import Flask, render_template
from society_data import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/societies/<int:society_id>')
def society_detail(society_id):
    
    society = getSocietyById(society_id)

    if (society != "NULL"): 
        return render_template('society.html', society=society)
    else:
        return render_template('no_society.html')
    

@app.route('/societies')
def society_list():
    return render_template("societies.html", societyData=societyData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)