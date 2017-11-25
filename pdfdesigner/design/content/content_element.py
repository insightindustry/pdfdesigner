# -*- coding: utf-8 -*-

"""
pdfdesigner.design.content.content_element
######################################

Implements the base class for defining :term:`Content Elements <Content Element>.`

"""
import uuid
import pdfdesigner
from pdfdesigner.design.content import Style


class ContentElement(object):
    """Object representation of a :term:`Content Element`."""

    def __init__(self,
                 style = None):
        """Create the :class:`ContentElement` and populate basic attributes."""
        self.id = uuid.uuid4()
        self._style = None
        self._has_flowed = False

        if style is None:
            style = pdfdesigner.get_default_style()

        self.set_style(style)

    def __repr__(self):
        """Return a string representation of the :class:`ContentElement` object."""
        return_tuple = ('ContentElement(style = {})'
                        .format(self.style))

        return ''.join(return_tuple)

    @property
    def name(self):
        """Alias the :ref:`ContentElement.id` attribute."""
        return self.id

    @name.setter
    def name(self, value):
        """Alias the :ref:`ContentElement.id` attribute."""
        self.id = value

    @property
    def style(self):
        """Return the :class:`Style` applied to this Paragraph."""
        return self._style

    def set_style(self, style):
        """Apply a :class:`Style` to the :class:`ContentElement`.

        :param style: A :class:`Style` or its name to apply to the
          :class:`ContentElement`.
        :type style: string / :class:`Style`

        :raises TypeError: If not a :class:`Style` or string.
        :raises ValueError: If a string, but the name is not in the PDF's
          :class:`Stylesheet`.
        """
        if not isinstance(style, Style) and not isinstance(style, str):
            raise TypeError('style must be either a string or a Style object')

        if isinstance(style, Style):
            self._style = style
        elif isinstance(style, str):
            if style not in pdfdesigner.get_stylesheet():
                raise ValueError('style ({}) is not present in the Stylesheet'
                                 .format(style))
            self._style = pdfdesigner.get_stylesheet()[style]

    @property
    def page_number(self):
        """Return the first page number on which the :term:`Content Element` appears."""
        return pdfdesigner.get_page_number(self.id, first_only = True)

    @property
    def page_numbers(self):
        """Return all page numbers where the :class:`ContentElement` appears.

        :rtype: tuple
        """
        return pdfdesigner.get_page_number(self.id, first_only = False)

    @property
    def container(self):
        """Return the first :class:`DesignTarget` that contains the :class:`ContentElement`.

        :rtype: :class:`DesignTarget` / ``None``
        """
        return pdfdesigner.get_container(self.id, first_only = True)

    @property
    def containers(self):
        """Return all :class:`DesignTargets <DesignTarget>` that contain the :class:`ContentElement`.

        :rtype: tuple / ``None``
        """
        return pdfdesigner.get_container(self.id, first_only = False)

    @property
    def is_flowable(self):
        """Return whether the :class:`ContentElement` can flow across :class:`DesignTarget`
          objects.

        :rtype: boolean
        """
        if self._style is None:
            return False

        return not self._style.keep_together

    @property
    def has_flowed(self):
        """Return whether the :class:`ContentElement` has flowed across
          :class:`DesignTargets <DesignTarget>`.

        :rtype: boolean
        """
        return self._has_flowed
