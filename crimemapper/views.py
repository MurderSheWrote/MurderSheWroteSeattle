"""View functions created here."""
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from crimemapper.models import (
    DBSession,
    Entry,
)
import os


@view_config(route_name='map', renderer='templates/map.jinja2')
def map_view(request):
    """Render map view on page."""
    # place = DBSession().query(Entry).get(location)
    place = {'lat': 47.696815491, 'lng': -122.327774048}, {'lat': 47.606815491, 'lng': -122.327774048}

    return {"places": place, "key": os.environ.get("GOOGLE_KEY")}


@view_config(route_name='codes', renderer='templates/reference.jinja2')
def codes_view(request):
    """Render code references on page."""
    return {}


@view_config(route_name='about', renderer='templates/about.jinja2')
def about_view(request):
    """Render about page."""
    return {}


@view_config(route_name='stats', renderer='templates/graphs.jinja2')
def stats_view(request):
    """Render stats page."""
    return {}
