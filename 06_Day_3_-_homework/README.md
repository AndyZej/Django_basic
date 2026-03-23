## Exercise 1

Change the `/movies/` view so that:
* at the top of the page there are three buttons for sorting the list of movies by their rating (ascending, descending, or default), after pressing the button the page should refresh, show sorted list of movies, and save to session under key `sorted` the following value:
   * `1` if descending option (highest to lowest rating) is selected,
   * `2` if ascending option (from lowest to highest rating) is selected,
   * `0` if the default option is selected (default sorting by year of production, as in exercise 2),

* after re-entering the page, the list was sorted according to the last selection.


## Exercise 2

Write the view `/search-movie/` under which:

* a form will be visible so that you can search for movies,
the form should contain the following fields (use appropriate values for the attribute `name`):
   * `title` - `name="title"`,
   * `first_name` - `name="first_name"`,
   * `last_name` - `name="last_name"`,
   * `year` - from `name="year_from"` to `name="year_to"`,
   * `genre` - `name="genre"`,
   * `rating` - from `name="rating_from"` to `name="rating_to"`.

* additional requirements:
   * it should be possible to search from-to by year of production,
   * it should be possible to search from-to by movie rating,
   * it should be possible to enter several genres, separated by commas, in the field `genre` and search all movies that are assigned to those genres,
   * after entering a first or last name in the field `person` all movies should be searched, in which the searched person plays a role (is a director, scriptwriter, actor),
   * an empty field in the submitted form should mean "all data",
   i.e. sending a completely empty form should search for all available movies in the database;
   entering the value `Smith` in the field `last_name` and leaving the other fields blank should search for all the films in which any role is played by persons named `Smith`.

Search results should appear on the same page, i.e. `/search-movie/`.
