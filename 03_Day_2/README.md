## Exercise 1 - done with the lecturer

Look in the `Django 1 - project` directory. You will find there a project named **coderslab**.
* Check the **settings.py** file to make sure everything is configured correctly.
* Create a virtual environment.
* Install the necessary libraries. (You can use the **requirements.txt** file: `pip install -r requirements.txt`)
* Create a database with the appropriate name.
* Perform the migration and start the project.


## Exercise 2 - done with the lecturer

Look in the **exercises_app** application in the **coderslab** project. There you will find a `Band` model that contains information about rock bands. You will find two fields defined there: `name` - band name, and `year` - year the band was formed.

Add the following fields there:
* `still_active`: whether the band is still active. The field should take a boolean type, default value `True`.
* `genre`: integer type field that should take values:
  * -1: not defined,
  * 0: rock,
  * 1: metal,
  * 2: pop,
  * 3: hip-hop,
  * 4: electronic,
  * 5: reggae,
  * 6: other.

The field should take the value -1 by default.

Hint: Use the **choices** parameter. You can find more in the **Snippets** section.

Remember to define all models in the **models.py** file!


## Exercise 3

Create a `Category` model that will store a list of all categories in the CMS. The model should have the following fields:
* `name`: string, max 64 characters,
* `description`: string, unlimited length. May be `null`.


>CMS - Content management system.
>https://en.wikipedia.org/wiki/Content_management_system


## Exercise 4

a. Create a model named `Article` that will store article data in the CMS. The model should have the following fields:

* `title`: string, max. 128 characters,
* `author`: string, max. 64 characters, can take `null`,
* `content`: string, unlimited length,
* `date_added`: datetime field, value to be automatically added when first saved
(hint: `auto_now_add=True`).

b. `Article` model needs a few more fields:

* status, which will take the following values:
    * in writing,
    * pending editor approval,
    * published
    (hint: **choices** attribute),
* publish date (field can be null),
* removal date (field can be null).

Define these properties, choosing field types accordingly.


## Exercise 5

Create a model named `Album` that will store the following values:
* album title,
* release year,
* rating (on a scale of 0-5 stars) (hint: **choices**).

Define these properties, choosing field types accordingly.


## Exercise 1 &ndash; done with the lecturer

In the **exercises_app**, there are a dozen bands in the `Band` model.

* Retrieve the data of all bands.
* Sort them alphabetically.
* Add data for the band Rage Against The Machine, formed in 1991.

Solve the tasks in the interactive console (`python manage.py shell`)

Hint: If you install **ipython** (`pip install ipython`), the shell will color the syntax and suggest commands using the **tab** button.

##### Perform all tasks using Django ORM.


#### Exercise 2

* Find all the bands that do not have a year defined when they were formed. Output in the console both their names and the identifier given by the database.
* Find information about bands that do not have the year of formation in the database.
Fill in the information (can be random) and save it in the database.

##### Use the **django** interactive shell (`python manage.py shell`)

Hint: You can write a function that you then import and call in the django shell.
A regular script won't work because it won't have the database and django application configured.

**For volunteers**: You can write your own command that will be launched from within **manage.py**.

