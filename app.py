from flask import Flask, render_template

#store society data here for now, maybe store it somewhere else later, or in a file
societyData = [
        {'id':1, 'name':"boardgames", 'description':"play board games etc etc etc"},
        {'id':2, 'name':"computing", 'description':"buncha nerds"},
        {'id':3, 'name':"esports", 'description':"also nerds but videogames"}
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<int:society_id>')
def society_detail(society_id):
    society = societyData.get(society_id)

    if society is None:
        return render_template('no_society.html')

    return render_template('society.html', society=society)

@app.route('/societies')
def society_list():
    return render_template("societies.html", societyData=societyData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)