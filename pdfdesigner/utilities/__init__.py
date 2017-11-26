# -*- coding: utf-8 -*-

"""
######################
pdfdesigner.utilities
######################

Module defines (pure) utility functions.

"""
import random
import string
import re
import collections
from collections import namedtuple
from numbers import Number
from decimal import Decimal
from keyword import iskeyword

from pdfdesigner.defaults import DEFAULT_COLORS

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

#: A named tuple which defines a property that may or may not map to a ReportLab setting.
PropertyReference = namedtuple('PropertyReference',
                               'default reportlab_key validation parameters conversion')


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


def is_tuple(value, length = None, expected_type = None):
    """Check whether the value is a ``tuple``.

    :param value: The value to check.

    :param length: The expected length of the ``tuple``.
    :type length: int

    :param expected_type: A tuple containing validation functions to apply
      against the value's members.
    :type expected_type: tuple

    :returns: ``True`` if ``value`` meets expectations, otherwise ``False``.
    :rtype: bool

    """
    if not isinstance(value, tuple):
        return False

    if expected_type is not None and not isinstance(expected_type, tuple):
        raise TypeError('expected_type expects to be a tuple')

    if length is None and expected_type is not None:
        length = len(expected_type)

    if length is not None:
        if len(value) != length:
            return False

    if expected_type is not None:
        for index, validation_operation in enumerate(expected_type):
            validation_function = validation_operation['function']
            validation_parameters = validation_operation['parameters']

            if validation_parameters is not None:
                is_valid = validation_function(value[index], **validation_parameters)
            else:
                is_valid = validation_function(value[index])

            if not is_valid:
                return False

    return True


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
    if value is None:
        return allow_none

    if isinstance(value, Color):
        is_valid = True

    if isinstance(value, str) and value in DEFAULT_COLORS:
        is_valid = True
    elif isinstance(value, str):
        try:
            color = HexColor(value)
            is_valid = True
        except (TypeError, ValueError):
            is_valid = False

    if is_iterable(value, min_length = 3, max_length = 4):
        try:
            color = Color(**value)
            is_valid = True
        except (TypeError, ValueError):
            is_valid = False

    return is_valid


def make_lowercase(value):
    """Return a lowercase version of the value."""
    return value.lower()


def random_string(length):
    """Return a random string of ``length`` lowercase characters."""
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def make_identifier(value, lowercase = True):
    """Return of the ``value`` that is safe for use in attributes."""
    if lowercase is True:
        value = value.lower()

    if iskeyword(value):
        raise ValueError('value ({value}) cannot be a Python keyword'.format(value = value))

    if not value.isidentifier():
        value = re.sub('[^0-9a-zA-Z_]', '', value)
        value = re.sub('^[^a-zA-Z_]+', '', value)

    return value


def hex_to_rgb(hex_color, percentage = False):
    """Return a tuple of form ``(red, green, blue)`` representing the color.

    :param hex_color: The color expressed in hexadecimal.
    :type hex_color: string

    :param percentage: Indicates that the RGB value returned should be expressed
      as a percentage of the color gradient (e.g. white would be R:1, G:1, B:1
      and not R:255, G:255, B:255).
    :type percentage: bool

    :returns: The color expressed as ``(red, green, blue)``.
    :rtype: tuple
    """
    hex_color = hex_color.lstrip('#')
    length = len(hex_color)
    return_value = tuple(int(hex_color[i:i + length // 3], 16) for i in range(0,
                                                                              length,
                                                                              length // 3)
                         )

    if percentage is True:
        red = return_value[0] / 255
        green = return_value[1] / 255
        blue = return_value[2] / 255

        return_value = (red, green, blue)

    return return_value


def convert_alignment(value):
    """Return a ReportLab Platypus-compatible alignment value."""
    conversion_dict = {
        'LEFT': TA_LEFT,
        'RIGHT': TA_RIGHT,
        'CENTER': TA_CENTER,
        'JUSTIFY': TA_JUSTIFY
    }

    if value not in conversion_dict:
        raise ValueError('value ({value}) is not a valid alignment'
                         .format(value = value))

    return conversion_dict[value]


def increment_name(name,
                 current_count = 0):
    """Increment ``current_count`` and append it to ``name``."""
    if not isinstance(name, str):
        raise TypeError('name must be a string')

    name += '_{}'.format(current_count + 1)

    return name
