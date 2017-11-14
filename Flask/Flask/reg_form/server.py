from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'Secrets'
@app.route('/')
def index():
    info = 0
    return render_template('index.html')

# @app.route('/process', methods = ['POST'])
# def process():
    
    
app.run(debug=True)

