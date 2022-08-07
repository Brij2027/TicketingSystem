TicketingSystem
A ticketing system for learning purposes

Steps to run:-

clone the repo
install python and venv and activate virutalenv
run the requirements file inside virtualenv
install mongodb either in your localsystem or use atlas
make a .env file in the root of the project and take reference from .env.example
run all migrations [python manage.py migrate]
run the development server [python manage.py runserver]
note:- [the tokens for request are prefixed by "Token" not "Bearer"]
