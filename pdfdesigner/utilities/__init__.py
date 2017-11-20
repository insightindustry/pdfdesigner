# -*- coding: utf-8 -*-

"""
######################
pdfdesigner.utilities
######################

Module defines (pure) utility functions.

"""
from numbers import Number


def is_numeric(value):
    """Check whether ``value`` is a numeric type.

    .. caution::
      Will also return ``True`` if passed a ``bool``, since in Python ``bool``
      is an ``int`` at heart.

    """
    return isinstance(value, Number)
