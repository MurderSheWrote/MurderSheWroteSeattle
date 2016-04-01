"""Graph calculations for graph view."""
from crimemapper.models import (
    DBSession,
    Entry,
)
from collections import Counter
import random

UPPER_DICT = {
    "Assault": ["ASSAULT"],
    "Theft": [
        "BIKE THEFT", "BURGLARY", "CAR PROWL", "MAIL THEFT", "PICKPOCKET",
        "PURSE SNATCH", "SHOPLIFTING", "THEFT OF SERVICE", "VEHICLE THEFT",
        "BURGLARY-SECURE PARKING-RES"
    ],
    "Sin": ["GAMBLE", "PORNOGRAPHY", "PROSTITUTION"],
    "Drugs": [
        "DUI", "LIQUOR VIOLATIONS", "NARCOTICS", "STAY OUT OF AREA OF DRUGS"
    ],
    "Fraud": ["COUNTERFEIT", "EMBEZZLE", "FORGERY", "FRAUD"],
    "Homicide": ["HOMICIDE"],
    "Property": [
        "ILLEGAL DUMPING", "LOST PROPERTY", "OTHER PROPERTY",
        "PROPERTY DAMAGE", "RECKLESS BURNING", "RECOVERED PROPERTY",
        "STOLEN PROPERTY",
    ],
    "Robbery": ["ROBBERY"],
    "Weapons": ["WEAPONS"],
    "Disturbances": [
        "DISORDERLY CONDUCT", "DISPUTE", "FIREWORK", "PUBLIC NUISANCE",
        "THREATS", "TRESPASS"
    ],
    "Other": [
        "ANIMAL COMPLAINT", "BIAS INCIDENT", "ELUDING", "ESCAPE", "EXTORTION",
        "HARBOR CALLS", "INJURY", "LOITERING", "METRO", "OBSTRUCT", "TRAFFIC",
        "WARRANT ARREST", "VIOLATION OF COURT ORDER"
    ],
}


CATEGORY_MAPPING = {tuple(val): key for key, val in UPPER_DICT.items()}


def get_category(word):
    """Inverting keys and items."""
    for words in CATEGORY_MAPPING:
        if word in words:
            return CATEGORY_MAPPING[words]
    else:
        return None


MAIN_RESULTS = {}


def main_db_call():
    """Cashing a db call to close the session."""
    if 'already_called' not in MAIN_RESULTS:
        results = DBSession().query(
            Entry.summarized_offense_description
        ).all()
        MAIN_RESULTS['already_called'] = results
    return MAIN_RESULTS['already_called']


def random_colors():
    """Produce a random rgb colors for charts."""
    def r():
        return random.randint(0, 255)
    return 'rgb({},{},{})'.format(r(), r(), r())


def offense_counter(offense_list):
    """Return a list of tuples with counted offenses."""
    sum_offense = Counter()
    for offense in offense_list:
        if offense is None:
            continue
        sum_offense[offense] += 1
    return sum_offense.most_common()


def color_applicator(sum_list):
    """Return a list of tuples with colors pacakaged."""
    pie = []
    for i, item in enumerate(sum_list):
        wedge = item + (random_colors(),)
        pie.append(wedge)
    return pie


def crime_dict_totals():
    """Return a count of all instances of a summary offense."""
    db_request = main_db_call()
    all_crimes = [item[0] for item in db_request]
    categorized_crimes = map(get_category, all_crimes)
    categorized_crimes = [c for c in categorized_crimes]
    sum_offense = offense_counter(categorized_crimes)
    return color_applicator(sum_offense)


def crime_category_breakdown():
    """Return a dictionary of crimes broken down by subcategories."""
    db_request = main_db_call()
    all_crimes = [item[0] for item in db_request]
    sub_offense = offense_counter(all_crimes)
    sub_pie = color_applicator(sub_offense)
    sub_dict = {}
    for i, thing in enumerate(sub_pie):
        for key, category in UPPER_DICT.items():
            if sub_pie[i][0] in category:
                sub_dict.setdefault(key, [])
                sub_dict[key].append(sub_pie[i])
            else:
                continue
    return sub_dict
