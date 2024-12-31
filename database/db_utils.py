from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_migrate import Migrate


db = SQLAlchemy()
pymysql.install_as_MySQLdb()


def init_db(app):
     # Изключва следенето на модификациите с цел подобряване на производителността
     app.config['SQLACLHEMY_TRACK_MODIFICATIONS'] = False
     db.init_app(app)

     