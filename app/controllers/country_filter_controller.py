from flask import make_response, jsonify
from services.country_filter_service import CountryFilterService


class CountryFilterController:
    @classmethod
    def country_filter(cls, df, params):
        """
        
        Check that the input is valid
        """
        value = params["value"]
        try:
            value = float(value)
        except:
            return make_response("value field need to be in float format!", 400)
        if value == 0:
            return make_response("value field is required!", 400)
        if value < 0:
            return make_response("value field need to be higher than 0", 400)
        else:
            return make_response(jsonify(CountryFilterService.country_filter(df, params)), 200)