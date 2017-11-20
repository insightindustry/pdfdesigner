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
