from .models import Entry
from .models import DBSession, Base
import transaction
from sqlalchemy import create_engine
import os
from sodapy import Socrata

DOMAIN = 'https://data.seattle.gov/resource/ih58-ykqj.json'


DATABASE_URL = os.environ["DATABASE_URL"]
TESTING_URL = os.environ["TESTING_URL"]
SOCRATA_TOKEN = os.environ["SOCRATA_TOKEN"]


def call_api():
    """Request data from socrata api and get back JSON."""
    client = Socrata("data.seattle.gov", 'SOCRATA_TOKEN')
    data = client.get("ih58-ykqj", content_type="json", limit=49998)
    return data


def add_entry(entry):
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


if __name__ == '__main__':
    """Set up database and populate with clean crime listing."""
    engine = create_engine(DATABASE_URL)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        for crime in clean_data(call_api()):
            add_entry(crime)
