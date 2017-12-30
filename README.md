# Flask MySQL Boilerplate

This is a boilerplate for a Flask app that can run as a virtualenv, Heroku or Docker application.

Make sure you have `python3` installed.

## Local MySQL server using Homebrew
- You can start and stop MySQL by doing `mysql.server start` and stopping with `mysql.server stop`.
- Create the application user and password:
    - Logon to MySQL using root user
    - Create the counter database `CREATE DATABASE counter;`
    - Give privileges to counter user `CREATE USER 'counter_user'@'%' IDENTIFIED BY 'counter_password';`  
    - Create the counter user `GRANT ALL PRIVILEGES ON counter.* TO 'counter_user'@'%';`
- Create a virtualenv: `virtualenv -p python3 venv`
- Activate the virtualenv: `source venv/bin/activate`
- Install the packages: `pip install -r requirements.txt`
- Set up your envvars from the `envvars` file as appropriate for your OS:
    - Copy the contents of `envvars` file into your `~/.bashrc` or
    - You can also use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Quit your terminal and reopen, and do virtualenv activate again, so that envvars are loaded
- Run `python manage.py db init` to create tables
- Run `python manage.py db migrate` and `python manage.py db upgrade`
- Run `gunicorn wsgi:app --bind 0.0.0.0:$PORT --reload`
- Open `http://localhost:5000` on your browser
- Run tests by doing `python tests.py`

## Using Docker
-
