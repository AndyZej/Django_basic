## Exercise 1

In the exercise, create three views that should have the following functionality:
* The first view should be available at `/set-session/` and set the information in the session under the key ```counter``` to **0**.
* The second view should be available at `/show-session/`, display the contents of the session stored under the key ```counter```, and increment it by **1**. If there is no such data in the session, the page should display appropriate information.
* The third view should be available at `/delete-session/` and delete data from the session (only those stored under key ```counter```).


## Exercise 2

Write a view assigned to the address `/login/`. This view should:
* When accessed using the GET method, display a login form:
```html
<form action="" method="POST">
    <label>
        Name:
        <input type="text" name="name">
    </label>
    <input type="submit">
</form>
``` 
* In the case where POST data is sent to the session under the `loggedUser` key, type the name sent.
* In the case where we enter it via GET method and the session contains information under the `loggedUser` key, display the message `Welcome <name>` - this part of the command requires modification of the code written in the first section.

**Hint:** The view will expect a CSRF token and if it doesn't find one, it will report an error and will not let the user through. To prevent this
(just for the sake of the exercise, CSRF is a pretty effective protection against hacking a website), use the decorator:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**For volunteers:**
You can put the **HTML** code in an external file and pass the data using a context. You can find out more about this in one of the additional presentations **TEMPLATES_INTRODUCTION_TO_WORKSHOPS**.


## Exercise 3

Write a view at the address `/add-to-session/` that will display the following form:  
```html
<form action="#" method="POST">
    <label>
        Key:
        <input type="text" name="key">
    </label>
    <label>
        Value:
        <input type="text" name="value">
    </label>
    <input type="submit">
</form>
  ``` 
When this page is accessed using the POST method, the view should add the submitted value to the session (under an appropriate key).  
Then write a view at `/show-all-session/` that will display in a table all the data in the session (both key and value).

**Hint:** The view will expect a CSRF token and if it doesn't find one, it will report an error and will not let the user through. To prevent this (just for the sake of this exercise, CSRF is a pretty effective protection against hacking a website), use the decorator:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**For volunteers:**
You can put the **HTML** code in an external file and pass the data using context. For more on this, see one of the additional presentations **TEMPLATES_INTRODUCTION_TO_WORKSHOPS**.


## Exercise 4 (*)

* modify the `add_game` view to remember in the session which team was last edited (as host),
* when re-entering the page, read the session variable and set the HTML list to the position corresponding to the last edited team (`<option ... selected>`)


## Exercise 1

Your task is to create three pages:
* The first view, assigned to the address `/set-cookie/`, should set a cookie named ```User``` to your name.
* The second view, assigned to the address `/show-cookie/`, should display the contents of the ```User``` cookie.
If there is no such cookie, it should display appropriate information.
* The third view, assigned to the address `/delete-cookie/`, should delete the cookie named ```User```.


## Exercise 2

Write a view at `/add-to-cookie/` that will display the following form:  
```html
<form action="#" method="POST">
    <label>
        Key:
        <input type="text" name="key">
    </label>
    <label>
        Value:
        <input type="text" name="value">
    </label>
    <input type="submit" name="conversionType">
</form>
  ``` 
When this page is accessed via POST, the view should add the submitted value to cookies (under an appropriate name).  
Then write a view at `/show-all-cookies/` that will display as a table all the data in the cookies you have access to (both cookie name and value).

**Hint:** The view will expect a CSRF token and if it doesn't find it, it will report an error and not let the user through. To prevent this (just for the sake of this exercise, CSRF is a pretty effective protection against hacking a website), use the decorator:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**For volunteers:**
You can put the **HTML** code in an external file and pass the data using context.
You can find more about this in one of the additional presentations **TEMPLATES_INTRODUCTION_TO_WORKSHOPS**.


## Exercise 3(*)

Create a view named `set_as_favourite` (make it available at an appropriate URL) that accepts an ID parameter via GET method, then:
* checks if the ID is a valid number, if not -- displays an error message,
* checks if the ID exists in the database (if a team with that ID exists). If not -- it displays a 404 error,
* if the ID is correct - set a cookie, valid for one year, in which you save the information which team is the user's favorite team.


## Exercise 4(*)

Modify the `league_table` view so that:
* the favorite team is displayed in red (read the cookie value),
* next to each team there is a link "mark as favorite", with a generated corresponding ID, leading to the `/set-as-favourite/` view.


## Exercise 1

Write a class-based view that, when accessed using the `GET` method, displays a form that accepts a name and a surname.
This form should redirect to the same address using the `POST` method.
If the page has been opened by a POST request, the following text should be displayed above the form:
`Welcome, <entered name> <entered surname>`.
You can rewrite the view from exercise 1 of the section **POST forms**.
 


## Exercise 2

Similarly to the previous exercise, rewrite exercise 2 from **POST forms** so that it uses a view **class**.


## Exercise 3

Recall exercise 2 from the **Models** section.
Write the view using a class. After entering by the `GET` method, the user should see a form with data about the band:
* name - band name
* year - year it was formed
* still_active - if it is still active
* genre - a select field

When **Submit** has been clicked, the data should be transferred to the same view using the `POST` method.
Upon entering via **POST** method, capture the form data and add a new band to the database. Then display the following message to the user:

`The band <name> was saved successfully to the database!`,

`<name>` being the name of the band that was added to the database.


## Exercise 4 (*)

Fix the views in the football application so that they were based on classes. Be sure to make appropriate changes to the **urls.py** file.



## Exercise 1

Change the routing for exercises 1-3 from the "Views" section as follows:
* In exercise 1, the variable `max number` must be a number and have 2 to 4 digits,
* In exercise 2, the variable `max number` must be a number and have exactly 4 digits, and the variable `min number` must have exactly 2 digits,
* In exercise 3, the variable `name` must consist of letters only and start with an uppercase letter.
 


## Exercise 2

Fix existing views where parameters are passed via GET so that they are passed in URLs.


## Exercise 3 (*)

* Write a view named `show_team_statistics` that shows:
    * team name,
    * total goals scored,
    * total goals lost,
    * number of home matches,
    * number of away matches.
* define a URL (in the **urls.py** file) that will be built the following way:
```/stats/<team-id>/```, **team_id** being the team ID.

#### Remember that receiving data stored in a URL defined this way is done differently than before!
