from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'


swagger_ui_blueprint = get_swaggerui_blueprint(
     SWAGGER_URL,
     API_URL,
     config={'app_name':'Flask Swagger'}
)

app.register_blueprint(swagger_ui_blueprint,url_prefix=SWAGGER_URL)

@app.route('/cars', methods=['GET'])
def getCars():
     return{'cars': [{'make':'Mercedes','model':'CLK','year':2004}]}

if __name__ == '__main__':
     app.run(debug=True)