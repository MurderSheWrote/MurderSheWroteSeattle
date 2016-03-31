"""Graph calculations for graph view."""
from crimemapper.models import (
    DBSession,
    Entry,
)
from collections import Counter

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


def crime_dict_totals():
    """Return a count of all instances of a summary offense."""
    db_request = DBSession().query(Entry.summarized_offense_description).all()
    all_crimes = [item[0] for item in db_request]
    categorized_crimes = map(get_category, all_crimes)
    categorized_crimes = [c for c in categorized_crimes]
    sum_offense = Counter()
    for offense in categorized_crimes:
        if offense is None:
            continue
        sum_offense[offense] += 1
    sum_offense = sum_offense.most_common()
    return sum_offense


def pie_calc():
    working_on = crime_dict_totals()
    total = 0
    for i in working_on:
        total += i[1]
    percentages = []
    for i in working_on:
        new_list = [i[0], (i[1]/total)]
        percentages.append(new_list)
    print(percentages)
    return percentages

pie_calc()