# -*- coding: utf-8 -*-

"""
pdfdesigner.design.content.fonts
######################################

Implements functions related to managing fonts.

"""
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from pdfdesigner.utilities import is_iterable

_FONT_VARIANTS = {
    'NORMAL': 'normal',
    'BOLD': 'bold',
    'ITALIC': 'italic',
    'BOLD-ITALIC': 'boldItalic'
}


class FontDefinition(object):
    """Properties and methods used to define a TrueType Font usable within your PDF."""

    def __init__(self,
                 name,
                 tt_filename,
                 variant = 'NORMAL'):
        """Create a FontDefinition object.

        :param name: The name used to identify the Font.
        :type name: string

        :param tt_filename: The filename where the font can be found. Must point
          to a TrueType font file.
        :type tt_filename: string

        :param variant: The :term:`Font Variant` that the font file contains.
        :type variant: member of ('NORMAL', 'BOLD', 'ITALIC', 'BOLD-ITALIC')

        :raises TypeError: If one of the arguments received is not a string.
        :raises ValueError: If ``variant`` is not a recognized variant.

        """
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        if not isinstance(tt_filename, str):
            raise TypeError('tt_filename must be a string')
        if not isinstance(variant, str):
            raise TypeError('variant must be a string')
        if variant not in _FONT_VARIANTS:
            raise ValueError('variant ({value}) is an invalid value'
                             .format(value = variant))

        self.name = name
        self.tt_filename = tt_filename
        self.variant = variant
        self._is_registered = False

    @property
    def is_registered(self):
        """Return ``True`` if the font has been registered with ReportLab."""
        return self._is_registered

    def register(self):
        """Register the Font Definition with PDFMetrics."""
        pdfmetrics.registerFont(self.to_ttfont())
        self._is_registered = True

    def to_ttfont(self):
        """Return a ReportLab ``TTFont`` object representation of the Font."""
        return TTFont(self.name, self.tt_filename)


def register_font_family(family_name,
                         fonts = None):
    """Register a set of :term:`Font Variants <Font Variant>` in a :term:`Font Family`.

    :param family_name: The name of the :term:`Font Family`.
    :type family_name: string

    :param fonts: An iterable of :term:`Font Definition` objects that are members
      of the :term:`Font Family`.
    :type fonts: iterable of :class:`FontDefinition`.

    :raises TypeError: If ``family_name`` is not a string, ``fonts`` is not
      iterable, or ``fonts`` does not contain :class:`FontDefinition` objects.
    :raises ValueError: If ``fonts`` is None or an empty iterable.

    """
    if not isinstance(family_name, str):
        raise TypeError('family_name must be a string')

    if fonts is None:
        raise ValueError('fonts cannot be None')
    if len(fonts) == 0:
        raise ValueError('must provide at least one font')

    if not is_iterable(fonts, min_length = 1):
        raise TypeError('fonts must be iterable')

    variants = {}

    for item in fonts:
        if not isinstance(item, FontDefinition):
            raise TypeError('fonts must contain FontDefinition objects')

        if not item.is_registered:
            item.register()
        variants[_FONT_VARIANTS[item.variant]] = item.name

    pdfmetrics.registerFontFamily(family_name, **variants)
