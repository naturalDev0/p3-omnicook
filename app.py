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
    
    sql_query = """
                SELECT recipe.id, recipe.recipe_title, recipe.recipe_desc, recipe.recipe_methods, cuisine.cuisine_type, author.author_name
                FROM recipe
                INNER JOIN cuisine ON recipe.cuisine_id=cuisine.id
                INNER JOIN author ON recipe.author_id=author.id
                """
    
    cursor.execute(sql_query)
    recipes = []
    for r in cursor:
        recipes.append(r)
    
    cursor.close()          # Close DB connection
    
    return render_template("index.html", recipes=recipes)

# ROUTE : Add recipe
@app.route('/recipe/add', methods=['GET'])
def add_recipe():
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    # Retrieve data from 'cuisine' table
    sql_query = "SELECT * FROM cuisine"
    cursor.execute(sql_query)
    
    # Store results in a 'cuisines' list
    cuisines = []
    for r in cursor:
        cuisines.append(r)
    
    cursor.close()          # Close DB connection
    
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
    
    # 1 --- Get last row id of ingredient name
    last_ingred_name_ids = []
    for i in recipe_ingred_form:
        print(i)
        sql_query = "INSERT INTO ingredient_name (ingred_name) VALUES ('{}')".format(i)
        cursor.execute(sql_query)
        last_ingred_name_ids.append(cursor.lastrowid)
    
    # 2 --- Get last row id of ingredient
    ingred_ids = []
    for ingredNameId, ingredServe in zip(last_ingred_name_ids, recipe_ingred_serve_form):
        print("i_n: {}, i_s: {}".format(ingredNameId, ingredServe))
        sql_query = "INSERT INTO ingredient (ingred_name_id, ingred_serving) VALUES ('{}','{}')".format(ingredNameId, ingredServe)
        cursor.execute(sql_query)
        ingred_ids.append(cursor.lastrowid)
                
    # 3 --- Create new author
    sql_query = "INSERT INTO author (author_name) VALUES ('{}')".format(recipe_author)
    cursor.execute(sql_query)
    last_author_id = cursor.lastrowid
    
    #### Missing 'recipe_image' for now
    
    # 4 --- Create new recipe
    sql_query = "INSERT INTO recipe (recipe_title, recipe_desc, recipe_methods, cuisine_id, author_id) VALUES ('{}', '{}', '{}', {}, {})".format(recipe_name, recipe_desc, recipe_methods, recipe_cuisine, last_author_id)
    cursor.execute(sql_query)
    last_recipe_id = cursor.lastrowid
    
    # 5 --- Create new relation between recipe and ingredient
    for i in ingred_ids:
        sql_query = "INSERT INTO ingredient_recipe (ingredient, recipe) VALUES ({}, {})".format(i, last_recipe_id)
        cursor.execute(sql_query)
    
    connection.commit()                                     # Committing changes to database
    cursor.close()                                          # Close DB connection
    
    return redirect(url_for('index'))


# ROUTE : Edit recipe
@app.route('/recipe/edit/<recipeId>')
def edit_recipe(recipeId):
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    # 1 --- Retrieve cuisines from 'cuisine' table
    sql_query = "SELECT * FROM cuisine"
    cursor.execute(sql_query)
    cuisines = []
    for r in cursor:
        cuisines.append(r)
    
    # 2 --- Retrieve data from 'recipe' & 'author' tables
    sql_query = """
                SELECT r.id, r.recipe_title, r.recipe_desc, r.recipe_methods, r.cuisine_id, a.author_name
                FROM recipe AS r
                INNER JOIN author AS a ON a.id=r.author_id WHERE r.id=%s
                """
    cursor.execute(sql_query, [recipeId])
    recipe = []
    for r in cursor:
        recipe.append(r)
    
    # 3 --- Retrieve data from 'ingredient_name, ingredient and ingredient_recipe' tables
    sql_query = """
                SELECT ingredName.ingred_name, ingred.ingred_serving
                FROM ingredient_name AS ingredName
                INNER JOIN ingredient AS ingred ON ingred.ingred_name_id=ingredName.id
                INNER JOIN ingredient_recipe AS in_re ON in_re.ingredient=ingred.id
                WHERE in_re.recipe=%s
                """
    cursor.execute(sql_query, [recipeId])
    ingredServe = []
    for i in cursor:
        ingredServe.append(i)
    
    cursor.close()                                          # Close DB connection
    
    return render_template("recipe_edit.html", recipe=recipe, cuisines=cuisines, ingredients=ingredServe)

