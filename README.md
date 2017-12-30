# Flask MySQL Boilerplate

This is a boilerplate for a Flask app that can run as a virtualenv, Heroku or Docker application.

Make sure you have `python3` and `virtualenv` installed.

## Local MySQL server
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
- Run `python manage.py db init` to initialize migrations
- Run `python manage.py db migrate` and `python manage.py db upgrade` to create tables
- Run `python manage.py runserver`
- Open `http://localhost:5000` on your browser
- Run tests by doing `python tests.py`

## Using Docker
- Run `docker-compose up`
- In a new terminal or tab run:
    - `docker exec -it counterappmysql_web_1 python manage.py db init` to initialize migrations
    - `docker exec -it counterappmysql_web_1 python manage.py db migrate` and `docker exec -it counterappmysql_web_1 python manage.py db upgrade` to create tables
- Open `http://localhost:5000` on your browser
- Run tests by doing `docker exec -it counterappmysql_web_1 python tests.py`

## Production
- Use Gunicorn `gunicorn wsgi:app --bind 0.0.0.0:$PORT --reload`
