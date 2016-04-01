"""Test writing for graphs."""
import pytest

from crimemapper.graph_calcs import random_colors, offense_counter


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


def test_offense_counter_obj():
    """Assert that function returns a list."""
    test_list = ['cat', 'dog', 'cat', 'potato', 'potato']
    result = offense_counter(test_list)
    assert type(result) == list


def test_offense_counter_contains():
    """Assert that function returns a list of tuples."""
    test_list = ['cat', 'dog', 'cat', 'potato', 'potato']
    result = offense_counter(test_list)
    assert type(result[0]) == tuple


def test_offense_counter_contents_1():
    """Assert that first item in tuple is the offense."""
    test_list = ['cat', 'dog', 'cat', 'potato', 'potato']
    result = offense_counter(test_list)
    assert type(result[0][0]) == str


def test_offense_counter_contents_2():
    """Assert that second item in tuple is the the number of times counted."""
    test_list = ['cat', 'dog', 'cat', 'potato', 'potato']
    result = offense_counter(test_list)
    assert type(result[0][1]) == int
