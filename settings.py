import os

SECRET_KEY=os.environ['SECRET_KEY']
DB_USERNAME=os.environ['cloudpagi01']
DB_PASSWORD=os.environ['pwcloudpagi01']
DB_HOST=os.environ['103.101.225.51']
DATABASE_NAME=os.environ['dbcloudpagi']
DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
MYSQL_ROOT_PASSWORD=os.environ['MYSQL_ROOT_PASSWORD']
