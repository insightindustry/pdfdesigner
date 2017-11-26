# -*- coding: utf-8 -*-

"""
pdfdesigner.design.content.content_element
######################################

Implements the base class for defining :term:`Content Elements <Content Element>.`

"""
import random
import string
import pdfdesigner
from pdfdesigner.design.content import Style


class ContentElement(object):
    """Object representation of a :term:`Content Element`."""

    def __init__(self,
                 name = None,
                 style = None):
        """Create the :class:`ContentElement` and populate basic attributes.

        :param style: The :class:`Style` which should be applied to the
          :class:`ContentElement`.
        :type style: :class:`Style`
        """
        self._name = name
        self.id = self.set_id(name)
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

    def set_id(self, value):
        """Set the object's :ref:`ContentElement.id` to the hash of ``value``.

        :param value: The value whose hash should be used as the object's ID.
        """
        hash_value = hash(value)
        self.id = hash_value

    @property
    def name(self):
        """Alias the :ref:`ContentElement.id` attribute."""
        if self._name is None:
            return self.id

        return self._name

    @name.setter
    def name(self, value):
        """Alias the :ref:`ContentElement.id` attribute."""
        if self._name is None:
            self._name = value
            self.set_id(value)

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
        """Return the first :class:`Container` that contains the :class:`ContentElement`.

        :rtype: :class:`Container` / ``None``
        """
        return pdfdesigner.get_container(self.id, first_only = True)

    @property
    def containers(self):
        """Return all :class:`Containers <Container>` that contain the :class:`ContentElement`.

        :rtype: tuple / ``None``
        """
        return pdfdesigner.get_container(self.id, first_only = False)

    @property
    def is_flowable(self):
        """Return whether the :class:`ContentElement` can flow across :class:`Container`
          objects.

        :rtype: boolean
        """
        if self._style is None:
            return False

        return not self._style.keep_together

    @property
    def has_flowed(self):
        """Return whether the :class:`ContentElement` has flowed across
          :class:`Containers <Container>`.

        :rtype: boolean
        """
        return self._has_flowed

    def get_required_width(self):
        """Return the object's minimum required width.

        :returns: ``None`` if there is no minimum required width, otherwise
          the number of points required.

        .. note::

          This method should be implemented in classes that inherit from
          :class:`ContentElement`.
        """
        return None

    def get_required_height(self, width = None):
        """Return the object's minimum required height to be drawn completely.

        :param width: The width to assume when calculating the required height.
        :type width: numeric

        :returns: ``None`` if there is no minimum required height, or if the
          object is :term:`Flowable Content`. Otherwise the height required.

        .. note::

          This method should be implemented in classes that inherit from
          :class:`ContentElement`.
        """
        if self.is_flowable:
            return None

        return None

    def will_fit(self, dimensions):
        """Check whether the :class:`ContentElement` will fit within the dimensions.

        :param dimensions: The ``(width, height)`` to check against.
        :type dimensions: tuple
        """
        will_fit = True

        if not isinstance(dimensions, tuple):
            raise TypeError('dimensions must be a tuple of form (width, height)')

        width = dimensions[0]
        height = dimensions[1]

        if width is None:
            raise ValueError('width cannot be None')
        if height is None:
            raise ValueError('height cannot be None')

        required_width = self.get_required_width()
        required_height = self.get_required_height(width = width)

        if required_width is not None and width < required_width:
            will_fit = False
        if required_height is not None and height < required_height:
            will_fit = False

        return will_fit
