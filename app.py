from flask import Flask, render_template

#store society data here for now, maybe store it somewhere else later, or in a file
# societyData = [
#         {'name':"board games club", 'description':"play board games etc etc etc"}
#         {'name':"computing society", 'description':"buncha nerds"}
#         {'name':"esports society", 'description':"also nerds but videogames"}]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)