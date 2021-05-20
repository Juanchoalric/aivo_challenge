from flask import make_response, jsonify

from services.country_filter_service import CountryFilterService


class CountryFilterController:

    @classmethod
    def country_filter(cls, params):
        """
        
        jsonify the response from the service
        TODO: Update the logic to connect to the schema
        """
        try:
            life_satisfaction_index = params["life_satisfaction_index"]
            life_satisfaction_index = float(life_satisfaction_index)
        except KeyError as e:
            return make_response(jsonify("The param need to be life_satisfaction_index", 400))
        except ValueError as e:
            return make_response(jsonify("The value need to be a float", 400))
        if life_satisfaction_index <= 0:
            return make_response(jsonify("The life_satisfaction_index need to greater than 0", 400))

        return make_response(jsonify(CountryFilterService.country_filter(life_satisfaction_index)), 200)