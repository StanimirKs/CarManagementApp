from flask import Flask, request, jsonify
from services.car_service import CarService
from DTOs.car_dto import CreateCarDTO,UpdateCarDTO,ResponseCarDTO
from models import car_model
from repositories.car_repository import carRepository
from database import db_utils

app = Flask(__name__)


# @app.route('/cars', methods=['GET'])
# def getCars():
#      try:
#           cars = CarService.listCars()
#           return jsonify(car.liscencePlate for car in cars)
#      except Exception as e:
#           return jsonify({"error": str(e)}),500