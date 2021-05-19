import random
import unittest
import pandas as pd
import pytest
from app import app

from controllers.country_filter_controller import CountryFilterController

class TestCountryFilterController(unittest.TestCase):

    def test_params_value_ok(self):
        df = pd.read_csv("app\countries.csv")
        with app.app_context():
            number = 100000
            params = {'value': number}
            result = CountryFilterController.country_filter(df, params)
            assert result is not None
            assert result.status_code == 200
    
    def test_params_value_not_a_number(self):
        df = pd.read_csv("app\countries.csv")
        with app.app_context():
            number = "Hello"
            params = {'value': number}
            result = CountryFilterController.country_filter(df, params)
            assert result.status_code == 400
    
    def test_params_value_not_a_positive_number(self):
        df = pd.read_csv("app\countries.csv")
        with app.app_context():
            number = -1
            params = {'value': number}
            result = CountryFilterController.country_filter(df, params)
            assert result.status_code == 400