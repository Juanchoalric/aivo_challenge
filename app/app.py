from schemas.life_satisfaction_schema import LifeSatisfactionSchema
from flask import Flask, request
import pandas as pd
from controllers.country_filter_controller import CountryFilterController

app = Flask(__name__)

#df = pd.read_csv("countries.csv")
schema = LifeSatisfactionSchema()

@app.route('/country')
def country():
    life_satisfaction_param = schema.dump(request.args.to_dict())
    life_satisfaction_index_response = CountryFilterController.country_filter(
        life_satisfaction_param
        )
    return life_satisfaction_index_response

if __name__ == '__main__':
    app.run()