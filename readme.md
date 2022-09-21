

pipenv install django : install virtua env for Django
pipenv shell   : to activate virtual env for the project
python manage.py runserver <port optional> : run the project


|django-admin| 
django-admin: will print commands to use.

|python manage.py|
you can see similar commands as django-admin. so we could run the server python manage.py runserver.


ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?


For Project, we want to python interpretor (virtual) inside our project rather than installed Python3 on Mac. 

todo: 
VSCode->view->command palette -> type python interpretor
it shows default python path:

on terminal: pipenv --venv
it will create virtual interpretor path: 
/Users/lukekim/.local/share/virtualenvs/DjangoProject-dxtLzAUt

- add (/bin/python) at the end.
then, select enter Interpretor at command palett, then past. 
then, reopen the terminal. it prints the new virtual interpretor activation msg. 

To create app in main project:
open an new terminal while the main server is running. then run
python manage.py startapp |app name| 

Then to register a new app in setting.py module. add
'app name' 

## Views (res, req handler)
req, res
 takes request -> return response ==> it is a request handler 
 in js, view is html, but in python, view is action not the ui view
## create urls.py in new app
we create and config a new app's url, then register it into main app's url.py 
routing is same as node js routing

## template (ui rendering)
add a directory as template -> hello.html 





