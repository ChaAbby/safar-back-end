# safar-back-end

## Introduction

Safar is a web app that allows a user to create itineraries by saving places to an itinerary that the user creates. The itinerary will output the most the efficent order that the user should travel to each location. The user will be able to access the google maps url link by a simple click of the locations in the itinerary. 

This app is integrated with a Flask API. The user is able to create an itinerary, save places and save places to a specific itinerary with functionality from the back end.


## Dependencies

    alembic==1.5.4
    attrs==20.3.0
    autopep8==1.5.5
    certifi==2020.12.5
    chardet==4.0.0
    click==7.1.2
    Flask==1.1.2
    Flask-Migrate==2.6.0
    Flask-SQLAlchemy==2.4.4
    gunicorn==20.1.0
    idna==2.10
    iniconfig==1.1.1
    itsdangerous==1.1.0
    Jinja2==2.11.3
    Mako==1.1.4
    MarkupSafe==1.1.1
    packaging==20.9
    pluggy==0.13.1
    psycopg2-binary==2.8.6
    py==1.10.0
    pycodestyle==2.6.0
    pyparsing==2.4.7
    pytest==6.2.3
    python-dateutil==2.8.1
    python-dotenv==0.15.0
    python-editor==1.0.4
    requests==2.25.1
    six==1.15.0
    SQLAlchemy==1.3.23
    toml==0.10.2
    urllib3==1.26.4
    Werkzeug==1.0.1



## Installation
1. Clone this repository.
2. Create a virtual environment using `python3 -m venv venv`.
3. Activate the virtual enviroment using  `source venv/bin/activate`.
4. While the virtual envirioment is running install dependencies by running `pip install -r requirements.txt`.
5. To run the server to test out the back-end functionality use `flask run` (to run in debug mode use `FLASK_ENV=development flask run`).