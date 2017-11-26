# -*- coding: utf-8 -*-

"""
###########################
pdfdesigner.design.content
###########################

This subpackage defines classes used to represent content in your PDF.

"""

# from .image import Image
# from .table import Table
from .stylesheet import Stylesheet, Style
from .content_element import ContentElement
from .paragraph import Paragraph
from .fonts import FontDefinition, register_font_family

__all__ = [
    'ContentElement',
    'Paragraph',
    #'Image',
    #'Table',
    'Stylesheet',
    'Style',
    'FontDefinition',
    'register_font_family'
]
