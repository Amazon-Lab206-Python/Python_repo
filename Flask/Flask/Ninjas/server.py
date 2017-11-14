from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def turtle(color):
    return render_template('colors.html', color_name = color)

app.run(debug=True)