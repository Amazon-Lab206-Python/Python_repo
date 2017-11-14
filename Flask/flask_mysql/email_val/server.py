 from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = 'Secrets'
@app.route('/')
def index():
    query = 'SELECT * FROM emails'
    emails = mysql.query_db(query)
    print emails
    return render_template('index.html', emails=emails)

@app.route('/email', methods = ['POST'])
def validate():
    if len(request.form['email']) < 1:
        flash('email !blank')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email')
        return redirect('/')
    else:
        query = 'INSERT INTO emails (name, created_at, updated_at) VALUES (:name, NOW(), NOW())'
        data = {
            'name': request.form['email']
        }
        mysql.query_db(query, data)
        
        query = 'SELECT * FROM emails'
        emails = mysql.query_db(query)
        flash('the email that you have entered: ' + request.form['email'] + ' is valid and has been added to the database!')
        return render_template('success.html', emails = emails)
app.run(debug=True)