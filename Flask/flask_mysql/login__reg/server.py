from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app) 
mysql = MySQLConnector(app,'usersdb')
app.secret_key = 'Secrets'
@app.route('/')
def index():
    query = 'SELECT * FROM users'
    emails = mysql.query_db(query)
    
    return render_template('index.html', emails=emails)

@app.route('/register', methods = ['POST'])
def register():
    query = 'SELECT * from users WHERE users.email = :email'
    data ={
        'email': request.form['email']
    }
    emails = mysql.query_db(query, data)
    # print emails
    if len(request.form['email']) < 1:
        flash('Please enter an email address')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Please enter a valid email address') 
    elif len(emails) !=0 :
        flash('Duplicate!')
        return redirect('/')   
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        flash( 'Please enter a valid name')
    if len(request.form['password']) < 8:
        flash('Please enter a longer password')
    if request.form['confirm_password'] != request.form['password']:
        flash('Password confirmations do not match')
        return redirect('/')   
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    query = 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())'
    data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    # print data
    mysql.query_db(query, data)
    flash ('Thank you for registering, Enjoy!')
    return render_template('/login.html')

@app.route('/login', methods=['POST'])
def login():
    query = 'SELECT * from users WHERE users.email = :email' 
    data ={
        'email': request.form['email']
    }
    print request.form['email']
    emails = mysql.query_db(query, data)
    password = request.form['password']
    print emails[0]['email']
    # if len(request.form['email']) < 1:
    #     flash('Please enter an email address')
    # elif not EMAIL_REGEX.match(request.form['email']):
    #     flash('Please enter a valid email address') 
    if emails[0]['email'] != request.form['email']:
        flash('The email and password ')
        
        return redirect('/')
    if len(password) < 1:
        flash("please enter a password")
    elif bcrypt.check_password_hash(emails[0]['password'], password): 
        flash('welcome!')
        return render_template('/login.html')
    else:
        flash('The email and password combo do not match our records')
        return redirect('/')
    return render_template('/login.html')
		# set flash error message and redirect to login page


app.run(debug=True)