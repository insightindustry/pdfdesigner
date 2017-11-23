# -*- coding: utf-8 -*-

"""
pdfdesigner.design.content.styling
######################################

Implements classes related to styling PDF content.

"""
from collections import namedtuple
from pdfdesigner.defaults import DEFAULT_SETTINGS
from pdfdesigner.utilities import is_numeric, is_string, is_member, is_color, is_boolean, is_none

PropertyReference = namedtuple('PropertyReference',
                               'default reportlab_key validation parameters')
_STYLE_PROPERTIES = {
    'font_name': PropertyReference(DEFAULT_SETTINGS.base_font_name,
                                   'fontName',
                                   is_string,
                                   None),
    'font_size': PropertyReference(10,
                                   'fontSize',
                                   is_numeric,
                                   None),
    'leading': PropertyReference(12,
                                 'leading',
                                 is_numeric,
                                 None),
    'left_indent': PropertyReference(0,
                                     'leftIndent',
                                     is_numeric,
                                     None),
    'right_indent': PropertyReference(0,
                                      'rightIndent',
                                      is_numeric,
                                      None),
    'first_line_indent': PropertyReference(0,
                                           'firstLineIndent',
                                           is_numeric,
                                           None),
    'alignment': PropertyReference('LEFT',
                                   'alignment',
                                   is_member,
                                   {
                                       'iterable': ['LEFT',
                                                    'CENTER',
                                                    'RIGHT',
                                                    'JUSTIFY'],
                                       'allow_none': False
                                   }),
    'space_before': PropertyReference(0,
                                      'spaceBefore',
                                      is_numeric,
                                      None),
    'space_after': PropertyReference(0,
                                     'spaceAfter',
                                     is_numeric,
                                     None),
    'bullet_font_name': PropertyReference(DEFAULT_SETTINGS.base_font_name,
                                          'bulletFontName',
                                          is_string,
                                          None),
    'bullet_font_size': PropertyReference(10,
                                          'bulletFontSize',
                                          is_numeric,
                                          None),
    'bullet_indent': PropertyReference(0,
                                       'bulletIndent',
                                       is_numeric,
                                       None),
    'bullet_color': PropertyReference('BLACK',
                                      'bulletColor',
                                      is_color,
                                      {
                                          'allow_none': True
                                      }),
    'bullet_offset_y': PropertyReference(0,
                                         'bulletOffsetY',
                                         is_numeric,
                                         None),
    'bullet_direction': PropertyReference('LTR',
                                          'bulletDir',
                                          is_member,
                                          {
                                              'iterable': [
                                                  'LTR',
                                                  'RTL',
                                                  'CJK'
                                              ],
                                              'allow_none': False
                                          }),
    'bullet_dedent': PropertyReference('AUTO',
                                       'bulletDedent',
                                       is_member,
                                       {
                                           'iterable': [
                                               'AUTO'
                                           ],
                                           'allow_none': False
                                       }),
    'bullet_start': PropertyReference(None,
                                      'bulletStart',
                                      is_string,
                                      None),
    'bullet_format': PropertyReference(None,
                                       'bulletFormat',
                                       is_none,
                                       None),
    'text_color': PropertyReference('BLACK',
                                    'textColor',
                                    is_color,
                                    {
                                        'allow_none': True
                                    }),
    'background_color': PropertyReference(None,
                                          'backColor',
                                          is_color,
                                          {
                                              'allow_none': True
                                          }),
    'word_wrap': PropertyReference(None,
                                   'wordWrap',
                                   is_member,
                                   {
                                       'iterable': ['CJK',
                                                    'LTR',
                                                    'RTL'],
                                       'allow_none': True
                                   }),
    'border_width': PropertyReference(0,
                                      'borderWidth',
                                      is_numeric,
                                      None),
    'border_padding': PropertyReference(0,
                                        'borderPadding',
                                        is_numeric,
                                        None),
    'border_color': PropertyReference(None,
                                      'borderColor',
                                      is_color,
                                      {
                                          'allow_none': True
                                      }),
    'border_radius': PropertyReference(0,
                                       'borderRadius',
                                       is_numeric,
                                       None),
    'allow_widows': PropertyReference(True,
                                      'allowWidows',
                                      is_boolean,
                                      None),
    'allow_orphans': PropertyReference(False,
                                       'allowOrphans',
                                       is_boolean,
                                       None),
    'text_transformation': PropertyReference(None,
                                             'textTransform',
                                             is_member,
                                             {
                                                 'iterable': [
                                                     'uppercase',
                                                     'lowercase',
                                                 ],
                                                 'allow_none': True
                                             }),
    'split_long_words': PropertyReference(True,
                                          'splitLongWords',
                                          is_boolean,
                                          None),
    'underline_proportion': PropertyReference(DEFAULT_SETTINGS.underline_proportion,
                                              'underlineProportion',
                                              is_numeric,
                                              None),
    'bullet_anchor': PropertyReference('START',
                                       'bulletAnchor',
                                       is_member,
                                       {
                                           'iterable': ['START',
                                                        'MIDDLE',
                                                        'END'],
                                           'allow_none': False
                                       }),
    'justify_last_line': PropertyReference(False,
                                           'justifyLastLine',
                                           is_boolean,
                                           None),
    'justify_line_breaks': PropertyReference(False,
                                             'justifyBreaks',
                                             is_boolean,
                                             None),
    'space_shrinkage': PropertyReference(DEFAULT_SETTINGS.space_shrinkage,
                                         'spaceShrinkage',
                                         is_numeric,
                                         None)

}


