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
    """Produce random colors for charts."""
    def r():
        return random.randint(0, 255)
    return 'rgb({},{},{})'.format(r(), r(), r())


def crime_dict_totals():
    """Return a count of all instances of a summary offense."""
    # import pdb; pdb.set_trace()
    db_request = main_db_call()
    all_crimes = [item[0] for item in db_request]
    categorized_crimes = map(get_category, all_crimes)
    categorized_crimes = [c for c in categorized_crimes]
    sum_offense = Counter()
    for offense in categorized_crimes:
        if offense is None:
            continue
        sum_offense[offense] += 1
    sum_offense = sum_offense.most_common()
    main_pie = []
    for i, item in enumerate(sum_offense):
        wedge = item + (random_colors(),)
        main_pie.append(wedge)
    return main_pie


def crime_category_breakdown():
    """Return a dictionary of crimes broken down by subcategories."""
    db_request = main_db_call()
    all_crimes = [item[0] for item in db_request]
    sub_offense = Counter()
    for offense in all_crimes:
        if offense is None:
            continue
        sub_offense[offense] += 1
    sub_offense = sub_offense.most_common()
    sub_pie = []
    for i, item in enumerate(sub_offense):
        wedge = item + (random_colors(),)
        sub_pie.append(wedge)
    print(sub_pie)
    sub_dict = {}
    # import pdb; pdb.set_trace()
    for i, thing in enumerate(sub_pie):
        for key, category in UPPER_DICT.items():
            if sub_pie[i][0] in category:
                sub_dict.setdefault(key, [])
                sub_dict[key].append(sub_pie[i])
            else:
                continue
                # sub_dict.setdefault(key, sub_pie[i][0])
        print(sub_dict)
    return sub_dict
