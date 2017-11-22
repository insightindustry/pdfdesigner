# -*- coding: utf-8 -*-

"""
pdfdesigner.design.content.styling
######################################

Implements classes related to styling PDF content.

"""

class Stylesheet(object):
    """
    Stores a collection of :class:`Style` objects that can be applied within a single PDF.

    :param name: the identifier given to the :class:`Stylesheet`
    :type name: string

    :param styles: a list of ::class:`Styles <Style>` that should be added to the
    stylesheet.
    :type styles: list, tuple, sequence, set


    """

    def __init__(self,
                 name = None,
                 styles = None,
                 based_on = None):
        """Creates a new Stylesheet object.

        Arguments:

        """
        self.name = name

        self.add_styles(styles)

        if based_on is not None:
            if not isinstance(based_on, Stylesheet):
                raise TypeError('Stylesheet constructor expects based_on to be another Stylesheet.')

            self.add_styles(based_on.styles)

    def add_style(self, style, overwrite = True):
        """Adds :class:`Style` object to the stylesheet.
        """
