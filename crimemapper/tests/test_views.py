# -*- coding:utf-8 -*-
"""Test file for views."""
from crimemapper.views import entry_view
from testapp.views import home_view
from testapp.models import DBSession, Entry
from pyramid.testing import DummyRequest
import pytest
from webtest import AppError


def test_map_view(dbtransaction, app):
    """Test map view route path."""
    response = app.get('/')
    assert response.status_code == 200


def test_bad_route(dbtransaction, app):
    """Test bad route requests."""
    with pytest.raises(AppError):
        app.get('/whatever')
