from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'oops'

@app.route('/')
def root():
    if not 'counter' in session:
        session['counter'] = 0

    # try:
    #     session['counter']
    # except:
    #     session['counter'] = 0
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def count():
    session['counter'] += 1 
    return redirect('/')

app.run(debug=True)