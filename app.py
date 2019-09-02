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
@app.route('/', methods=['GET'])
def index():
    
    # Connect to DB
    connection = connect()
    
    # Set DB connection
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql_query = "SELECT recipe.id, recipe.recipe_title, recipe.recipe_desc, recipe.recipe_methods, cuisine.cuisine_type, author.author_name FROM recipe INNER JOIN cuisine ON recipe.cuisine_id=cuisine.id INNER JOIN author ON recipe.author_id=author.id"
    
    cursor.execute(sql_query)
    recipes = []
    for r in cursor:
        recipes.append(r)
    # print(recipes)
    
    # sql_query = "SELECT cuisine_type FROM cuisine WHERE id= {}".format(recipes['cuisine_id'])
    # cursor.execute(sql_query)
    
    cursor.close()
    
    return render_template("index.html", recipes=recipes)

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
    
    # Get form values ...
    recipe_name = request.form.get('recipeName')                            # Recipe name
    recipe_desc = request.form.get('recipeDesc')                            # Recipe description
    recipe_methods = request.form.get('recipeMethods')                      # Recipe methods
    recipe_ingred_form = request.form.getlist('ingred-name[]')              # Array : Recipe ingredients
    recipe_ingred_serve_form = request.form.getlist('ingred-serve[]')       # Array : Recipe ingredient's serving
    recipe_author = request.form.get('recipeAuthor')                        # Recipe author
    recipe_cuisine = request.form.get('recipeCuisine')                      # Recipe cuisine
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    # Get last row id of ingredient name
    last_ingred_name_ids = []
    for i in recipe_ingred_form:
        print(i)
        sql_query = "INSERT INTO ingredient_name (ingred_name) VALUES ('{}')".format(i)
        cursor.execute(sql_query)
        last_ingred_name_ids.append(cursor.lastrowid)
    print("IngredNameIds: {}".format(last_ingred_name_ids))
    
    # Get last row id of ingredient
    ingred_ids = []
    for ingredNameId, ingredServe in zip(last_ingred_name_ids, recipe_ingred_serve_form):
        print("i_n: {}, i_s: {}".format(ingredNameId, ingredServe))
        sql_query = "INSERT INTO ingredient (ingred_name_id, ingred_serving) VALUES ('{}','{}')".format(ingredNameId, ingredServe)
        cursor.execute(sql_query)
        ingred_ids.append(cursor.lastrowid)
                
    #  Create new author
    sql_query = "INSERT INTO author (author_name) VALUES ('{}')".format(recipe_author)
    cursor.execute(sql_query)
    last_author_id = cursor.lastrowid
    
    #### Missing 'recipe_image' for now
    sql_query = "INSERT INTO recipe (recipe_title, recipe_desc, recipe_methods, cuisine_id, author_id) VALUES ('{}', '{}', '{}', {}, {})".format(recipe_name, recipe_desc, recipe_methods, recipe_cuisine, last_author_id)
    cursor.execute(sql_query)
    last_recipe_id = cursor.lastrowid
    
    # Create new relation between recipe and ingredient
    for i in ingred_ids:
        sql_query = "INSERT INTO ingredient_recipe (ingredient, recipe) VALUES ({}, {})".format(i, last_recipe_id)
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
@app.route('/recipe/delete/<recipeId>')
def delete_recipe(recipeId):
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    sql_query = "SELECT * FROM recipe WHERE id = {}".format(recipeId)
    cursor.execute(sql_query)
    recipeId = cursor.fetchone()
    print(recipeId)
    
    return render_template("recipe_delete.html", recipeId=recipeId)

# ROUTE : Confirmed delete recipe
@app.route('/recipe/delete/confirmed/<recipeId>', methods=['POST'])
def confirmed_delete_recipe(recipeId):
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    # Retrieve ingredient ids from ingredient_recipe
    getIngredientIds = []
    sql_query = "SELECT ingredient FROM ingredient_recipe WHERE recipe={}".format(recipeId)
    cursor.execute(sql_query)
    for r in cursor:
        getIngredientIds.append(r['ingredient'])
    
    # Remove ingredients and serving from ingredient    
    for i in getIngredientIds:
        sql_query = "DELETE FROM ingredient WHERE id={}".format(i)
        cursor.execute(sql_query)
    
    # Remove ingredient dependencies from ingredient_recipe using recipeId
    sql_query = "DELETE FROM ingredient_recipe WHERE recipe={}".format(recipeId)
    cursor.execute(sql_query)
    
    # Retrieve author id from recipe
    getAuthorId = 0
    sql_query = "SELECT author_id FROM recipe WHERE id = {}".format(recipeId)
    cursor.execute(sql_query)
    getAuthorId = cursor.fetchone()
    authorId = getAuthorId['author_id']
    
    # Remove author from author
    sql_query = "DELETE FROM author WHERE id={}".format(authorId)
    cursor.execute(sql_query)
    
    # Lastly, Remove recipe from recipe
    sql_query = "DELETE FROM recipe WHERE id={}".format(recipeId)
    cursor.execute(sql_query)
    
    # Committing changes to database
    connection.commit()
    
    # Close connection
    cursor.close()
    
    return redirect(url_for('index'))

# Boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)