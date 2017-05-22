# Flask MySQL Boilerplate

This is a boilerplate for a Flask app that can run as a virtualenv, Heroku or Docker application.

If you install MySQL locally using Homebrew, You can start and stop MySQL by doing `mysql.server start` and stopping with `mysql.server stop`.

Remember to run `python manage.py db init` to create tables and `python manage.py db migrate` and/or `python manage.py db upgrade` when you modify them.
