# -*- coding: utf-8 -*-

"""
********************
PDFDesginer
********************

PDFDesigner is a library that aids in the generation of beautifully-designed PDFs.

Basic usage:

    >>> import pdfdesigner
    >>> from pdfdesigner.design.layout import Page
    >>> from pdfdesigner.design.content import Paragraph, Story
    >>> from pdfdesigner.defaults import DEFAULT_STYLES
    >>>
    >>> title = Paragraph("Great Expectations", style = "title")
    >>> by_line = Paragraph("by Charles Dickens", style = "subtitle")
    >>> title_page = title + by_line
    >>>
    >>> chapter_heading = Paragraph("Chapter 1", style = "heading1")
    >>> chapter1 = Story(style = "normal").from_textfile("chapter1.txt")
    >>> other_pages = chapter_heading + chapter1
    >>>
    >>> pdfdesigner.add_page(title_page, template = "title_page")
    >>> pdfdesigner.add_section(other_pages, template = "chapter")
    >>>
    >>> pdfdesigner.generate_pdf()

Verbose and complex design functionality is supported, with a robust public API.
Full documentation is at <http://pdfdesigner.readthedocs.io>.

Functions:
==========

    .. todo:: Add list of functions.

Modules:
========

    :mod:`exceptions <pdfdesigner.exceptions>` - Custom exceptions generated by
    PDFDesigner when it encounters a problem.

Subpackages:
============

    :mod:`defaults <pdfdesigner.defaults>` - Constants used to define default
    behavior.

    :mod:`design <pdfdesigner.design>` - Classes that are used to assemble your
    content into a beautiful PDF.

    :mod:`templates <pdfdesigner.templates>` - Classes that are used to
    instantiate templates used by your PDF.

:copyright: (c) 2017 Insight Industry Inc.
:license: MIT, see LICENSE for more details
"""

import warnings

from ._PDFDesigner import _PDFDesigner
from pdfdesigner.design.content import register_font_family as _register_font_family


def register_font_family(family_name, fonts = None):
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
    _register_font_family(family_name, fonts)


def get_stylesheet():
    """Return the :class:`_PDFDesigner` instance's configured stylesheet."""
    raise NotImplementedError()


def get_default_style():
    """Return the :class:`_PDFDesigner` instance's configured default style."""
    raise NotImplementedError()


def get_page_number(item_id,
                    first_only = False):
    """Return the page number on which a given item appears.

    :param item_id: The ``id`` of the object who's page number should be returned.

    :param first_only: If ``True``, will return the first page number where the
      item appears. If ``False``, will return all page numbers.

    :returns: The :term:`page number(s) <Page Number>` (non zero-indexed).
    :rtype: int or tuple

    """
    raise NotImplementedError()


def get_component(item_id):
    """Return the :term:`Content Element` or :term:`Design Target` identified
      by ``item_id``.

    :param item_id: The ``id`` of the object who's page number should be returned.

    :returns: The content identified by ``item_id``.

    """
    raise NotImplementedError()


def get_container(item_id,
                  first_only = False):
    """Return the :term:`Design Target` that contains the :class:`ContentElement`
      identified by ``item_id``.

    :param item_id: The ``id`` of the :class:`ContentElement` who's container
      should be returned.

    :param first_only: If ``True``, returns the first :class:`DesignTarget` where
      the :class:`ContentElement` appears. If ``False``, returns a tuple with all
      of them.

    :returns: The :class:`DesignTarget` identified by ``item_id``.
    :rtype: :class:`DesignTarget` / ``None`` / tuple
    """
    raise NotImplementedError()