def _get_default_style_properties():
    """Return a dictionary of style properties with default values set."""
    default_properties = {}
    for key in _STYLE_PROPERTIES:
        default_properties[key] = _STYLE_PROPERTIES[key].default

    return default_properties

class Stylesheet(object):
    """Store a collection of :class:`Style` objects that can be applied within a single PDF.

    :param name: the identifier given to the :class:`Stylesheet`
    :type name: string

    :param styles: Iterable of :class:`Style` objects that are to be included in
      the Stylesheet.
    :type styles: list/tuple/set

    :param based_on: A Stylesheet whose :class:`Styles <Style>` will be
      copied into the current object.
    :type based_on: :class:`Stylesheet`

    :raises TypeError: If the value of ``based_on`` is not a :class:`Stylesheet`.
    """

    def __init__(self,
                 name = None,
                 styles = None,
                 based_on = None):
        #: Name of the Stylesheet.
        self.name = name
        self._styles = {}
        self._based_on = None

        if based_on is not None:
            if not isinstance(based_on, Stylesheet):
                raise TypeError('Stylesheet constructor expects based_on to be another Stylesheet.')
            self._based_on = based_on.name

            self.add_styles(based_on.styles)

        self.add_styles(styles, overwrite = True)

    def __repr__(self):
        """Return a valid string representation of the Stylesheet."""
        repr_string = "Stylesheet: {self.name} ({self.id})\n\n"
        repr_string += "Stylesheet(name = {self.name}, based_on = {self._based_on})"

        return repr_string

    def __len__(self):
        """Return the number of Style objects in the Stylesheet."""
        return len(self._styles)

    def __iter__(self):
        """Return the list of :class:`Style` objects in the Stylesheet."""
        return iter(self.styles)

    def __contains__(self, item):
        """Return True if a style with the name ``item`` is present."""
        if isinstance(item, str):
            return item in self._styles
        elif isinstance(item, Style):
            return item.name in self._styles

        return False

    @property
    def based_on(self):
        """The name of the Stylesheet that this instance was created from."""
        return self._based_on

    @property
    def styles(self):
        """A list of :class:`Style` objects in the Stylesheet."""
        return self._styles.values()

    def add_style(self,
                  style,
                  overwrite = True):
        """Add :class:`Style` object to the stylesheet.

        :param style: The :class:`Style` that you are adding to the Stylesheet.
        :type style: :class:`Style`

        :param overwrite: If ``True``, will overwrite a :class:`Style` with
          the same name, if it already exists in the Stylesheet. If ``False``,
          will throw a ``ValueError``.
        :type overwrite: bool

        :raises TypeError: If ``style`` is not a :class:`Style`.

        :raises ValueError: If ``overwrite is False`` and a :class:`Style`
          with the same ``name`` is already exists within the Stylesheet.

        """
        if not isinstance(style, Style):
            raise TypeError('style is expected to be a Style object')

        if self.has_style(style.name) and overwrite is False:
            raise ValueError('Style named "{style.name}" already exists.')

        self._styles[style.name] = style
        self._style_names.append(style.name)

    def add_styles(self,
                   styles,
                   overwrite = True):
        """Add :class:`Style` objects to the stylesheet.

        :param styles: The iterable of :class:`Style` objects that you are
          adding to the Stylesheet.
        :type styles: list/tuple/set of :class:`Style` objects

        :param overwrite: If ``True``, will overwrite a :class:`Style` with
          the same name, if it already exists in the Stylesheet. If ``False``,
          will throw a ``ValueError``.
        :type overwrite: bool

        :raises ValueError: If ``overwrite is False`` and a :class:`Style`
          with the same ``name`` already exists within the Stylesheet.

        """
        for style in styles:
            self.add_style(style, overwrite = overwrite)

    def has_style(self,
                  style_name):
        """Check if the Stylesheet has a :class:`Style` with the given name.

        :param style_name: The name of the :class:`Style` to check for.
        :type style_name: string

        :returns: ``True`` / ``False``
        :rtype: bool

        """
        return style_name in self

    def get_style(self,
                  style_name,
                  fail_silently = True):
        """Return a :class:`Style` object with the name indicated.

        :param style_name: Name of the :class:`Style` to return.
        :type style_name: string

        :param fail_silently: If ``True``, will return ``None`` if no matching
          :class:`Style` is found. If ``False``, will throw a :ref:`LookupError`.
        :type fail_silently: bool

        :raises LookupError: If ``fail_silently is False`` and no matching
          :class:`Style` is present.

        :returns: The :class:`Style` requested, or ``None`` if ``fail_silently``.
        :rtype: :class:`Style` / ``None``

        """
        return_value = None
        for style in self._styles:
            if style.name == style_name:
                return_value = style
                break

        if return_value is None and fail_silently is False:
            raise LookupError('Style "{style_name}" not found in Stylesheet.')

        return return_value


