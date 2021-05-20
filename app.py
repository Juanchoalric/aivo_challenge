from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint

from controllers.country_filter_controller import CountryFilterController

app = Flask(__name__)

SWAGGER_ROUTE = '/api/docs'
API_ROUTE_FILE = '/static/swagger.yaml'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_ROUTE,
    API_ROUTE_FILE,
    config={
        'app_name': "filter_country"
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_ROUTE)


@app.route('/')
def index():
    return 'Go to /country-filter or /api/docs for a better experience'


@app.route('/filter-country')
def country():
    life_satisfaction_param = request.args.to_dict()
    life_satisfaction_index_response = CountryFilterController.country_filter(
        life_satisfaction_param
    )
    return life_satisfaction_index_response


if __name__ == '__main__':
    app.run()
