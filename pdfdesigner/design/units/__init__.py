# -*- coding: utf-8 -*-

"""
#########################
pdfdesigner.design.units
#########################

Defines constants used to represent units of measurement.

"""

#: Base unit of measurement used by PDFDesigner.
POINT = 1.0

#: 12.0 points
PICA = 12.0

#: 72.0 points
INCH = 72.0

#: 28.3464 points
CM = 72.0 * 0.3937

#: 0.10 centimeters
MM = CM * 0.1

#: A constant that is dynamically scaled based on the PDFDesigner's configuration
#: settings.
GRID_COLUMN = -99

__all__ = [
    'POINT',
    'PICA',
    'INCH',
    'CM',
    'MM',
    'GRID_COLUMN'
]
