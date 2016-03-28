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
    return HTTPFound(request.route_url('map'))
