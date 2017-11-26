# -*- coding: utf-8 -*-

"""
pdfdesigner.utilities.constants
######################################

Exports a variety of constants used by the **PDFDesigner**.

"""

from enum import Enum


class ORIGIN_POINTS(Enum):
    """Set of constants used to indicate a :term:`transform's <Transform>`
      :term:`Origin Point`.
    """

    TOP_LEFT = 0
    TOP_CENTER = 1
    TOP_RIGHT = 2
    MIDDLE_LEFT = 3
    MIDDLE_CENTER = 4
    MIDDLE_RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM_CENTER = 7
    BOTTOM_RIGHT = 8

    @classmethod
    def LEFT(cls):
        """Return a list of the attributes that are along the left edge."""
        return [cls.TOP_LEFT,
                cls.MIDDLE_LEFT,
                cls.BOTTOM_LEFT]

    @classmethod
    def CENTER(cls):
        """Return a list of the attributes that are along the center."""
        return [cls.TOP_CENTER,
                cls.MIDDLE_CENTER,
                cls.BOTTOM_CENTER]

    @classmethod
    def RIGHT(cls):
        """Return a list of the attributes that are along the right edge."""
        return [cls.TOP_RIGHT,
                cls.MIDDLE_RIGHT,
                cls.BOTTOM_RIGHT]

    @classmethod
    def TOP(cls):
        """Return a list of the attributes that are along the top edge."""
        return [cls.TOP_LEFT,
                cls.TOP_CENTER,
                cls.TOP_RIGHT]

    @classmethod
    def MIDDLE(cls):
        """Return a list of the attributes that are long the middle."""
        return [cls.MIDDLE_LEFT,
                cls.MIDDLE_CENTER,
                cls.MIDDLE_RIGHT]

    @classmethod
    def BOTTOM(cls):
        """Return a list of the attributes that are along the bottom edge."""
        return [cls.BOTTOM_LEFT,
                cls.BOTTOM_CENTER,
                cls.BOTTOM_RIGHT]
