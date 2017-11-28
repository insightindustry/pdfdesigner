# -*- coding: utf-8 -*-

"""Tests for pdfdesigner.utilities"""

import pytest
from pdfdesigner import utilities

def test_is_numeric():
    assert utilities.is_numeric(1) is True
    assert utilities.is_numeric('alamakota') is False
    assert utilities.is_numeric(True) is True
    assert utilities.is_numeric([1, 2, 3]) is False


def test_is_string():
    assert utilities.is_string(1) is False
    assert utilities.is_string('alamakota') is True
    assert utilities.is_string(True) is False
    assert utilities.is_string(u'this-is-unicode') is True


def test_is_iterable():
    assert utilities.is_iterable(1) is False
    assert utilities.is_iterable('alamakota') is True
    assert utilities.is_iterable(True) is False
    assert utilities.is_iterable([1, 2, 3]) is True
    assert utilities.is_iterable({'test': 1, 'test2': 2}) is True
    assert utilities.is_iterable((1, 2)) is True


def test_get_indexes(iterable):
    iterable = ['test1', 'test2', 'test3', 'test2']
    expected_result = [1, 3]
    result = utilities.get_indexes(iterable, item = 'test2')
    assert result == expected_result


def test_remove_relative_item():
    iterable = ['test1', 'test2', 'test3', 'test2', 'test2']
    expected_result = ['test1', 'test2', 'test3', 'test2']

    result = utilities.remove_relative_item(iterable,
                                            relative_position = 1,
                                            item = 'test2')

    assert result == expected_result
