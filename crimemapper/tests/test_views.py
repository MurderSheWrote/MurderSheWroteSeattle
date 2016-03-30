# -*- coding:utf-8 -*-
"""Test file for views."""
from crimemapper.models import DBSession, Entry
import pytest
from webtest import AppError


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
