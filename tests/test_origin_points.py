# -*- coding: utf-8 -*-

"""Tests for pdfdesigner.utilities.constants.ORIGIN_POINTS."""

from pdfdesigner.utilities.constants import ORIGIN_POINTS


def test_in_LEFT():
    """Test whether membership checking methods work in :class:`ORIGIN_POINTS`."""
    test_value = ORIGIN_POINTS.TOP_LEFT

    assert test_value in ORIGIN_POINTS.LEFT()
