# -*- coding: utf-8 -*-

"""
###########################
pdfdesigner.design.content
###########################

This subpackage defines classes used to represent content in your PDF.

*********
Classes:
*********

    :class:`Paragraph` - Used to represent a paragraph of text.

    :class:`Image` - Used to represent a graphical image.

    :class:`Table` - Used to represent a table of content.

    :class:`Stylesheet` - Used to represent a collection of
    :term:`Styles <Style>` that can be applied to content and layout in your
    PDF.
"""

# from .paragraph import Paragraph
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
