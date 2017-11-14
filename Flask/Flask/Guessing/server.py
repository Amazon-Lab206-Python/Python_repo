from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'oops'

@app.route('/')
def root():
    try:
        session['winner']
    except:
        session['winner'] = random.randint(1,100)
    print session['winner']
    print type(session['winner'])
    return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
    session['myguess'] = request.form['myguess']
    session['myguess'] = int(session['myguess'])
    # myguess = int(myguess)
    print type(session['myguess'])
    return render_template('guess.html',myguess=session['myguess'])
    
app.run(debug=True)