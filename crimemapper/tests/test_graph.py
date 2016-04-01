"""Test writing for graphs."""
import pytest
from crimemapper.graph_calcs import(
    random_colors,
    offense_counter,
    color_applicator,
    get_category,
    main_db_call,
    crime_dict_totals,
    crime_category_breakdown
)


def test_random_colors_type():
    """Assert that result is a string object."""
    result = random_colors()
    assert type(result) is str


def test_random_colors_format_front():
    """Assert that front format is correctly formated."""
    result = random_colors()
    assert result[:4] == 'rgb('


def test_random_colors_format_end():
    """Assert that the end of string is formatted correctly."""
    result = random_colors()
    assert result[-1] == ')'


def test_random_colors_ints():
    """Assert that numbers are int the correct place."""
    result = random_colors()
    result = result[4:-1]
    num_list = result.split(',')
    assert type(int(num_list[0])) is int
    assert type(int(num_list[1])) is int
    assert type(int(num_list[2])) is int


def test_random_colors_range():
    """Assert that numbers are in the rgb range."""
    result = random_colors()
    result = result[4:-1]
    num_list = result.split(',')
    assert 0 <= int(num_list[0]) <= 255
    assert 0 <= int(num_list[1]) <= 255
    assert 0 <= int(num_list[2]) <= 255


def test_offense_counter_obj(test_list):
    """Assert that function returns a list."""
    result = offense_counter(test_list)
    assert type(result) == list


def test_offense_counter_contains(test_list):
    """Assert that function returns a list of tuples."""
    result = offense_counter(test_list)
    assert type(result[0]) == tuple


def test_offense_counter_tuple(test_list):
    """Assert that function returns a list of tuples with two items in each."""
    result = offense_counter(test_list)
    assert len(result[0]) == 2


def test_offense_counter_contents_1(test_list):
    """Assert that first item in tuple is the offense."""
    result = offense_counter(test_list)
    assert type(result[0][0]) == str


def test_offense_counter_contents_2(test_list):
    """Assert that second item in tuple is the the number of times counted."""
    result = offense_counter(test_list)
    assert type(result[0][1]) == int


def test_color_applicator_obj(test_list):
    """Assert that function returns a list."""
    result = offense_counter(test_list)
    result = color_applicator(result)
    assert type(result) == list


def test_color_applicator_contains(test_list):
    """Assert that function returns a list of tuples."""
    result = offense_counter(test_list)
    result = color_applicator(result)
    assert type(result[0]) == tuple


def test_color_applicator_tuple(test_list):
    """Assert that function returns a list of tuples with 3 items in each."""
    result = offense_counter(test_list)
    result = color_applicator(result)
    assert len(result[0]) == 3


def test_color_applicator_contents_1(test_list):
    """Assert that first item in tuple is the offense."""
    result = offense_counter(test_list)
    result = color_applicator(result)
    assert type(result[0][0]) == str


def test_color_applicator_contents_2(test_list):
    """Assert that second item in tuple is the the number of times counted."""
    result = offense_counter(test_list)
    result = color_applicator(result)
    assert type(result[0][1]) == int


def test_color_applicator_contents_3(test_list):
    """Assert that third item in tuple is the rgb."""
    result = offense_counter(test_list)
    result = color_applicator(result)
    assert type(result[0][2]) == str


def test_color_applicator_contents_4(test_list):
    """Assert that third item in tuple is the rgb for sure."""
    result = offense_counter(test_list)
    result = color_applicator(result)
    assert result[0][2][:4] == 'rgb('


def test_get_category():
    """Assert return is None when item not in values."""
    result = get_category('fish')
    assert result is None


def test_get_category_2():
    """Assert that key is returned for a found value."""
    result = get_category('BIKE THEFT')
    assert result == 'Theft'


def test_get_category_3():
    """Assert return is None when item is not string."""
    result = get_category([])
    assert result is None


def test_main_db_call(new_entry, clear_main_cache):
    """Assert db will be hit & return a list."""
    result = main_db_call()
    assert type(result) == list


def test_main_db_call_empty_db(dbtransaction, clear_main_cache):
    """Assert if db is empty it will return a list."""
    with pytest.raises(ImportError):
        main_db_call()


def test_main_db_call_items(new_entry, clear_main_cache):
    """Assert db will be hit & return a list of with sub-category."""
    result = main_db_call()
    assert type(result[0][0]) == str


def test_crime_dict_totals(new_entry, clear_main_cache):
    """Assert function will return a list."""
    result = crime_dict_totals()
    assert type(result) == list


def test_crime_dict_totals_contents(new_entry, clear_main_cache):
    """Assert function will return a list of tuples."""
    result = crime_dict_totals()
    assert type(result[0]) == tuple


def test_crime_dict_totals_inside_1(new_entry, clear_main_cache):
    """Assert function will return a list of tuples with formatted content."""
    result = crime_dict_totals()
    assert type(result[0][0]) == str


def test_crime_dict_totals_inside_2(new_entry, clear_main_cache):
    """Assert function will return a list of tuples with formatted content."""
    result = crime_dict_totals()
    assert type(result[0][1]) == int


def test_crime_dict_totals_inside_3(new_entry, clear_main_cache):
    """Assert function will return a list of tuples with formatted content."""
    result = crime_dict_totals()
    assert type(result[0][2]) == str


def test_crime_dict_totals_inside_4(new_entry, clear_main_cache):
    """Assert function will return a list of tuples with formatted content."""
    result = crime_dict_totals()
    assert result[0][2][:4] == 'rgb('


def test_crime_dict_totals_inside_5(new_entry, clear_main_cache):
    """Assert function will return a list of tuples with formatted content."""
    result = crime_dict_totals()
    assert len(result[0]) == 3


def test_crime_dict_totals_key(new_entry, clear_main_cache):
    """Assert function converted from keys."""
    from crimemapper.graph_calcs import UPPER_DICT
    result = crime_dict_totals()
    assert result[0][0] in UPPER_DICT


def test_crime_category_breakdown_contents(new_entry, clear_main_cache):
    """Assert function will return a dictionary."""
    result = crime_category_breakdown()
    assert type(result) == dict
