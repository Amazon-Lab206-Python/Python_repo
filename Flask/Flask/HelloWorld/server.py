from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
        return render_template('index.html')
@app.route('/', methods =['POST'])
def landing():
        
        return render_template('index.html')

@app.route('/Dojos', methods=['POST'])
def Dojos():
        name = request.form['name']
        location = request.form['location']
        comment = request.form['comment']
        return render_template('Dojos.html', name = name, location = location, comment = comment)
# @app.route('/Dojos')
# def process():
#         return render_template('Dojos.html')

app.run(debug=True)