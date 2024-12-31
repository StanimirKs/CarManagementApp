from flask import Flask, jsonify
from database.db_utils import init_db,db
from models import car_model, garage_model, car_garage_model
from sqlalchemy.sql import text
from flask_migrate import Migrate
from services.car_service import CarService
from repositories.car_repository import CarRepository


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://carUser:car123@localhost:3306/carprojectdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init the database
init_db(app)

# Migrations
migrate = Migrate(app,db)

car_repository = CarRepository(db)
car_service = CarService(car_repository)


@app.route('/')
def index():
     return 'hello world'


@app.route('/cars', methods=['GET'])
def getCars():
     cars = car_service.listCars()
     return jsonify(cars)
     





if __name__ == '__main__':
     app.run(debug=True)