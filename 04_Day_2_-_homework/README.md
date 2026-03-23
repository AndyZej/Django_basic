## Exercise 1

Imagine a website about movies in the style of IMDB.
You will collect information about movies and people working in film. To do this, define the following objects:

* `Person` containing the following fields:
    * `first_name` string with max length of 32 characters,
    * `last_name` string with max length of 32 characters.
    
* `Genre` containing the following fields:
    * `name` string with max length of 32 characters,
    
* `Movie` i.e. description of the movie, containing the following fields:
    * `title`: string with max length of 128 characters,
    * `director`: foreign key to the `Person` model,
    * `screenplay`: foreign key to the `Person` model,
    * `starring`: Many-to-many relation with the `Person` model. The relation should have an additional field `role` (string of 128 characters, may be null), which is the role the actor plays in the movie, the intermediate table should be named `PersonMovie`,
    * `year`: integer, movie production year,
    * `rating`: float, number from 1.0 to 10.0,
    * `genre` many-to-many relationship with the `Genre` model.

Fill models with data: define some people: directors, writers, actors. Add some movies.


**Hint:**.

You will probably need to add the `related_name` property to the fields `director` and `screenplay`.
Otherwise, if you want to list all movies of a person, django won't know
whether you mean movies in which the person is a director or a writer.

Read more: [https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.related_name](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.related_name)


## Exercise 2

* Write a view that will be available at `/movies/`. It will list the movie titles sorted from newest to oldest, the year of production, director's name, and rating. The movie title should be a link to the URL `/movie-details/{id}/`, id being the movie ID.


## Exercise 3

Write a view that will be available at `/movie-details/{id}/`, id being the movie ID.
The view will retrieve data about the movie from the database (using a model) and display all the information it has about the movie on the page.


## Exercise 4

* Add views:
    * `/persons/` - person list: there should be an edit link next to each person's name.
    The parameter should be passed in the URL. There should be an "add person" link at the bottom of the person list.
    * `/edit-person/{id}/` - edit person: after entering the edit link, the edit person form is displayed.
    You can change and save the data.
    * `/add-person/` - after entering the link "add person", an empty form should be displayed, in which you can add and save a new person. After adding the person properly we should be redirected to the address `/persons`.
 


## Exercise 5

* modify `/movies/` view:
    * next to the movie title add a link to edit the movie, the parameter should be passed in the URL.
    After clicking this link, the program should retrieve the data about this movie from the database, and then show a movie editing form filled with data of the selected movie. The movie can be saved to the database.
    The edit page should be available at `/edit_movie/{id}/`
    * at the bottom of the list of movies add a link "Add movie". After clicking on this link, an empty form should appear for adding a film. The movie can be saved to the database. The edit page should be available at `/add-movie/`.
    After the movie is correctly added to the database, you should be redirected to the address `/movies/`,
