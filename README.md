# aivo_challenge

Context:

* Build a REST API using Python 3.

* Using the dataset from the attached CSV file, develop the following user story:

 
Story:

To get a better view of data, a user can filter an indicator for getting countries which has greater index value than a filter (input) value.

Scenario: An user wants to get countries with life satisfaction index value greater than an input value

* Given: All countries with their indicators loaded (from the dataset).

* When: A user wants to get countries with life satisfaction index greater than the input value.

* Then: Return countries with their index value, greater than the input value, using only life satisfaction index and total inequality.

## Requirements for the project

* Python 3.8
* Docker
* Docker-compose
* A lot of patience :)

## Walkthough of the installation

Inside the root folder run the following command
```
docker-compose build
```

Once you finish building the application run
```
docker-compose up
```

Hopefully you will get the following message:

> web_1  |  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

if not dont panic... Just use python
```
pip install -r requirements.txt
```
Once the requirements have finished run
```
python app.py
```

If your application did not start. Please contact me at:

> juancruzalriccortabarria@gmail.com

I will gladly help you with the problem.

## Endpoints

1. "/" --> Just a welcoming message to help you navigate the API

2. /country/filter?life_satisfaction_index=100000

Response:

```
{
  "countries": [
    {
      "country": "Belgium",
      "flags": "",
      "indicator": "Household net financial wealth",
      "inequality": "Total",
      "measure": "Value",
      "powerCode": "Units",
      "reference Period": "",
      "unit": "US Dollar",
      "value": 104084
    },
    {
      "country": "Switzerland",
      "flags": "",
      "indicator": "Household net financial wealth",
      "inequality": "Total",
      "measure": "Value",
      "powerCode": "Units",
      "reference Period": "",
      "unit": "US Dollar",
      "value": 128415
    },
    {
      "country": "United States",
      "flags": "",
      "indicator": "Household net financial wealth",
      "inequality": "Total",
      "measure": "Value",
      "powerCode": "Units",
      "reference Period": "",
      "unit": "US Dollar",
      "value": 176076
    }
  ]
}
```

3. "/api/docs --> SWAGGER ENDPOINT

Really cool interface for calling the endpoints in an easy and fast way

### TODO'S

. Get rid of the validation in the controller class and declare it in the schema.
. Get the list of countries in the /country endpoint.
. Refactor the app.py to only have the running instance, the controller should be the one calling the endpoints.



