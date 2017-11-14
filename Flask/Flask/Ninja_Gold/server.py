from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'oops'

@app.route('/')
def root():
    if not 'money' in session:
        session ['money'] = 0

    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def money():
    if request.form['building'] == 'farm':
        addmoney = 0
        addmoney = random.randint(10,20)
        session['money'] += addmoney
        return redirect('/')
    elif request.form['building'] == 'cave':
        addmoney = 0
        addmoney = random.randint(5,10)
        session['money'] += addmoney
        return redirect('/')
    elif request.form['building'] == 'house':
        addmoney = 0
        addmoney = random.randint(2,5)
        session['money'] += addmoney
        return redirect('/')
    elif request.form['building'] == 'casino':
        if random.randint(1,4) == 4:
            addmoney = 0
            addmoney = random.randint(0,50)
            session['money'] += addmoney
            return redirect('/')
        else:
            addmoney = 0
            addmoney = random.randint(0,50)
            session['money'] -= addmoney
            return redirect('/')
    else:
        session['money'] = 0
        return redirect('/')
    
app.run(debug=True)