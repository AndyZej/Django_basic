## Exercise 1 &ndash; creating a project

Create a fork of the repository. Clone the repository to your computer. Then create a folder **project_1** - the folder should be located in **1_Exercises/Day_1** directory.  
Then in terminal go to the folder and do the following steps:

1. create a virtual environment in the env subdirectory (remember to create the environment for Python version 3)
2. start virtualenv,
3. using the PIP tool, install the Django library,
4. using the **django-admin** tool, create a project
5. run the development server and check if it works (http://127.0.0.1:8000/).


## Exercise 2 &ndash; project configuration

1. using the **manage.py** tool, create a new **django_1** application,
2. add the **exercises_app** application to the **settings.py** file,
3. install the PostgreSQL driver:
    * using PIP tool, install the `psycopg2-binary` package.
4. configure Django to work with a PostgreSQL database:
    * set up a database and include it in the project, name it **exercises**,
    * in the **settings.py** file find the entry `DATABASES` and change it to work with your database:

```python
DATABASES = {
    'default': {
        'NAME': '<here enter database name>',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': '<here enter the name of database user>',
        'PASSWORD': '<here enter the password for the database>',
        'HOST': '127.0.0.1'
    }
}
```

5. perform the first migration,
6. run the development server and check if it works.

Has the project homepage changed? How?


## Exercise 3 - the first page

Based on the example from the presentation, write a page that shows the string `Hello World`. The page should be assigned the address `/hello/`. Remember that the method to be executed should return an object of the `HttpResponse` type.

Hint: you can use the following regular expression to assign the function to the corresponding address:

```
r'^hello/$'
```

You can also use the `path` method, then you won't need to use regular expressions.

## Exercise 4 - second page

Following the example from the presentation, write a page that will show a random number from the range between 0 and 100.
The page should be assigned to the address `/random/`.
The page should display `Drawn number: <drawn number>`, inserting the drawn number in the appropriate place. Remember that the method to be executed should return an object of the `HttpResponse` type.

Hint: you can use the following regular expression to assign the function to the appropriate address:

```
r'^random/$'
```
You can also use the `path` method, then you don't have to use regular expressions.


## Exercise 1 - done with the lecturer

Write a view that is assigned to the address `/random/<max number>/` where `max number` should be a number
(don't worry about validation for now - just take a variable).
This page should show a random number between 0 and the number specified by the user.
The page should display a string: `The user entered the value <max number>. The following number was drawn: <drawn number>`, of course, inserting appropriate variables in the appropriate places.

Hint: The regular expression for the file **urls.py**
```
r'^random/(?P<max_number>(+)/$'
```
You can also use the `path` method, then you won't have to use regular expressions.
```
'random/<int:max_number>/'
```


## Exercise 2

Write a view that is assigned to the address `/random/<min number>/<max number>/` where `min number` and `max number` should be numbers 
(don't worry about validation for now - just take a variable).
This page should show a random number from the range specified by the user.
The page should display the text `The user entered the values <min number> and <max number>. The following number was drawn: <drawn number>`,
of course, inserting appropriate variables in the appropriate places.  
Notice how the views from exercises 1, 2 or 3 (from the previous section) are executed depending on the different number of parameters.

Hint: The regular expression for the file **urls.py**
```
r'^random/(?P<min_number>(¯min_number)+)/(?P<max_number>(¯min_number)+)/$'
```

You can also use the `path` method, then you won't have to use regular expressions.
```
'random/<int:min_number>/<int:max_number>/'
```


## Exercise 3

Write a view that is assigned to the address `/hello/<name>/`, where `name` should be a string
(don't worry about validation for now - just take a variable).
This page should show `hello <name>`, of course, inserting an appropriate variable in the appropriate place.

Hint: The regular expression for the file **urls.py**
```
r'^hello/(?P<name>([A-Za-z])+)/$
```

You can also use the `path` method, then you won't have to use regular expressions.
```
'random/<str:name>/'

```
