# -*- coding: utf-8 -*-

"""Tests for pdfdesigner.design.content.stylesheet.Style."""

import pytest
from pdfdesigner.design.content import Style, Stylesheet
from pdfdesigner.utilities import random_string
from pdfdesigner.defaults import DEFAULT_STYLESHEET

@pytest.fixture
def default_style():
    """Return a default :class:`Style` with a random ``name``."""
    name = random_string(6)

    return Style(name)


def test_create_stylesheet(default_style1 = default_style,
                           default_style2 = default_style,
                           default_style3 = default_style):
    """Test creation of a stylesheet with styles passed in argument."""
    style1 = default_style1()
    style2 = default_style2()
    style3 = default_style3()

    assert style1 != style2
    assert style2 != style3
    assert style1 != style3

    style2.name = 'style2'
    style3.name = 'style3'

    new_stylesheet = Stylesheet('default',
                                styles = [
                                    style1,
                                    style2,
                                    style3
                                ])

    assert new_stylesheet.name == 'default'
    assert style1.name in new_stylesheet
    assert style1 in new_stylesheet

    assert style2.name in new_stylesheet
    assert style2 in new_stylesheet

    assert new_stylesheet[style1.name] == style1
    assert new_stylesheet.style2 == style2
    assert new_stylesheet.style3 == style3

    assert new_stylesheet.based_on is None


def test_based_on():
    """Test stylesheet creation using ``based_on`` argument."""
    new_stylesheet = Stylesheet('stylesheet2',
                                based_on = DEFAULT_STYLESHEET)

    assert new_stylesheet != DEFAULT_STYLESHEET
    assert new_stylesheet.name == 'stylesheet2'
    assert new_stylesheet.based_on == DEFAULT_STYLESHEET.name
    assert len(new_stylesheet) == len(DEFAULT_STYLESHEET)
    assert 'Normal' in new_stylesheet
    assert new_stylesheet.Normal is not None
    assert 'Heading 1' in new_stylesheet
    assert new_stylesheet['Heading 1'] is not None
    assert new_stylesheet.heading1 is not None
    assert new_stylesheet.heading1 == new_stylesheet['Heading 1']


def test_has_style():
    """Test whether :ref:`Stylesheet.has_style()` returns valid value."""
    assert 'Heading 1' in DEFAULT_STYLESHEET
    assert DEFAULT_STYLESHEET.has_style('Heading 1') == ('Heading 1' in DEFAULT_STYLESHEET)
    assert 'Heading 9' not in DEFAULT_STYLESHEET
    assert DEFAULT_STYLESHEET.has_style('Heading 9') == ('Heading 9' in DEFAULT_STYLESHEET)
