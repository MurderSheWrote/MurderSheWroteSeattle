import requests
from requests import ConnectionError
import pprint
import json
from .models import Entry
from .models import DBSession, Base
import transaction
from sqlalchemy import create_engine
import os
from sodapy import Socrata
from urllib.error import HTTPError

DOMAIN = 'https://data.seattle.gov/resource/ih58-ykqj.json'


DATABASE_URL = os.environ["DATABASE_URL"]
TESTING_URL = os.environ["TESTING_URL"]
SOCRATA_TOKEN = os.environ["SOCRATA_TOKEN"]


def call_api():
    """Request data from socrata api and get back JSON."""
    try:
        client = Socrata("data.seattle.gov", 'SOCRATA_TOKEN')
        data = client.get("ih58-ykqj", content_type="json", limit=9999)
        return data
    except ConnectionError:
        raise ConnectionError
    except HTTPError:
        raise HTTPError


def populate_db(entry):
    """Populate database with entries."""
    entries = Entry(**entry)
    DBSession.add(entries)


def clean_data(crime_entries):
    """Replace 'X' with 'None'."""
    for entry in crime_entries:
        for key in entry:
            if entry[key] == "X":
                entry[key] = None
    return crime_entries


def main():
    """Set up database and populate with clean crime listing colleciton."""
    engine = create_engine(DATABASE_URL)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        for crime in clean_data(call_api()):
            populate_db(crime)


if __name__ == '__main__':
    main()
