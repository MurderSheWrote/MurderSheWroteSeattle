"""View functions created here."""
from pyramid.view import view_config
from crimemapper.models import (
    DBSession,
    Entry,
)
import os
from .crimedict import CRIME_DICT
from pyramid.httpexceptions import HTTPServiceUnavailable
from .graph_calcs import crime_dict_totals, crime_category_breakdown


CACHED_RESULTS = {}


def cached_db_call():
    """Cache database hit so no further calls need to be made."""
    if 'already_called' not in CACHED_RESULTS:
        results = DBSession().query(
            Entry.latitude,
            Entry.longitude,
            Entry.summarized_offense_description
        ).all()
        CACHED_RESULTS['already_called'] = results
    return CACHED_RESULTS['already_called']


def find_category(description):
    for k, v in CRIME_DICT.items():
        if description in v:
            return k


@view_config(route_name='map', renderer='templates/map.jinja2')
def map_view(request):
    """Render map view on page."""
    point = cached_db_call()
    places = []
    for i, l in enumerate(point):
        if point[i][0] is None:
            continue  # pragma: no cover
        place = {'lat': point[i][0], 'lng': point[i][1]}
        description = str(point[i][2])
        category = find_category(description)
        places.append([place, description, category])
    dict_ = {"places": places, "key": os.environ.get("GOOGLE_KEY"), "crimes": CRIME_DICT}
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
    try:
        main_pie = crime_dict_totals()
        sub_dict = crime_category_breakdown()
        return {'main_pie': main_pie, 'sub_dict': sub_dict}
    except ImportError:
        raise HTTPServiceUnavailable()
