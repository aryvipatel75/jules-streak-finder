import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_longest_streak_at_end():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7]) == 3

def test_longest_streak_in_middle():
    assert longest_positive_streak([2, 3, 4, -1, 5, 6]) == 3

def test_with_zeros():
    assert longest_positive_streak([2, 3, 0, 5, 6, 7]) == 3

def test_with_negatives():
    assert longest_positive_streak([2, 3, -5, 5, 6, 7]) == 3

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_element_positive():
    assert longest_positive_streak([5]) == 1

def test_single_element_non_positive():
    assert longest_positive_streak([-5]) == 0

def test_example_from_description():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_another_example():
    assert longest_positive_streak([1, 1, 1]) == 3