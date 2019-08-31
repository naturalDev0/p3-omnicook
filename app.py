from flask import Flask, render_template, request, redirect, url_for
import os
import pymysql
# import urllib.parse
# from urllib.parse import urlparse

# urllib.parse.uses_netloc.append("mysql")

# url = urlparse(os.environ['CLEARDB_DATABASE_URL'])
# database = url.path[1:]
# username = url.username
# password = url.password
# host = url.hostname
# port = url.port

# Initialize selected DB connection
# connection = pymysql.connect(
#     host=host,              # IP address of the database; localhost means "the local machine"
#     user=username,          #the mysql user
#     password=password,      #the password for the user
#     database=database,      #the name of database we want to use
#     port=port
# )

def connect():
    connection = pymysql.connect(
        host="localhost",               # IP address of the database; localhost means "the local machine"
        user="admin",                   # the mysql user
        password="n0tY0urP@55w0rd",     # the password for the user
        database="cookbook"             # the name of database we want to use
    )
    return connection

app = Flask(__name__)

# ROUTE : Homepage
@app.route('/')
def index():
    return render_template("index.html")

# ROUTE : Add recipe
@app.route('/recipe/add', methods=['GET'])
def add_recipe():
    
    # Connect to DB
    connection = connect()
    
    # Set DB connection
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    # Retrieve data from 'cuisine' table
    sql_query = "SELECT * FROM cuisine"
    cursor.execute(sql_query)
    
    # Store results in a 'cuisines' list
    cuisines = []
    for r in cursor:
        cuisines.append(r)
    
    cursor.close()
    
    return render_template("recipe_add.html", cuisines=cuisines)
    
@app.route('/recipe/add', methods=['POST'])
def create_add_recipe():
    
    recipe_name = request.form.get('recipeName')
    # print("recipe title: {}".format(recipe_name))
    recipe_desc = request.form.get('recipeDesc')
    recipe_methods = request.form.get('recipeMethods')
    recipe_ingred = request.form.get('ingred-name-1')
    recipe_ingred_serve = request.form.get('ingred-serve-1')
    recipe_author = request.form.get('recipeAuthor')
    recipe_cuisine = request.form.get('recipeCuisine')
    
    # Connect to DB
    connection = connect()
    
    # Set DB connection
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql_query = "INSERT INTO ingredient_name (ingred_name) VALUES ('{}')".format(recipe_ingred)
    cursor.execute(sql_query)
    last_ingredName_rowId = cursor.lastrowid
    # print("lastrowid: %d" % last_ingredName_rowId)
    
    sql_query = "INSERT INTO ingredient (ingred_name_id, ingred_serving) VALUES ({},'{}')".format(last_ingredName_rowId, recipe_ingred_serve)
    cursor.execute(sql_query)
    last_ingred_rowId = cursor.lastrowid
                
    sql_query = "INSERT INTO author (author_name) VALUES ('{}')".format(recipe_author)
    cursor.execute(sql_query)
    last_author_id = cursor.lastrowid
    
    # Missing 'recipe_image' for now
    sql_query = "INSERT INTO recipe (recipe_title, recipe_desc, recipe_methods, cuisine_id, author_id) VALUES ('{}', '{}', '{}', {}, {})".format(recipe_name, recipe_desc, recipe_methods, recipe_cuisine, last_author_id)
    # print("{} {} {} {} {} {} {}".format(recipe_name, recipe_desc, recipe_methods, recipe_ingred, recipe_ingred_serve, recipe_author, recipe_cuisine))
    cursor.execute(sql_query)
    last_recipe_id = cursor.lastrowid
    
    sql_query = "INSERT INTO ingredient_recipe (ingredient, recipe) VALUES ({}, {})".format(last_ingred_rowId, last_recipe_id)
    cursor.execute(sql_query)
    
    connection.commit()
    cursor.close()
    
    return redirect(url_for('index'))


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