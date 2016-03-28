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
    # place = DBSession().query(Entry).get(location)
    place = {'lat': 47.696815491, 'lng': -122.327774048}
    return {'place': place}
    # return {}