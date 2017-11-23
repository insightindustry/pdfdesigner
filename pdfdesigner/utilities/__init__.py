# -*- coding: utf-8 -*-

"""
######################
pdfdesigner.utilities
######################

Module defines (pure) utility functions.

"""
from numbers import Number
from decimal import Decimal
import collections


def is_numeric(value):
    """Check whether ``value`` is a numeric type.

    :param value: The value to be validated.

    :returns: ``True`` if the value is of a numeric type, otherwise ``False``.
    :rtype: bool

    .. caution::
      Will also return ``True`` if passed a ``bool``, since in Python ``bool``
      is an ``int`` at heart.

    """
    return isinstance(value, Number)


def is_string(value):
    """Check whether ``value`` is a string."""
    return isinstance(value, str)


def is_none(value):
    """Check whether ``value`` is ``None``."""
    return value is None

def is_boolean(value):
    """Check whether ``value`` is a boolean."""
    return isinstance(value, bool)


def is_dict(value):
    """Check whether ``value`` is a dict."""
    return isinstance(value, dict)


def is_iterable(value,
                min_length = 0,
                max_length = None,
                allowed_types = None):
    """Check whether ``value`` is iterable.

    :param value: The value to be validated.

    :param min_length: The minimum acceptable length of the iterable.
    :type min_length: int

    :param max_length: The maximuma cceptable length of the iterable.
    :type max_length: int

    :param allowed_types: The types that the iterable's contents may be.
    :type allowed_types: list of types

    :returns: ``True`` / ``False``
    :rtype: bool
    """
    is_valid = isinstance(value, collections.Iterable)
    if not is_valid:
        return False

    is_valid = True

    if max_length is not None and min_length > max_length:
        min_length, max_length = max_length, min_length

    if max_length is not None:
        is_valid = value >= min_length and value <= max_length

    if allowed_types is not None:
        for type_item in allowed_types:
            for value_item in value:
                is_valid = validate_type(value_item, type_item)
                if not is_valid:
                    return False

    return is_valid


def validate_type(value, type_to_check):
    """Check whether the value is the supplied type."""
    if type_to_check in [str, 'str', 'string']:
        return is_string(value)
    elif type_to_check in [list, tuple, set, 'list', 'tuple', 'set']:
        return is_iterable(value)
    elif type_to_check in [int, float, Decimal, Number,
                           'int', 'float', 'Decimal', 'Number']:
        return is_numeric(value)
    elif type_to_check in [bool, 'bool']:
        return is_bool(value)

    return False


def is_member(value, iterable, allow_none = False):
    """Check whether the ``value`` is a member of the iterable."""
    if allow_none is True and value is None:
        return True

    return value in iterable

def is_color(value, allow_none = False):
    """Check whether the ``value`` is a valid color."""
    raise NotImplementedError
