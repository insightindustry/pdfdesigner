# -*- coding: utf-8 -*-

"""Tests for pdfdesigner.design.content.stylesheet.Style."""

import pytest
from pdfdesigner.design.content import Style
from pdfdesigner.utilities import random_string

@pytest.fixture
def default_style():
    """Return a default :class:`Style` with a random ``name``."""
    name = random_string(6)

    return Style(name)


def test_default_style(default_style):
    """Test a default style is initialized with expected values."""
    assert default_style is not None
    assert default_style.font_name == 'Helvetica'
    assert default_style.font_size == 10


def test_init_from_style():
    """Test whether :class:`Style`` respects the ``from_style`` argument."""
    style1 = Style('style1',
                   font_size = 24)
    style2 = Style('style2',
                   from_style = style1,
                   font_size = 8)

    assert style1._from_style is None
    assert style1.font_size == 24
    assert style1.name == 'style1'
    assert style2.name == 'style2'
    assert style2._from_style == 'style1'
    assert style2.font_size == 8


def test_from_style():
    """Test the :ref:`Style.from_style()` method."""
    style1 = Style('style1',
                   font_size = 24)
    style2 = Style.from_style('style2', style1)

    assert style1._from_style is None
    assert style2.name == 'style2'
    assert style2._from_style == 'style1'
    assert style2.font_size == 24


def test_to_platypus():
    """Test the :ref:`Style.to_platypus()` method."""
    style1 = Style('style1',
                   font_size = 24,
                   text_transformation = 'UPPERCASE')
    rl_style = style1.to_platypus()

    assert style1.name == 'style1'
    assert rl_style.fontSize == 24
    assert rl_style.textTransform == 'uppercase'
