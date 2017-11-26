# -*- coding: utf-8 -*-

"""
pdfdesigner.design.layout.container
######################################

Implements the base class for defining :term:`Containers <Container>.`

"""
import pdfdesigner
from pdfdesigner.design.content import ContentElement, Style
from pdfdesigner.utilities import is_iterable, is_numeric
from pdfdesigner.utilities.constants import ORIGIN_POINTS


def _get_transform_from_origin(origin_point,
                               x = None,
                               y = None,
                               width = None,
                               height = None):
    """Get :term:`Transform Coordinates` given an :term:`Origin Point`.

    :param origin_point: The :term:`Origin Point` for the :term:`Transform`.
    :type origin_point: :class:`ORIGIN_POINTS`

    :param x: The x-coordinate of the :term:`Origin Point`.
    :type x: numeric

    :param y: The y-coordinate of the :term:`Origin Point`.
    :type y: numeric

    :param width: The width of the :term:`Transform`.
    :type width: numeric

    :param height: The height of the :term:`Transform`.
    :type height: numeric

    :returns: The :term:`Transform Coordinates` for the object.
    :rtype: ``tuple((x0, y0), (x1, y1))``
    """
    if not isinstance(origin_point, ORIGIN_POINTS):
        raise TypeError('origin_point must be an ORIGIN_POINTS enum')

    x0 = None
    y0 = None
    x1 = None
    y1 = None

    if origin_point in ORIGIN_POINTS.LEFT():
        x0 = x
        if width is not None:
            x1 = x + width
    if origin_point in ORIGIN_POINTS.RIGHT():
        x1 = x
        if width is not None:
            x0 = x - width

    if origin_point in ORIGIN_POINTS.TOP():
        y0 = y
        if height is not None:
            y1 = y + height
    if origin_point in ORIGIN_POINTS.BOTTOM():
        y1 = y
        if height is not None:
            y0 = y - height

    if origin_point in ORIGIN_POINTS.CENTER():
        if width is not None:
            x0 = x - (width * 0.5)
            x1 = x + (width * 0.5)

    if origin_point in ORIGIN_POINTS.MIDDLE():
        if height is not None:
            y0 = y + (height * 0.5)
            y1 = y - (height * 0.5)

    return x0, y0, x1, y1


