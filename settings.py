import os

SECRET_KEY=os.environ['SECRET_KEY']
DB_USERNAME=os.environ['cloudpagi01']
DB_PASSWORD=os.environ['pwcloudpagi01']
DB_HOST=os.environ['103.101.225.51']
DATABASE_NAME=os.environ['dbcloudpagi']
DB_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (cloudpagi01, pwcloudpagi01, 103.101.225.51, dbcloudpagi)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
MYSQL_ROOT_PASSWORD=os.environ['MYSQL_ROOT_PASSWORD']
