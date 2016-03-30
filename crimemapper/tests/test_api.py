import pytest
import requests
from requests import Response, HTTPError
import json
from unittest.mock import MagicMock, Mock
from unittest.mock import patch
from sodapy import Socrata


RESPONSE_200_DATA = {
    'census_tract_2000': '1900.1012',
    'date_reported': '2016-03-10T08:18:00',
    'district_sector': 'L',
    'general_offense_number': '201684521',
    'hundred_block_location': '2XX BLOCK OF NE 94 ST',
    'latitude': '47.696815491',
    'location': {
        'latitude': '47.696815491',
        'longitude': '-122.327774048',
        'needs_recoding': False
    },
    'longitude': '-122.327774048',
    'occurred_date_or_date_range_start': '1990-01-01T00:00:00',
    'occurred_date_range_end': '2016-03-10T08:00:00',
    'offense_code': 'X',
    'offense_code_extension': '21',
    'offense_type': 'DISTURBANCE-OTH',
    'rms_cdw_id': '700713',
    'summarized_offense_description': 'DISTURBANCE',
    'summary_offense_code': 'X',
    'zone_beat': 'L2'
}

CLEANED_DATA = {
    'census_tract_2000': '1900.1012',
    'date_reported': '2016-03-10T08:18:00',
    'district_sector': 'L',
    'general_offense_number': '201684521',
    'hundred_block_location': '2XX BLOCK OF NE 94 ST',
    'latitude': '47.696815491',
    'location': {
        'latitude': '47.696815491',
        'longitude': '-122.327774048',
        'needs_recoding': False
    },
    'longitude': '-122.327774048',
    'occurred_date_or_date_range_start': '1990-01-01T00:00:00',
    'occurred_date_range_end': '2016-03-10T08:00:00',
    'offense_code': None,
    'offense_code_extension': '21',
    'offense_type': 'DISTURBANCE-OTH',
    'rms_cdw_id': '700713',
    'summarized_offense_description': 'DISTURBANCE',
    'summary_offense_code': None,
    'zone_beat': 'L2'
}


def test_call_api_200():
    """Test calling url and getting reponse back without raising error."""
    from crimemapper.api import call_api
    r = Response()
    r.status_code = 200
    r.json = MagicMock()
    requests.get = MagicMock(return_value=r)
    call_api()


def test_call_api_403():
    """Test calling url and raising error."""
    from crimemapper.api import call_api
    r = Response()
    r.status_code = 403
    requests.get = MagicMock(return_value=r)
    with pytest.raises(HTTPError):
        call_api()


def test_clean_crime_entry():
    """Test json data with X replcaed by None."""
    from crimemapper.api import clean_data
    assert clean_data(RESPONSE_200_DATA) == CLEANED_DATA


def test_import_crimes():
    """Test json data is clean."""
    from crimemapper.api import import_crimes
    r = Response()
    r.status_code = 200
    r.json = MagicMock(return_value=RESPONSE_200_DATA)
    requests.get = MagicMock(return_value=r)
    assert import_crimes() == CLEANED_DATA


def test_populate_db():
    """Test right entry passed into db."""
    pass
#     from crimemapper.api import populate_db
#     from crimemapper.models import DBSession, Entry
#     DBSession.add = Mock()
#     populate_db(CLEANED_DATA)
#     DBSssion.add.call_args
#     #call(entries.attr=val)
#     call()[0]
#     for key, val in CLEANED_DATA.items():
#         if key =
