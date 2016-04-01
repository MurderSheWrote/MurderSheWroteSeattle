# -*- coding:utf-8 -*-
"""Test file for views."""
from crimemapper.views import map_view
import pytest
from webtest import AppError
from pyramid.testing import DummyRequest


def test_map_view_0(new_entry, clear_db_cache):
    """Test that map view returns a list of items for template."""
    result = map_view(DummyRequest)
    assert type(result['places']) is list


def test_map_view_1(new_entry, clear_db_cache):
    """Test that map view returns key for google as a string."""
    result = map_view(DummyRequest)
    assert type(result['crimes']) is dict


def test_map_view_2(new_entry, clear_db_cache):
    """Test that when query returns nothing places list is empty."""
    result = map_view(DummyRequest)
    assert type(result[['places'][0]]) is list


def test_map_view_3(dbtransaction, clear_db_cache):
    """Test that when query returns nothing places list is empty."""
    result = map_view(DummyRequest)
    places_list = result[['places'][0]]
    with pytest.raises(IndexError):
        type(places_list[0]) is list


def test_map_view_4(new_entry, clear_db_cache):
    """Test that when query returns nothing places list is empty."""
    result = map_view(DummyRequest)
    places_list = result[['places'][0]]
    assert type(places_list[0][0]) is dict


def test_map_view_5(new_entry, clear_db_cache):
    """Test that when query returns nothing places list is empty."""
    result = map_view(DummyRequest)
    places_list = result[['places'][0]]
    assert type(places_list[0][1]) is str


def test_map_view_route(app, clear_db_cache):
    """Test map view route path."""
    response = app.get('/')
    assert response.status_code == 200


def test_bad_route(app):
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
