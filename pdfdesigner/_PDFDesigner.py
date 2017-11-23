# -*- coding: utf-8 -*-

"""
pdfdesigner._PDFDesigner.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module defines the _PDFDesigner class, which is the internal (hidden) class
that is responsible for interfacing with the ReportLab library and actually
generating the PDF.
"""

import reportlab
from reportlab import platypus
from reportlab.platypus import FrameBreak, PageBreak, Frame, PageTemplate
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader

class _PDFDesigner(object):
    """The internal _PDFDesigner object that generates the PDF.

    You never call this class or inherit it directly. It is used internally
    within the :mod:`pdfdesigner` namespace.
    """
    pass
    
 class Singleton(object):
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    
    """
    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
