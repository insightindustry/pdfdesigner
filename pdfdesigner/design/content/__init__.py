# -*- coding: utf-8 -*-

"""
###########################
pdfdesigner.design.content
###########################

This subpackage defines classes used to represent content in your PDF.

"""

from .paragraph import Paragraph
# from .image import Image
# from .table import Table
from .stylesheet import Stylesheet, Style
from .fonts import FontDefinition, register_font_family

__all__ = [
    'Paragraph',
    'Image',
    'Table',
    'Stylesheet',
    'Style',
    'FontDefinition',
    'register_font_family'
]