class Style(object):
    """Defines the properties that affect how a unit of content is drawn in the PDF.

    :param name: The unique name that will be given to the Style.
    :type name: string

    :param from_style: An existing :class:`Style` whose properties will be
      copied to the new ``Style`` created.
    :type from_style: :class:`Style`

    :raises ValueError: If ``name`` is None.
    :raises TypeError: If ``name`` is not a string.

    """

    def __init__(self,
                 name,
                 from_style = None,
                 **kwargs):
        if name is None:
            raise ValueError('name expects a value, received None')
        if not isinstance(name, str):
            raise TypeError('name expects a string')

        #: Unqiue name given to the Style.
        self.name = name
        self._from_style = None
        self._properties = _get_default_style_properties()

        if from_style is not None:
            self = self.from_style(name, from_style)
            return

        for key in kwargs:
            normalized_key = key.upper()
            if normalized_key in _STYLE_PROPERTIES.keys():
                self._properties[normalized_key] = kwargs[key]

    def __repr__(self):
        """Return a string representation of the Style."""
        if self._from_style is not None:
            repr_string = 'Style({self.name}, from_style = "{self._from_style}")'
        else:
            repr_string = 'Style({self.name},\n'
            for key in self._properties:
                repr_string += '{key} = {self._properties[key]},\n'
            repr_string = repr_string[:-2]
            repr_string += ')'

        return repr_string

    def __str__(self):
        """Return an easily readable string representation of the object."""
        return 'Style: {self.name} ({self.id})'

    def __getattr__(self, name):
        """Return the :class:`Style` property indicated by Name."""
        normalized_name = name.upper()
        if normalized_name not in self._properties.keys():
            raise AttributeError('{name} not a valid Style attribute')


        return self._properties[normalized_name]

    @staticmethod
    def from_style(name,
                   from_style = None):
        """
        Return a :class:`Style` object with properties copied from the supplied template.

        :param name: The name to apply to the new :class:`Style` object.
        :type name: string

        :param from_style: An existing :class:`Style` whose properties will be
          copied to the new ``Style`` created.
        :type from_style: :class:`Style`

        :returns: A :class:`Style` object with properties copied from the
          supplied template.
        :rtype: :class:`Style`

        :raises ValueError: If either parameter is ``None``.
        :raises TypeError: If ``name`` is not a string, or ``from_style`` is not
          a :class:`Style`.

        """
        if name is None:
            raise ValueError("Style requires a name.")
        if from_style is None:
            raise ValueError('Style.from_style() expects a base style.')

        if not isinstance(name, str):
            raise TypeError('name expects a string')
        if not isinstance(from_style, Style):
            raise TypeError('from_style expects a Style object')

        new_style = Style(name)
        new_style.properties = from_style.properties

        return new_style

    @property
    def properties(self):
        """Return the :class:`Style` properties."""
        return self._properties

    @properties.setter
    def properties(self, value):
        """Set the Style's properties.

        :param value: The complete set of properties that should apply to the
          :class:`Style`.
        :type value: dict

        :raises TypeError: If ``value`` is not a ``dict``.
        :raises ValueError: If ``value`` has an invalid key.
        """
        if not isinstance(value, dict):
            raise TypeError('properties expected to be a dict')
        for key in value.keys():
            normalized_key = key.upper()
            if normalized_key not in _STYLE_PROPERTIES.keys():
                raise ValueError('Property {key} not recognized.')
            self._properties[normalized_key] = value[key]
