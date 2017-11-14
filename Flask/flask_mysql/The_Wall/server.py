from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
from flask_bcrypt import Bcrypt 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app) 
mysql = MySQLConnector(app,'thewalldb')
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
    return redirect('/wall')

@app.route('/wall')
def thewall():
    messages_query ='SELECT messages.id, messages.message, concat(users.first_name," ",users.last_name)AS name, messages.created_at AS date FROM thewalldb.messages LEFT JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC'
    messages = mysql.query_db(messages_query)
    comments_query ='SELECT comments.*, users.first_name, users.last_name FROM Comments JOIN users ON users.id = comments.user_id'
    comments = mysql.query_db(comments_query)
    print comments
    return render_template('thewall.html', messages = messages, comments = comments)

@app.route('/login', methods=['POST'])
def login():
    query = 'SELECT * from users WHERE users.email = :email' 
    data ={
        'email': request.form['email']
    }
    # print request.form['email']
    emails = mysql.query_db(query, data)
    password = request.form['password']
    # print emails[0]['email']
    # if len(request.form['email']) < 1:
    #     flash('Please enter an email address')
    # elif not EMAIL_REGEX.match(request.form['email']):
    #     flash('Please enter a valid email address') 
    if emails[0]['email'] != request.form['email']:
        flash('The email')        
        return redirect('/')
    if len(password) < 1:
        flash("please enter a password")
    elif bcrypt.check_password_hash(emails[0]['password'], password): 
        # print session
        # print session['id']
        # messages = mysql.query_db(query, data)
        # query= 'SELECT * FROM thewalldb.messages'
        # data={
        #     'messages': messages
        # }
        flash('Welcome ' + emails[0]['first_name']+ '!')
        print session
        print session['id']
        print emails
        return redirect('/wall')
    else:
        flash('The email and password combo do not match our records')
        return redirect('/')
		# set flash error message and redirect to login page
    # messages = mysql.query_db(query)

@app.route('/post', methods = ['POST'])
def post():
    try:
        session ['id']
    except:
        session['id'] = 3
    print session
    query = 'INSERT INTO thewalldb.messages(user_id, message, created_at) VALUES(:user_id, :message, NOW())'
    data = {
        'message': request.form['message'],
        'user_id': session['id']
    }
    mysql.query_db(query, data)
    print 'wow'
    print 'wow'
    return redirect('/wall')

@app.route('/comment', methods = ['POST'])
def comment():
    # print request.form['message_id']
    # print request.form['comment']
    # print session['id']
    query = 'INSERT INTO thewalldb.comments(user_id, message_id, comment, created_at, updated_at) VALUES(:user_id, :message_id, :comment, NOW(), NOW())'
    data = {
        'user_id': session['id'],
        'message_id': request.form['message_id'],
        'comment': request.form['comment']
    }
    print request.form['comment']
    mysql.query_db(query, data)
    return redirect('/wall')


app.run(debug=True)