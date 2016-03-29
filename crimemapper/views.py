"""View functions created here."""
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError
from crimemapper.models import (
    DBSession,
    Entry,
)


@view_config(route_name='map', renderer='templates/map.jinja2')
def map_view(request):
    """Render map view on page."""
    lat = DBSession().query(Entry.latitude).all()
    lng = DBSession().query(Entry.longitude).all()
    places = []
    for i, l in enumerate(lat):
        if i == 0:
            continue
        place = {'lat': lat[i][0], 'lng': lng[i][0]}
        places.append(place)
    return {'places': places}



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
