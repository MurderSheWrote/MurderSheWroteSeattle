"""View functions created here."""
# from pyramid.response import Response
from pyramid.view import view_config
# from pyramid.httpexceptions import HTTPFound
# from sqlalchemy.exc import DBAPIError
from crimemapper.models import (
    DBSession,
    Entry,
)
import os


POINTS = DBSession().query(Entry.latitude, Entry.longitude, Entry.summarized_offense_description).all()


# @view_confit(route_name='map', renderer="json", xhr=True)
@view_config(route_name='map', renderer='templates/map.jinja2')
def map_view(request):
    """Render map view on page."""
    point = POINTS
    places = []
    for i, l in enumerate(point):
        if i == 0:
            continue
        place = {'lat': point[i][0], 'lng': point[i][1]}
        description = str(point[i][2])
        places.append([place, description])
    dict_ = {'places': places, "key": os.environ.get("GOOGLE_KEY")}
    print(dict_)
    return dict_


@view_config(route_name='codes', renderer='templates/crimelist.jinja2')
def codes_view(request):
    """Render code references on page."""
    from .crimedict import CRIME_DICT
    return {"crimes": CRIME_DICT}


@view_config(route_name='about', renderer='templates/about.jinja2')
def about_view(request):
    """Render about page."""
    return {}


@view_config(route_name='stats', renderer='templates/graphs.jinja2')
def stats_view(request):
    """Render stats page."""
    return {}
