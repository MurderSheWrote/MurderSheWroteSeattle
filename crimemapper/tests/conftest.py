# -*- coding: utf-8 -*-
"""Pytest fixtures for testing."""
from sqlalchemy import create_engine
from crimemapper.models import DBSession, Base, Entry
from crimemapper import main
from webtest import TestApp
from pyramid.paster import get_appsettings
import os
import pytest
import transaction


TEST_DATABASE_URL = os.environ["TESTING_URL"]


@pytest.fixture(scope='session')
def config_path():
    """Fixture to send path of dev.ini file."""
    dir_ = os.path.dirname(__file__)
    demo_dir = os.path.join(dir_, '../..')
    return os.path.join(demo_dir, 'development.ini')


@pytest.fixture(scope='session')
def test_url():
    """Fixture to access path to test database."""
    return TEST_DATABASE_URL


@pytest.fixture(scope='session')
def sqlengine(request):
    engine = create_engine(TEST_DATABASE_URL)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    def teardown():
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return engine


@pytest.fixture(scope='function')
def dbtransaction(request, sqlengine):
    connection = sqlengine.connect()
    trans = connection.begin()
    DBSession.configure(bind=connection)

    def teardown():
        trans.rollback()
        connection.close()
        DBSession.remove()

    request.addfinalizer(teardown)
    return connection


@pytest.fixture(scope='function')
def entry_dict():
    """Create a testing dictionary."""
    a_dict = {
        'rms_cdw_id': 705233,
        'general_offense_number': 201939834,
        'offense_code': 2799,
        'offense_code_extension': 0,
        'offense_type': 'EMBEZZLE',
        'summary_offense_code': 2700,
        'summarized_offense_description': 'EMBEZZLE',
        'date_reported': '05/07/2015 11:13:00 AM',
        'occurred_date_or_date_range_start': '08/30/2005 10:00:00 AM',
        'occurred_date_range_end': '01/01/2013 10:00:00 AM',
        'hundred_block_location': '7XX BLOCK OF PIKE ST',
        'district_sector': 'M',
        'zone_beat': 'M2',
        'census_tract_2000': '8200.1018',
        'longitude': -122.332801819,
        'latitude': 47.611839294,
        'location': '(47.611839294, -122.332801819)',
    }
    return a_dict


@pytest.fixture(scope='function')
def new_entry(request, dbtransaction, entry_dict):
    """Create an entry to testing db."""
    new_model = Entry(**entry_dict)
    with transaction.manager:
        DBSession.add(new_model)

    def teardown():
        # import pdb; pdb.set_trace()
        with transaction.manager:
            DBSession.delete(new_model)
        print('foo')

    request.addfinalizer(teardown)


@pytest.fixture(scope='function')
def app(config_path, dbtransaction, test_url):
    """Create pretend app fixture of main app to test routing."""
    settings = get_appsettings(config_path)
    settings['sqlalchemy.url'] = test_url
    app = main({}, **settings)
    return TestApp(app)


@pytest.fixture(scope="function")
def clear_db_cache():
    """Clear cache."""
    import crimemapper
    crimemapper.views.CACHED_RESULTS = {}


@pytest.fixture(scope="function")
def clear_main_cache():
    """Clear main cache."""
    import crimemapper
    crimemapper.graph_calcs.MAIN_RESULTS = {}


@pytest.fixture(scope="function")
def test_list():
    """Fake list for testing."""
    t_list = ['cat', 'dog', 'cat', 'potato', 'potato', None]
    return t_list
