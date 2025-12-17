from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import mysql.connector
from config.config import dbconfig
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()  

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    
    if request.method == "POST":
        data = request.form  
        user = user_model()
        response = user.user_signup(data)
        # user.close_connection()  # optional
        return response

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    
    if request.method == "POST":
        data = request.form
        user = user_model()
        response = user.user_login(data)

        if response[1] == 200:
            session['user_id'] = response[0].json['user']['id']
            session['email'] = response[0].json['user']['email']

            return render_template("dashboard.html")

        return response

@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("login.html")


class user_model:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host= dbconfig['host'],
                user= dbconfig['user'],
                password= dbconfig['password'],
                database= dbconfig['database'],
                auth_plugin='mysql_native_password')
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Connection Successful :)")
        except Exception as e:
            print("Some Error in Connection of DB :(")
            print(e) 



    def hash_password(self, password):
            # Convert string to bytes
        password_bytes = password.encode('utf-8')
        
        # Generate salt
        salt = bcrypt.gensalt()
        
        # Generate hash
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        
        # Convert bytes back to string for storage
        hash_pass =  hashed_password.decode('utf-8')
        return hash_pass
        
    def user_signup(self, data):
        hashed_pass = self.hash_password(data['password'])
        self.cur.execute(
        "INSERT INTO user_data(username, email, password_hash) VALUES (%s, %s, %s)", (data['username'], data['email'], hashed_pass))

        return render_template("success.html")
    
    def close_connection(self):
        self.cur.close()
        self.con.close()

    def check_password(self, plain_password, hashed_password):
        return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

    def user_login(self, data):
        self.cur.execute("SELECT id, email, username, password_hash FROM user_data WHERE email=%s", (data['email'],))
        user = self.cur.fetchone()

        if not user:
            return render_template("error.html")
        
        is_valid = self.check_password(data['password'], user['password_hash'])

        if not is_valid:
            return render_template("error.html")
        
        return jsonify({
            "message": "Login Successful",
            "user": {
                "id" : user['id'],
                "email" : user['email'],
                "username" : user['username']
            }
        }), 200