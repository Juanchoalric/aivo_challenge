from flask import Flask, request

from controllers.country_filter_controller import CountryFilterController

app = Flask(__name__)


@app.route('/country')
def country():
    life_satisfaction_param = request.args.to_dict()
    life_satisfaction_index_response = CountryFilterController.country_filter(
        life_satisfaction_param
    )
    return life_satisfaction_index_response


if __name__ == '__main__':
    app.run()
