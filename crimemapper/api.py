import requests
import pprint
import json
from .models import Entry
from .models import DBSession, Base
import transaction
from sqlalchemy import create_engine


DOMAIN = 'https://data.seattle.gov/resource/ih58-ykqj.json'


def call_api():
    """Request data from socrata api and get response text back."""
    url = DOMAIN
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def populate_db(entry):
    """Populate database with entries."""
    entries = Entry(**entry)
    DBSession.add(entries)


def clean_dict(listing_collection):
    """Replace 'X' with 'NULL'."""
    for crime in listing_collection:
        for key in crime: 
            if crime[key] == 'X':
                crime[key] = None
    return listing_collection


def make_dict(json):
    """Appending crime into listing collection."""
    listing_collection = []
    for listing in json:
        crime = {}
        for key in listing:
            crime[key] = listing[key]
        listing_collection.append(crime)
    return clean_dict(listing_collection)


def import_crimes():
    """Returns clean crime listing collection."""
    response = call_api()
    json_response = json.loads(response)
    return make_dict(json_response)


def main():
    """Set up database and populate with clean crime listing colleciton."""
    database_url = 'postgres://nadiabahrami:@localhost:5432/crimedb'
    engine = create_engine(database_url)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        for crime in import_crimes():
            populate_db(crime)


if __name__ == '__main__':
    main()
