from flask import Flask, request
import pandas as pd
from controllers.country_filter_controller import CountryFilterController

app = Flask(__name__)

#df = pd.read_csv("countries.csv")

@app.route('/country')
def country():
    df = pd.read_csv("countries.csv")
    response = {}
    params = request.args.to_dict()
    output = CountryFilterController.country_filter(df, params)
    response["countries"] = output
    return output

if __name__ == '__main__':
    app.run()