# Flask MySQL Boilerplate

This is a boilerplate for a Flask app that can run as a virtualenv, Heroku or Docker application. Updated for Flask 1.0.2.

Make sure you have `python 3.6` installed.

## Local MySQL server
- Create the application user and password:
    - Logon to MySQL using root user
    - Create the counter database `CREATE DATABASE counter;`
    - Give privileges to counter user `CREATE USER 'counter_user'@'%' IDENTIFIED BY 'counter_password';`  
    - Create the counter user `GRANT ALL PRIVILEGES ON counter.* TO 'counter_user'@'%';` and `FLUSH PRIVILEGES;`
- Create a virtualenv: `python3 -m venv venv`
- Activate the virtualenv: `source venv/bin/activate`
- Install the packages: `pip install -r requirements.txt`
- Run `flask db init` to initialize migrations
- Run `flask db migrate` and `flask db upgrade` to create tables
- Run `flask runserver`
- Open `http://localhost:5000` on your browser
- To open a shell, just do `flask shell`
- Run tests by doing `python tests.py`

## Using Docker
- Run `docker-compose up`
- In a new terminal or tab run:
    - `docker exec -it counterappmysql_web_1 flask db init` to initialize migrations
    - `docker exec -it counterappmysql_web_1 flask db migrate` and `docker exec -it counterappmysql_web_1 flask db upgrade` to create tables
- Open `http://localhost:5000` on your browser
- Run tests by doing `docker exec -it counterappmysql_web_1 python tests.py`

## Production
- Use Gunicorn `gunicorn wsgi:app --bind 0.0.0.0:$PORT --reload`
