from flask import make_response, jsonify
from services.country_filter_service import CountryFilterService


class CountryFilterController:
    @classmethod
    def country_filter(cls, params):
        """
        
        jsonify the response from the service
        """
        return make_response(jsonify(CountryFilterService.country_filter(params)), 200)