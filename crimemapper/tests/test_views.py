# -*- coding:utf-8 -*-
"""Test file for views."""
from crimemapper.models import DBSession, Entry
from crimemapper.views import map_view
import pytest
from webtest import AppError
from pyramid.testing import DummyRequest



def test_map_view(dbtransaction):
    result = map_view(DummyRequest)
    assert type(result['places']) is list
    # test_entry = map_view(entry_dict)
    # assert map_view(entry_dict) == {[{'lat': 47.611839294, 'lng': -122.332801819}, 'EMBEZZLE']}


# def test_new_entry(dbtransaction, entry_dict, new_entry):
#     new_model = Entry(entry_dict)
#     assert new_model.id is None
    # DBSession.add(new_entry)
    # DBSession.flush()
    # assert entry_dict.id is not None


def test_map_view_route(dbtransaction, app):
    """Test map view route path."""
    response = app.get('/')
    assert response.status_code == 200


def test_bad_route(dbtransaction, app):
    """Test bad route requests."""
    with pytest.raises(AppError):
        app.get('/whatever')


def test_stats_view_route(dbtransaction, app):
    """Test statistics view route path."""
    response = app.get('/stats')
    assert response.status_code == 200


def test_codes_view_route(dbtransaction, app):
    """Test codes refference view route path."""
    response = app.get('/codes')
    assert response.status_code == 200


def test_about_view_route(dbtransaction, app):
    """Test codes refference view route path."""
    response = app.get('/about')
    assert response.status_code == 200