[https://docs.djangoproject.com/en/dev/howto/custom-management-commands/](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)


## Exercise 3

* Complete the band's genres and information whether they are still active.

##### Use the **django** interactive shell (`python manage.py shell`)

Hint: You can write a function that you then import and call in the django shell.
A regular script won't work because it won't have the database and django application configured.

**For volunteers**: You can write your own command that will be launched from within **manage.py**.

[https://docs.djangoproject.com/en/dev/howto/custom-management-commands/](https://docs.djangoproject.com/en/dev/howto/custom-management-commands/)


## Exercise 4

Find and write on the console all bands that:

* have "The" in their name,
* were formed in the 1980s and are still active,
* were formed in the 1970s and have "The" in their name,
* were formed in the 1980s and are no longer active.


## Exercise 5

* Add some selected categories to the `Category` model from the previous section,
* Add some articles to the `Article` model.

Do not add title or content randomly, use the [Random text generator](http://randomtextgenerator.com/).


## Exercise 6

Write a view that you will share at `/articles`, that shows a list of articles.
The list should show the title, author (if any), and the date the article was added to the database.
Select only articles with the status "published".

To do this, in the view retrieve all published articles from the database, and use the `format` method to pass them to a string with the **html** code, which will display the data accordingly.

**For volunteers**:
Instead of writing **html** code in a variable in the view, you can use an external **html** file (a so-called template).
You can find more about this in one of the presentations from this module, or in the official documentation:
[https://docs.djangoproject.com/en/4.0/ref/templates/](https://docs.djangoproject.com/en/4.0/ref/templates/)


## Exercise 1 &ndash; done with the lecturer

* In one of the previous exercises, we created the `Album` model. Now add an appropriate relationship with the `Band` model, so that one band can have multiple albums.

* Add multiple albums to multiple bands (don't look them up on the internet, you can make something up).

* List all the albums of any band in the console.

##### Perform all tasks using Django ORM.


## Exercise 2

Add another model: `Song`. It should have the following fields:
* `title`: string, max length of 128 characters,
* `duration`: time (TimeField), can take null,
* add a many-to-one relationship so that one album can have multiple songs.

Complete the data by creating albums of bands and populating them with songs (the songs don't have to be real, just add any).


## Exercise 3

Extract from the database (and output to the console), using models:

* all the albums by any band,
* all the songs from every album.


## Exercise 4

* Combine `Article` and `Category` so that one article can have multiple categories, and each category can be assigned to multiple articles.
* Add multiple categories to each article.

Hint: You can hook the many-to-many relationship to any model:
* You can add a categories field in the `Article` model
* You can add articles field in the `Category` model.


## Exercise 5

* Select a category. Then select (and list on the console) all articles belonging to that category.
* Select two categories. Then select and list on the console all articles belonging to both categories *at the same time*.


## Exercise 6

* Write a `Person` model that has the following property:
    * `name`,
* Write a `Position` model, which will have the following properties:
    * `position_name`,
    * `salary`,
* Connect those two models with a relationship so that one person can be assigned to exactly one position, and each position has only one employee. Ensure that when a position is deleted, the person assigned to it is also deleted.

Hint:
You have two ways to do this:
- you either add a `person` field in the `Position` model
- or you add a `position` field in the `Person` model

* Add multiple people and positions.


## Exercise 7

Write a view and make it available at `/show-band/{id}/`, **id** being the band identifier.
The view should display information about the music band: its name, genre and year it was formed, and whether it is still active.

To do this, the view has to take the band id as a parameter from the URL, extract the band data using the model, and pass it via a `format` statement to a string with HTML code.

Note that if you added the Band - Album foreign key in exercise 1, you have a field in the `Band` model that stores a list of albums for that band. Show the albums in the template.

**Hint:** use the following regular expression to define the URL:
```
^/show-band/(?P<id>+)/$
```

You can also use the **path** statement, specifying the path in a simpler way:
```
/show-band/<int:id>/
```

**For volunteers**
You can put the **HTML** code in an external file and pass the data using context. You can find more about this in one of the additional presentations **TEMPLATES_INTRODUCTION_TO_WORKSHOPS**.


## Exercise 8 (*)

1. Study the **football** application and check if it is registered in the project.
2. Study the database structure found in the **models.py** file.
3. Perform a migration to add the appropriate tables to the database.
4. In the `management` directory, there is a command that loads sample data into the database.
You can familiarize yourself with the contents of this directory. Run the `python manage.py insert_football_data` command.
5. Create a view named `league_table` that will:
    * pull a league table from the database, sorted by number of points scored,
    * create HTML with the following data:
        * position in the table,
        * club name,
        * number of points,
    * return the result in the browser.
6. Create an entry in the **urls.py** file that will give the application access to the `league_table` view at URL `/table/`.

**Hint:**

To see information about available commands, type:
```
python manage.py help
```
To load data run the command:
```
python manage.py insert_football_data
```
You can read more about custom django commands here: 
[https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/](https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/)


## Exercise 9 (*)
1. Select your favorite football club from the table (e.g. The Fiery Dragons).
2. Create a view named `games_played` that will:
    * extract all the matches the club has played (both home and away) from the table,
    * create HTML with the following data:
        * name of the host club,
        * name of the visiting club,
        * score (e.g. 2:0),
    * return the result in the browser.
3. Create an entry in the **urls.py** file that will give the application access to the `games_played` view at URL `/games/`.

### Hints for exercises 8 and 9

* Use models for database operations.

* You can refer to the materials at the links below. You will learn how to deal with creating models for existing databases:
    * [https://docs.djangoproject.com/en/4.0/ref/django-admin/#inspectdb](https://docs.djangoproject.com/en/4.0/ref/django-admin/#inspectdb)
    * [https://docs.djangoproject.com/en/3.0/howto/legacy-databases/](https://docs.djangoproject.com/en/3.0/howto/legacy-databases/)

* To practice importing data using the above method, you can use the `football_en.sql` file.
The result should be similar to running the migration and using the `insert_football_data` command.
You can create a new django project for this and try to import the database from an existing file.
