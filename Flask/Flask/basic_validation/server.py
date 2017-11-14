from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'Secrets'
@app.route('/')
def index():
    info = 0
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    info = request.form
    print info
    if len(request.form['name']) < 1:
        flash('need a name homeslice!')
        return redirect('/')
    elif request.form['location'] == 'pick':
        flash('pick a location!')
        return redirect('/')
    elif request.form['language'] == 'pick':
        flash('pick a language!')
        return redirect('/')
    elif len(request.form['description']) > 120:
        flash('Dont be a narcissist!')
        return redirect('/')
    else:
        return render_template('self.html', info = info)
app.run(debug=True)

