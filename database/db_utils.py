from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate


db = SQLAlchemy()
pymysql.install_as_MySQLdb()


def init_db(app):
     db.init_app(app)

     