class Container(object):
    """Object representation of a :term:`Container`."""

    def __init__(self,
                 name,
                 contents = None,
                 style = None,
                 origin_point = ORIGIN_POINTS.TOP_LEFT,
                 origin_coordinate = None,
                 width = None,
                 height = None,
                 transform_coordinates = None,
                 layer = 0):
        """Create a :class:`Container` instance.

        :param name: The human-readable name given to the :class:`Container`.
        :type name: string

        :param contents: The :class:`ContentElements <ContentElement>` that
          should be drawn inside this :class:`Container`.
        :type contents: Iterable of :class:`ContentElement` objects.

        :param style: The :class:`Style` which should be applied to the
          :class:`Container`.
        :type style: :class:`Style`

        :param origin_point: The :term:`Transform Coordinate` whose position will
          be determined by ``origin_coordinate``.
        :type origin_point: :class:`ORIGIN_POINT`

        :param origin_coordinate: The position of the :class:`Container's <Container>`
          :term:`Origin Point`.
        :type origin_coordinate: ``None`` / ``tuple(x, y)``

        :param width: The :class:`Container's <Container>` width.
        :type width: numeric

        :param height: The :class:`Container's <Container>` height.
        :type height: numeric

        :param transform_coordinates: Collection of coordinates that explicitly
          determine the :class:`Container's <Container>` position and dimensions.
        :type transform_coordinates: ``None`` or tuple of four tuples of the form::

            ((top_left_x, top_left_y), (top_right_x, top_right_y),
             (bottom_left_x, bottom_left_y), (bottom_right_x, bottom_right_y))

          or tuple of two tuples of the form::

            ((top_left_x, top_left_y), (bottom_right_x, bottom_right_y))

        :raises ValueError: If ``transform_coordinates`` and ``origin_coordinate``
          are both supplied.

        """
        if transform_coordinates is not None and origin_coordinate is not None:
            raise ValueError('Container cannot have both transform_coordinates ' +
                             'and origin_coordinate.')

        self.id = hash(name)
        self.name = name
        self._contents = {}
        self._content_ids = []
        self.origin_point = origin_point
        self._width = width
        self._height = height
        self.layer = layer

        self._x0 = None
        self._y0 = None
        self._x1 = None
        self._y1 = None

        self._style = None
        if style is None:
            style = pdfdesigner.get_default_style()
        self.set_style(style)

        if transform_coordinates is not None:
            self.set_transform_coordinates(transform_coordinates)
        elif origin_coordinate is not None:
            self.set_transform_coordinates(origin_coordinate)

        if contents is not None:
            self.add_contents(contents)

    def __repr__(self):
        """Return a string representation of the :class:`Container`."""
        return_string = 'Container(name={}, '.format(self.name) + \
                        'contents={}, '.format(self._contents) + \
                        'style={}, '.format(self.style.name) + \
                        'origin_point={}, '.format(self.origin_point) + \
                        'width={}, '.format(self._width) + \
                        'height={}, '.format(self._height) + \
                        'origin_coordinate={}'.format(self.origin_coordinate) + \
                        'layer={})'.format(self.layer)

        return return_string

    def __len__(self):
        """Return the number of :class:`ContentElements <ContentElement>`."""
        return len(self._content_ids)

    def __iter__(self):
        """Return an iterator over the :class:`Container` contents."""
        return iter(self._contents.values())

    def __contains__(self, item):
        """Return whether the :class:`Container` has ``item`` in its content."""
        if isinstance(item, ContentElement):
            return item.id in self._content_ids

        if isinstance(item, str):
            item_hash = hash(item)

            return item_hash in self._content_ids

        if is_numeric(item):
            return item in self._content_ids

        return False

    def __add__(self, other):
        """Add the value of ``other`` to the :class:`Container` based on its type.

        :param other: The object to add to the :class:`Container`.
        :type other: :class:`ContentElement` / :class:`Container`

        :returns: The modified :class:`Container` object or the created
          :class:`Story` object.

        """
        if isinstance(other, ContentElement):
            self.add_content_element(other)

            return self

        if isinstance(other, Container):
            raise NotImplementedError()

    def __sub__(self, other):
        """Remove the value of ``other`` from the :class:`Container`.

        :param other: The :class:`ContentElement` to remove.
        :type other: :class:`ContentElement`

        :returns: The :class:`Container` object
        :rtype: :class:`Container`

        :raises TypeError: If ``other`` is not a :class:`ContentElement` object.
        """
        if not isinstance(other, ContentElement):
            raise TypeError('Only ContentElement objects can be subtracted from ' +
                            'Container objects.')

        self.remove_content_element(other)

        return self

    @property
    def style(self):
        """Return the :class:`Style` applied to this :class:`Container`."""
        return self._style

    def set_style(self, style):
        """Apply a :class:`Style` to the :class:`Container`.

        :param style: A :class:`Style` or its name to apply to the
          :class:`Container`.
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
    def width(self):
        """Return the :class:`Container's <Container>` width."""
        if self._width is not None:
            width = self._width
        else:
            width = pdfdesigner.get_page(self.page_number).live_area_width

        return width

    @property
    def height(self):
        """Return the :class:`Container's <Container>` height."""
        if self._height is not None:
            height = self._height
        else:
            page = pdfdesigner.get_page(self.page_number)
            height = page.get_available_height(self.id)

        return height

    @property
    def dimensions(self):
        """Return dimensions as a tuple ``(width, height)``."""
        return (self.width, self.height)

    @property
    def left(self):
        """Return the x-coordinate of the :term:`Bounding Box's <Bounding Box>`
          left edge."""
        return self._x0

    @property
    def right(self):
        """Return the x-coordinate of the :term:`Bounding Box's <Bounding Box>`
          right edge."""
        return self._x1

    @property
    def top(self):
        """Return the y-coordinate of the :term:`Bounding Box's <Bounding Box>`
          top edge."""
        return self._y0

    @property
    def bottom(self):
        """Return the y-coordinate of the :term:`Bounding Box's <Bounding Box>`
          bottom edge."""
        return self._y1

    @property
    def origin(self):
        """Return the origin coordinate for the :term:`Transform`."""
        origin_point = self.origin_point
        height = self.height
        width = self.width

        if origin_point in ORIGIN_POINTS.TOP():
            origin_y = self.top
        elif origin_point in ORIGIN_POINTS.MIDDLE():
            if height is not None:
                origin_y = self.top + (height * 0.5)
            else:
                origin_y = None
        elif origin_point in ORIGIN_POINTS.BOTTOM():
            origin_y = self.bottom

        if origin_point in ORIGIN_POINTS.LEFT():
            origin_x = self.left
        elif origin_point in ORIGIN_POINTS.CENTER():
            if width is not None:
                origin_x = self.left + (width * 0.5)
            else:
                origin_x = None
        elif origin_point in ORIGIN_POINTS.RIGHT():
            origin_x = self.right

        return (origin_x, origin_y)

    @property
    def transform_coordinates(self):
        """Return the :class:`Container's <Container>` :term:`Transform Coordinates`."""
        return ((self.left, self.top),
                (self.right, self.bottom))

    def set_transform_coordinates(self, coordinates):
        """Set the :class:`Container's <Container>` :term:`Transform Coordinates`.

        :param coordinates: Coordinates on the :term:`Page`.
        :type coordinates: ``tuple(x, y)`` or ``tuple((x0, y0), (x1, y1))`` or
          ``tuple((x0, y0), (x1, y0), (x0, y1), (x1, y1))``

        """
        if not isinstance(coordinates, tuple):
            raise TypeError('coordinates must be a tuple')

        if len(coordinates == 4):
            x0 = coordinates[0][0]
            y0 = coordinates[0][1]

            x1 = coordinates[1][0]
            y1 = coordinates[1][1]
        elif len(coordinates == 2):
            if isinstance(coordinates[0], tuple):
                x0 = coordinates[0][0]
                y0 = coordinates[0][1]

                x1 = coordinates[1][0]
                y1 = coordinates[1][1]
            else:
                x0, y0, x1, y1 = _get_transform_from_origin(self.origin_point,
                                                            x = coordinates[0],
                                                            y = coordinates[1])

        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    @property
    def center_coordinates(self):
        """Return coordinates for the :class:`Container's <Container>` center point."""
        width = self.width
        height = self.height
        left = self.left
        top = self.top

        if width is None or height is None:
            return None

        center_x = left + (width * 0.5)
        center_y = top + (height * 0.5)

        return (center_x, center_y)

    @property
    def page_number(self):
        """Return the page number on which the :class:`Container` appears."""
        return pdfdesigner.get_page_number(self.id)

    def add_contents(self, contents):
        """Add :class:`ContentElements <ContentElement>` to the :class:`Container`.

        :param contents: The :class:`ContentElements <ContentElement>` that
          should be drawn inside this :class:`Container`.
        :type contents: Iterable of :class:`ContentElement` objects.

        """
        if not is_iterable(contents, min_length = 1):
            raise TypeError('contents must be iterable')

        for element in contents:
            self.add_content_element(element)

    def add_content_element(self,
                            content_element):
        """Add a single :class:`ContentElement` to the :class:`Container`.

        :param content_element: The :class:`ContentElement` that should be added
          to this :class:`Container`.
        :type contents: :class:`ContentElement`

        :raises ValueError: If the :class:`ContentElement` is not
          :term:`flowable <Flowable Content>` and will not fit within the
          :class:`Container`.

        """
        if not isinstance(content_element, ContentElement):
            raise TypeError('content_element must be a ContentElement object')

        if not content_element.is_flowable and \
           not content_element.will_fit(self.dimensions):
            raise ValueError('{cls}({content}) will not fit in Container '
                             .format(cls = content_element.__class__.__name__,
                                     content = str(content_element)) +
                             '{container} with dimensions {dimensions}'
                             .format(container = self.name,
                                     dimensions = self.dimensions))

        self._contents[content_element.id] = content_element
        self._content_ids.append(content_element.id)

    def remove_content_element(self,
                               content_element,
                               fail_silently = True):
        """Remove the ``content_element`` from the :class:`Container`.

        :param content_element: The :class:`ContentElement` to remove.
        :type content_element: string / numeric / :class:`ContentElement`

        :param fail_silently: If ``True``, will return ``None`` if
          :class:`ContentElement` was not found.
        :type fail_silently: bool

        :raises LookupError: If ``fail_silently is False`` and :class:`ContentElement`
          was not found.

        :returns: The :class:`ContentElement` removed.
        """
        if content_element in self:
            self._content_ids.remove(content_element.id)
            return self._contents.pop(content_element.id, None)

        if fail_silently is True:
            return None
        else:
            raise LookupError("Content Element ({}) was not found in Container {}"
                              .format(content_element.id,
                                      self.name))

    def clear_content_elements(self):
        """Remove all :class:`ContentElements <ContentElement>` from the
          :class:`Container`.
        """
        self._contents = {}
        self._content_ids = []
