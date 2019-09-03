# <a href="https://omnicook-tl.herokuapp.com/" target="_blank">Omnicook</a>

Code-Institute Project #3 : An cookbook project that shows different varieties of recipe for hobbyist to get inspirations and ideas to jumpstart them in learning how to cook and make delicious form of dishes.
 
 
## UI / UX

### Interface
1. You can refer to the initial UI through [here](https://drive.google.com/file/d/15hE_VO6VaOnUheitaI-4sei5_7XlH8Kt/view?usp=sharing).
    * NOTE: *The existing UI/UX has been changed.*
 
### Experience
User Stories: --> <i>(e.g. As a user type, I want to perform an action, so that I achieve a goal.)</i>

*As a user...*
1. I want to filter recipes by name, so that I can easily find the recipe with the name in mind.
1. I want to filter recipes by cuisine, so that I can search for other interesting recipes as well.
1. I want to edit recipe, so that I can make amendments when I changed my mind.
1. I want to delete recipe, so that I can remove them when they are no longer needed.
1. I want to view recipes individually, so that I can focus on the contents.
1. I want to upload recipe image, so that I can make the recipe card with familiarity.

### Database Schema

*ER Diagram*

![alt text](/documents/p3_omnicook_er-diagram.png "omnicook_er-diagram")

*Actual model*

![alt text](/documents/p3_omnicook_db-model.png "omnicook_db-model")


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

<i>Users can ...</i>

* Feature #1 - Create new recipe
* Feature #2 - View recipe individually
* Feature #3 - View several recipes on home page
* Feature #4 - Delete selected recipe
* Feature #5 - Update and Delete recipe

### Features Left to Implement
* Feature #1 - Filter search results of *'recipe'* table
* Feature #2 - Check and delete ingredient names inside *'ingredient_name'* table to maintain data integrity
* Feature #3 - Upload images along with the desired recipe
<br/>

## Technologies Used

1. HTML5 --- *required*
1. CSS3 --- *required*
    1. Import Google Font CDN and style certain HTML components
    1. Add in @media (media queries) to control element size when screen size changed
1. JavaScript --- *required*
    * Add in certain functions such as (e.g. click, ready, on ...),
        * Dynamically generate HTML elements
        * Components such as ...
            1. *append()*        - Add in element into selector
            1. *children()*      - Point to the children HTML element of the parent selector
            1. *last()*          - Point to the last children HTML element of the parent selector
            1. *attr()*          - Use it to retreive id HTML element
            1. *val()*           - Retrieve the value of the HTML element
1. [Bootstrap 4.3](https://getbootstrap.com/)
    * Speed up website building through simple ready made components
    * Components used ...
        1. *form-group*          - Individual form group components that managed 
        1. *form-row*            - Form rows 
        1. *container*           - A box that has formatted paddings that centralized contents in the middle of the webpage
        1. *container-fluid*     - A box that takes up the whole width of the webpage.
        1. *...*

1. [JQuery](https://jquery.com)
    * Manipulate HTML selectors.

1. [Python 3.6.8](https://docs.python.org/3.6/)
    * Back-end language that helps to link front-end data to DB.
    * Components used (some)...
        1. *Function*
        1. *list [ ]*            - Act like an array, to temporarily store values
        1. *append()*            - Insert new values into list
        1. *...*
        
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * Developed dynamic web link routes. An micro framework.

1. [MySQL](https://www.mysql.com/)
    * The database framework is used in this project.

1. [ClearDB](https://w2.cleardb.net/)
    * *This is required to deploy on Heroku as they don't support MySQL on the platform.*


## Testing

<i>These are the tests I have done so far...</i>

### Manual Test
1. Add Recipe (recipe_add.html) --- Steps
    1. *Select 'Add Recipe' button on home page ('index.html')*
    1. *Key in desire values into fields*
    1. *Select 'Submit Recipe' button to submit the recipe*
    1. *User is directed to index*
    1. *Recipe is displayed on the page*

1. Edit Recipe (recipe_edit.html) --- Steps
    1. *Select 'View' button on the desired recipe*
    1. *Select 'Edit' button to edit recipe*
    1. *Update the fields with the desired values*
    1. *Select 'Submit Recipe' button to update the recipe*
    1. *User is direct to index*
    1. *Changes is reflected on the recipe card* 

1. Delete Recipe (recipe_delete.html) --- Steps
    1. *Select 'View' button on the desired recipe*
    1. *Select 'Delete' button to be directed delete confirmation page*
    1. *Select 'Delete' button to delete the recipe*
    1. *Otherwise, revert back to index homepage*

1. Read Recipe items (recipe_view, recipe_add, recipe_edit, recipe_delete) --- Steps
    * *This function appears is commonly used in several pages*

### Missing Tests
*Due to time constraints ... These are the features with tests I have yet to implement*

1. Form validations
    * Currently the form has no validations, users can freely type any desired values into fields.
1. Data integrity
    * *"ingredient_name"* table data will keep stacking up as currently it does not have logics in Back-End to ensure zero duplications.

<br/>


## Deployment

<i>[Please take note that your project environment will be different ...]</i>

* The website is currently hosted on Heroku, developed on AWS Cloud 9 IDE platform and the source code is stored on Github Repository. Occasionally, I would perform some lightweight code edits using Microsoft Visual Studio (VS) Code (e.g. README.md).

### Steps deployment

1. Create a new repository for your project on your local computer.
    ```
    git init .                  // initialize repo with all files
    git add .                   // add all files into local staging
    git status                  // check if any files are left out before commiting
    git commit -m "message"     // commit change with message of your files into repo
    ```
2. Add your remote git link for uploading your files onto Github later on.
    ```
    // add your remote repo link
    git remote add origin https://github.com/naturalDev0/p3-omnicook.git
    ```
3. Push your files onto your remote
    ```
    // upload your files into your remote repo
    git push -u origin master
    ```

4. Should you have the interest to work the files offline, you can do so by cloning a copy.
    ```
    // Clone the selected repo offline
    git clone https://github.com/naturalDev0/p3-omnicook.git
    ```

    NOTE: All commits are pushed to master branch, as currently there is no intention of creating new branches.
<br/><br/>

### Additional packages to install
1. Flask
    ```
    pip3 install Flask          // Install Flask package to get started
    ```
1. PyMySQL
    ```
    pip3 install pymysql        // Install PyMySQL to coding CRUD with MySQL
    ```
<br/>

## Credits

### Acknowledgements

*I have took inspirations from the following sites...*

Misc
1. [Google Fonts](https://fonts.google.com/) - (Font)
2. [Bytesize Icons](https://github.com/danklammer/bytesize-icons) - (Icons)

Image
1. [unsplash - brooke lark](https://unsplash.com/photos/4J059aGa5s4)
    * Image has been shrinked to width: 512px, height: 341px

Web layout
1. [kinokuniya](https://kinokuniya.com.sg/)
1. [justonecookbook](https://www.justonecookbook.com/)
1. [popular](https://www.popular.com.sg/)

Web layout, Fields to implement in DB
1. [allrecipes](https://www.allrecipes.com/)
1. [foodnetwork](https://www.foodnetwork.com/)
1. [bbcgoodfood's cuisines](https://www.bbcgoodfood.com/recipes/category/cuisines)
    * Idea on the ‘Type of cuisines’

<br/>

***This project is for educational use. Thank you for your understanding.***