#  ROUTE : Update recipe
@app.route('/recipe/edit/<recipeId>', methods=['POST'])
def update_recipe(recipeId):
    
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
    
    print("recipe_ingred_form: {}, recipe_ingred_serve_form: {}".format(recipe_ingred_form, recipe_ingred_serve_form))
    
    # 1 --- Retrieve ingredient IDs from 'ingredient_recipe' table
    sql_query = """
                SELECT ingred_id.ingredient
                FROM ingredient_recipe AS ingred_id
                WHERE ingred_id.recipe=%s
                """
    cursor.execute(sql_query, [recipeId])
    ingredId = []
    for i in cursor:
        ingredId.append(i['ingredient'])
    
    # 2 --- Delete ingredients from 'ingredient' table
    for id in ingredId:
        sql_query = "DELETE FROM ingredient WHERE id=%s"
        cursor.execute(sql_query, [id])
    
    # 3 --- Delete ingredient IDs from 'ingredient_recipe' table
    sql_query = "DELETE FROM ingredient_recipe WHERE recipe=%s"
    cursor.execute(sql_query, [recipeId])
    
    # 4 --- Create new and Get last row ID of ingredient names
    last_ingred_name_ids = []
    for i in recipe_ingred_form:
        sql_query = "INSERT INTO ingredient_name (ingred_name) VALUES (%s)"
        print("ingredient: {}".format(i))
        cursor.execute(sql_query, [i])
        last_ingred_name_ids.append(cursor.lastrowid)
    print("last_ingred_name_ids: {}".format(last_ingred_name_ids))
    
    # 5 --- Create new and Get last row ID of ingredients
    ingred_ids = []
    for ingredNameId, ingredServe in zip(last_ingred_name_ids, recipe_ingred_serve_form):
        sql_query = "INSERT INTO ingredient (ingred_name_id, ingred_serving) VALUES (%s, %s)"
        cursor.execute(sql_query, [ingredNameId, ingredServe])
        ingred_ids.append(cursor.lastrowid)
    print("ingred_ids: {}".format(ingred_ids))
    
    # 6 --- Create new relation between recipe and ingredient
    for i in ingred_ids:
        sql_query = "INSERT INTO ingredient_recipe (ingredient, recipe) VALUES (%s, %s)"
        cursor.execute(sql_query, [i, recipeId])
    
    # 7 --- Update recipe
    sql_query = """
                UPDATE recipe AS r
                INNER JOIN author AS a ON r.author_id=a.id
                SET r.recipe_title=%s, r.recipe_desc=%s, r.recipe_methods=%s, r.cuisine_id=%s, a.author_name=%s
                WHERE r.id=%s
                """
    cursor.execute(sql_query, [recipe_name, recipe_desc, recipe_methods, recipe_cuisine , recipe_author, recipeId])
    
    connection.commit()                                     # Committing changes to database
    cursor.close()                                          # Close DB connection
    
    return redirect(url_for('index'))

# ROUTE : View recipe    
@app.route('/recipe/<recipeId>')
def view_recipe(recipeId):
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    # 1 --- Retrieve data from 'recipe, cuisine, author, ingredient_recipe, ingredient and ingredient_name' tables
    sql_query = """
                SELECT r.id, r.recipe_title, r.recipe_desc, r.recipe_methods, c.cuisine_type, a.author_name
                FROM recipe AS r
                INNER JOIN cuisine AS c ON c.id=r.cuisine_id
                INNER JOIN author AS a ON a.id=r.author_id
                WHERE r.id=%s
                """
    cursor.execute(sql_query, [recipeId])
    recipe = []
    for r in cursor:
        recipe.append(r)
    
    sql_query = """
                SELECT ingredName.ingred_name, i.ingred_serving
                FROM ingredient_recipe AS ir
                INNER JOIN ingredient AS i ON i.id=ir.ingredient
                INNER JOIN ingredient_name AS ingredName ON ingredName.id=i.ingred_name_id
                WHERE ir.recipe=%s
                """
    cursor.execute(sql_query, [recipeId])
    ingredName = []
    for i in cursor:
        ingredName.append(i)
    
    cursor.close()                                          # Close DB connection
    
    return render_template("recipe_view.html", recipe=recipe, ingredName=ingredName)

# ROUTE : Delete recipe    
@app.route('/recipe/delete/<recipeId>')
def delete_recipe(recipeId):
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    # 1 --- Retreive recipe from 'recipe' table from selected ID
    sql_query = "SELECT * FROM recipe WHERE id = {}".format(recipeId)
    cursor.execute(sql_query)
    recipeId = cursor.fetchone()
    
    cursor.close()                                          # Close DB connection
    
    return render_template("recipe_delete.html", recipeId=recipeId)

# ROUTE : Confirmed delete recipe
@app.route('/recipe/delete/confirmed/<recipeId>', methods=['POST'])
def confirmed_delete_recipe(recipeId):
    
    connection = connect()                                                  # Connect to DB
    cursor = connection.cursor(pymysql.cursors.DictCursor)                  # Set DB connection
    
    # 1 --- Retrieve ingredient ids from 'ingredient_recipe' table
    getIngredientIds = []
    sql_query = "SELECT ingredient FROM ingredient_recipe WHERE recipe={}".format(recipeId)
    cursor.execute(sql_query)
    for r in cursor:
        getIngredientIds.append(r['ingredient'])
    
    # 2 --- Remove ingredients and serving from 'ingredient' table
    for i in getIngredientIds:
        sql_query = "DELETE FROM ingredient WHERE id={}".format(i)
        cursor.execute(sql_query)
    
    # 3 --- Remove ingredient dependencies from 'ingredient_recipe' table using recipeId
    sql_query = "DELETE FROM ingredient_recipe WHERE recipe={}".format(recipeId)
    cursor.execute(sql_query)
    
    # 4 --- Retrieve author_id from 'recipe' table
    getAuthorId = 0
    sql_query = "SELECT author_id FROM recipe WHERE id = {}".format(recipeId)
    cursor.execute(sql_query)
    getAuthorId = cursor.fetchone()
    authorId = getAuthorId['author_id']
    
    # 5 --- Remove author_name from 'author' table
    sql_query = "DELETE FROM author WHERE id={}".format(authorId)
    cursor.execute(sql_query)
    
    # 6 --- Remove recipe from 'recipe' table
    sql_query = "DELETE FROM recipe WHERE id={}".format(recipeId)
    cursor.execute(sql_query)
    
    connection.commit()                                     # Committing changes to database
    cursor.close()                                          # Close DB connection
    
    return redirect(url_for('index'))

# Boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)