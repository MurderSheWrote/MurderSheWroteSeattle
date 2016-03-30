import requests
import pprint
import json
from .models import Entry
from .models import DBSession, Base
import transaction
from sqlalchemy import create_engine
import os


DOMAIN = 'https://data.seattle.gov/resource/ih58-ykqj.json'


DATABASE_URL = os.environ["DATABASE_URL"]
TESTING_URL = os.environ["TESTING_URL"]


def call_api():
    """Request data from socrata api and get response text back."""
    url = DOMAIN
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def populate_db(entry):
    """Populate database with entries."""
    entries = Entry(**entry)
    DBSession.add(entries)


def clean_data(crime_entry):
    """Replace 'X' with 'None'."""
    cleaned = {}
    for key in crime_entry:
        cleaned[key] = None if crime_entry[key] == "X" else crime_entry[key]
    return cleaned


def import_crimes():
    """Returns clean crime listing collection."""
    return clean_data(call_api())


def main():
    """Set up database and populate with clean crime listing colleciton."""
    engine = create_engine(DATABASE_URL)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        for crime in import_crimes():
            populate_db(crime)


if __name__ == '__main__':
    main()
