from flask import Flask
from database.db_utils import init_db,db
from models import CarModel, GarageModel, MaintenanceModel
from sqlalchemy.sql import text
from flask_migrate import Migrate

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://carUser:car123@localhost:3306/carprojectdb'


# init the database
init_db(app)

# Migrations
migrate = Migrate(app,db)



@app.route('/')
def index():
     return 'hello world'


@app.route('/cars',methods=['GET'])
def getCars():
     return "A list of cars"






if __name__ == '__main__':
     app.run(debug=True)