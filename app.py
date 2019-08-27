from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql
import urllib.parse
from urllib.parse import urlparse

urllib.parse.uses_netloc.append("mysql")

url = urlparse(os.environ['CLEARDB_DATABASE_URL'])
database = url.path[1:]
username = url.username
password = url.password
host = url.hostname
port = url.port

# Initialize selected DB connection
connection = pymysql.connect(
    host=host,              # IP address of the database; localhost means "the local machine"
    user=username,          #the mysql user
    password=password,      #the password for the user
    database=database,      #the name of database we want to use
    port=port
)

app = Flask(__name__)

# ROUTE : Homepage
@app.route('/')
def index():
    return render_template("index.html")

# ROUTE : Add recipe
@app.route('/recipe/add', methods=['GET'])
def add_recipe():
    
    # Set DB connection
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # Retrieve data from 'allergen' table
    sql_query_1 = "SELECT * FROM allergen"
    cursor.execute(sql_query_1)
    
    # Store results in a 'allergens' list
    allergens = []
    for r in cursor:
        allergens.append(r)
    
    # Retrieve data from 'cuisine' table
    sql_query_2 = "SELECT * FROM cuisine"
    cursor.execute(sql_query_2)
    
    # Store results in a 'cuisines' list
    cuisines = []
    for r in cursor:
        cuisines.append(r)
    
    return render_template("recipe_add.html", cuisines=cuisines, allergens=allergens)
    
@app.route('/recipe/add', methods=['POST'])
def create_add_recipe():
    return render_template("recipe_add.html")


# ROUTE : Edit recipe
@app.route('/recipe/edit')
def edit_recipe():
    return render_template("recipe_edit.html")

# ROUTE : View recipe    
@app.route('/recipe')
def view_recipe():
    return render_template("recipe_view.html")

# ROUTE : Delete recipe    
@app.route('/recipe/delete')
def delete_recipe():
    return render_template("recipe_delete.html")


# Boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)