from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql

app = Flask(__name__)

# Initialize selected DB connection
# connection = pymysql.connect(
#     host='localhost', # IP address of the database; localhost means "the local machine"
#     user="admin",  #the mysql user
#     password="password", #the password for the user
#     database="Chinook" #the name of database we want to use
# )

@app.route('/')
def index():
    return "Hello World!"

# Boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)