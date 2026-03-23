## Exercise 1

Give all URLs labels (the third argument in the URL definition). Remember that labels should be unique.
(If you are in doubt how to do this, read here:
[https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls](https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls))


## Exercise 2

Change the views so that they refer to labels in the links. 

If you are unsure how to do this, check here:
[https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls](https://docs.djangoproject.com/en/2.2/topics/http/urls/#reverse-resolution-of-urls)


## Exercise 3

Rewrite the views `/persons/` and `/movies/` to meet the following conditions:
* there should be buttons next to each person's name and next to the title of each movie that allow you to delete the person and movie
* buttons should redirect to the following addresses: `/del-person/{id}/` for a person, and `/del-movie/{id}/` for a movie.
* After the correct deletion of a person and a movie, the message `Person deleted!` or `Movie deleted!` should appear on the screen.


## Exercise 4

Make sure the movie page is graphically consistent. There should be a menu on each page to allow easy navigation throughout the page (links to list of people, list of movies, search form)


## Exercise 5 (*)

If you have placed **HTML** code in variables in views, move it to external HTML files.
For more on this, see one of the additional presentations named: **TEMPLATES_WORKSHOP_INTRODUCTION**.
