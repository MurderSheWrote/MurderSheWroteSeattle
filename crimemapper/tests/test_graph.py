"""Test writing for graphs."""
import pytest
from crimemapper.models import DBSession, Entry

from crimemapper.graph_calcs import random_colors

try:
    from unittest.mock import Mock, patch, mock, MagicMock
except ImportError:
    from mock import Mock, patch, mock, MagicMock


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
    """Assert that numbers are int the correct place."""
    result = random_colors()
    result = result[4:-1]
    num_list = result.split(',')
    assert 0 <= int(num_list[0]) <= 255
    assert 0 <= int(num_list[1]) <= 255
    assert 0 <= int(num_list[2]) <= 255


def test_crime_year_count_input():
    """Test query is correct entry column."""
    from crimemapper.graph_calcs import crime_year_count, MAIN_RESULTS
    mocked = MagicMock()
    DBSession().query = mocked
    mocked.all = MagicMock(return_value=[])
    crime_year_count()
    DBSession().query.assert_called_with(Entry.occurred_date_or_date_range_start)


def test_crime_year_count_output():
    """Test query output is dict of tuple."""
    from crimemapper.graph_calcs import crime_year_count, MAIN_RESULTS
    mocked = MagicMock()
    DBSession().query = mocked
    mocked.all = MagicMock(return_value=[])
    crime_year_count()
    assert type(MAIN_RESULTS) is dict


# def test_crime_year_count_result():
#     """Test function returns year and count dict."""
#     from crimemapper.graph_calcs import crime_year_count, MAIN_RESULTS
#     mocked = MagicMock()
#     DBSession().query = mocked
#     mocked.all = MagicMock(return_value=[
#         ('1990-01-01T00:00:00',),
#         ('1990-01-06T00:00:00',),
#         ('1992-01-01T00:00:00',)
#     ])
#     test = crime_year_count()
#     assert test == {1990: 2, 1992: 1}
