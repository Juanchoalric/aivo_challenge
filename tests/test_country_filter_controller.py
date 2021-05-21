import unittest
from app import app


class TestCountryFilter(unittest.TestCase):

    def test_country_filter_ok(self):

        reply = {"countries":[{"country":"Belgium","flags":"","indicator":"Household net financial wealth","inequality":"Total","measure":"Value","powerCode":"Units","reference Period":"","unit":"US Dollar","value":104084.0},{"country":"Switzerland","flags":"","indicator":"Household net financial wealth","inequality":"Total","measure":"Value","powerCode":"Units","reference Period":"","unit":"US Dollar","value":128415.0},{"country":"United States","flags":"","indicator":"Household net financial wealth","inequality":"Total","measure":"Value","powerCode":"Units","reference Period":"","unit":"US Dollar","value":176076.0}]}
        tested_app = app.test_client(self)
        response = tested_app.get("/country/filter?life_satisfaction_index=100000").get_json()
        self.assertEqual(reply, response)

    def test_country_filter_should_be_greater_than_0(self):

        tested_app = app.test_client(self)
        response = tested_app.get("/country/filter?life_satisfaction_index=-1").get_json()[1]
        self.assertEqual(response, 400)

    def test_country_filter_should_be_a_float(self):

        tested_app = app.test_client(self)
        response = tested_app.get("/country/filter?life_satisfaction_index=hey").get_json()[1]
        self.assertEqual(response, 400)

    def test_country_filter_should_be_named_life_satisfaction_index(self):

        tested_app = app.test_client(self)
        response = tested_app.get("/country/filter?life_satisfaction_index=hey").get_json()[1]
        self.assertEqual(response, 400)
