# -*- coding: utf-8 -*-

"""
pdfdesigner.design.content.stylesheet
######################################

Implements classes related to styling PDF content.

"""
from reportlab.lib import styles as platypus_styles
from pdfdesigner.defaults import DEFAULT_SETTINGS
from pdfdesigner.utilities import PropertyReference, is_numeric, is_string, \
    is_member, is_color, is_boolean, is_none, make_lowercase, make_identifier

_STYLE_PROPERTIES = {
    'font_name': PropertyReference(DEFAULT_SETTINGS.base_font_name,
                                   'fontName',
                                   is_string,
                                   None,
                                   None),
    'font_size': PropertyReference(10,
                                   'fontSize',
                                   is_numeric,
                                   None,
                                   None),
    'leading': PropertyReference(12,
                                 'leading',
                                 is_numeric,
                                 None,
                                 None),
    'left_indent': PropertyReference(0,
                                     'leftIndent',
                                     is_numeric,
                                     None,
                                     None),
    'right_indent': PropertyReference(0,
                                      'rightIndent',
                                      is_numeric,
                                      None,
                                      None),
    'first_line_indent': PropertyReference(0,
                                           'firstLineIndent',
                                           is_numeric,
                                           None,
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
                                   },
                                   None),
    'space_before': PropertyReference(0,
                                      'spaceBefore',
                                      is_numeric,
                                      None,
                                      None),
    'space_after': PropertyReference(0,
                                     'spaceAfter',
                                     is_numeric,
                                     None,
                                     None),
    'bullet_font_name': PropertyReference(DEFAULT_SETTINGS.base_font_name,
                                          'bulletFontName',
                                          is_string,
                                          None,
                                          None),
    'bullet_font_size': PropertyReference(10,
                                          'bulletFontSize',
                                          is_numeric,
                                          None,
                                          None),
    'bullet_indent': PropertyReference(0,
                                       'bulletIndent',
                                       is_numeric,
                                       None,
                                       None),
    'bullet_color': PropertyReference('BLACK',
                                      'bulletColor',
                                      is_color,
                                      {
                                          'allow_none': True
                                      },
                                      None),
    'bullet_offset_y': PropertyReference(0,
                                         'bulletOffsetY',
                                         is_numeric,
                                         None,
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
                                          },
                                          None),
    'bullet_dedent': PropertyReference('AUTO',
                                       'bulletDedent',
                                       is_member,
                                       {
                                           'iterable': [
                                               'AUTO'
                                           ],
                                           'allow_none': False
                                       },
                                       make_lowercase),
    'bullet_start': PropertyReference(None,
                                      'bulletStart',
                                      is_string,
                                      None,
                                      None),
    'bullet_format': PropertyReference(None,
                                       'bulletFormat',
                                       is_none,
                                       None,
                                       None),
    'text_color': PropertyReference('BLACK',
                                    'textColor',
                                    is_color,
                                    {
                                        'allow_none': True
                                    },
                                    None),
    'background_color': PropertyReference(None,
                                          'backColor',
                                          is_color,
                                          {
                                              'allow_none': True
                                          },
                                          None),
    'word_wrap': PropertyReference(None,
                                   'wordWrap',
                                   is_member,
                                   {
                                       'iterable': ['CJK',
                                                    'LTR',
                                                    'RTL'],
                                       'allow_none': True
                                   },
                                   None),
    'border_width': PropertyReference(0,
                                      'borderWidth',
                                      is_numeric,
                                      None,
                                      None),
    'border_padding': PropertyReference(0,
                                        'borderPadding',
                                        is_numeric,
                                        None,
                                        None),
    'border_color': PropertyReference(None,
                                      'borderColor',
                                      is_color,
                                      {
                                          'allow_none': True
                                      },
                                      None),
    'border_radius': PropertyReference(0,
                                       'borderRadius',
                                       is_numeric,
                                       None,
                                       None),
    'allow_widows': PropertyReference(True,
                                      'allowWidows',
                                      is_boolean,
                                      None,
                                      None),
    'allow_orphans': PropertyReference(False,
                                       'allowOrphans',
                                       is_boolean,
                                       None,
                                       None),
    'text_transformation': PropertyReference(None,
                                             'textTransform',
                                             is_member,
                                             {
                                                 'iterable': [
                                                     'UPPERCASE',
                                                     'LOWERCASE',
                                                 ],
                                                 'allow_none': True
                                             },
                                             make_lowercase),
    'split_long_words': PropertyReference(True,
                                          'splitLongWords',
                                          is_boolean,
                                          None,
                                          None),
    'underline_proportion': PropertyReference(DEFAULT_SETTINGS.underline_proportion,
                                              'underlineProportion',
                                              is_numeric,
                                              None,
                                              None),
    'bullet_anchor': PropertyReference('START',
                                       'bulletAnchor',
                                       is_member,
                                       {
                                           'iterable': ['START',
                                                        'MIDDLE',
                                                        'END'],
                                           'allow_none': False
                                       },
                                       make_lowercase),
    'justify_last_line': PropertyReference(False,
                                           'justifyLastLine',
                                           is_boolean,
                                           None,
                                           None),
    'justify_line_breaks': PropertyReference(False,
                                             'justifyBreaks',
                                             is_boolean,
                                             None,
                                             None),
    'space_shrinkage': PropertyReference(DEFAULT_SETTINGS.space_shrinkage,
                                         'spaceShrinkage',
                                         is_numeric,
                                         None,
                                         None),

    'rule_above_thickness': PropertyReference(0,
                                              None,
                                              is_numeric,
                                              None,
                                              None),
    'rule_above_color': PropertyReference(None,
                                          None,
                                          is_color,
                                          {
                                              'allow_none': True
                                          },
                                          None),
    'rule_above_padding': PropertyReference(12,
                                            None,
                                            is_numeric,
                                            None,
                                            None),

    'rule_below_thickness': PropertyReference(0,
                                              None,
                                              is_numeric,
                                              None,
                                              None),
    'rule_below_color': PropertyReference(None,
                                          None,
                                          is_color,
                                          {
                                              'allow_none': True
                                          },
                                          None),
    'rule_below_padding': PropertyReference(12,
                                            None,
                                            is_numeric,
                                            None,
                                            None),

}


def _get_default_style_properties():
    """Return a dictionary of style properties with default values set."""
    default_properties = {}
    for key in _STYLE_PROPERTIES:
        default_properties[key] = _STYLE_PROPERTIES[key].default

    return default_properties


def _validate_style_property(name, value):
    """Check whether the ``value`` supplied is valid for Style Property ``name``."""
    validation_function = _STYLE_PROPERTIES[name].validation
    validation_parameters = _STYLE_PROPERTIES[name].parameters

    if validation_parameters is not None:
        is_valid = validation_function(value, **validation_parameters)
    else:
        is_valid = validation_function(value)

    return is_valid


class Stylesheet(object):
    """Store a collection of :class:`Style` objects applied within a single PDF."""

    def __init__(self,
                 name = None,
                 styles = None,
                 based_on = None):
        """Create a Stylesheet.

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
        #: Name of the Stylesheet.
        self.name = name
        self._styles = {}
        self._based_on = None

        if based_on is not None:
            if not isinstance(based_on, Stylesheet):
                raise TypeError('Stylesheet constructor expects based_on to be ' +
                                'another Stylesheet.')
            self._based_on = based_on.name

            self.add_styles(based_on.styles)

        if styles is not None:
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
        """Return True if a :class:`Style` with the name ``item`` is present."""
        if isinstance(item, Style):
            return item.identifier_name in self._styles
        elif isinstance(item, str):
            normalized_item = make_identifier(item, lowercase = True)
            return normalized_item in self._styles

        return False

    def __getitem__(self, item):
        """Return the :class:`Style` indicated by `item`."""
        if not isinstance(item, str) and not isinstance(item, Style):
            raise TypeError('item must be a string or Style object')

        if isinstance(item, str):
            normalized_item = make_identifier(item, lowercase = True)
        elif isinstance(item, Style):
            normalized_item = item.identifier_name

        return self._styles[normalized_item]

    def __add__(self, other):
        """Add the :class:`Style` passed as ``other`` to the Stylesheet.

        :param other: A :class:`Style` object.
        :type other: :class:`Style`

        :raises TypeError: If ``other`` is not a :class:`Style` object.

        """
        if not isinstance(other, Style):
            raise TypeError('Only Style objects can be added to a Stylesheet.')

        self.add_style(other, overwrite = True)

    def __sub__(self, other):
        """Remove the :class:`Style` passed as ``other`` from the Stylesheet.

        :param other: The :class:`Style` to be removed.
        :type other: string / :class:`Style`

        :raises TypeError: If ``other`` is not a string or a :class:`Style`.

        """
        if isinstance(other, Style):
            self.remove_style(other.name)
        elif isinstance(other, str):
            self.remove_style(other)
        else:
            raise TypeError('Only Style objects or names of Styles can be removed ' +
                            'from a Stylesheet.')

    def __getattr__(self, name):
        """Return the :class:`Style` named ``name``.

        :param name: The name of the :class:`Style` to return.
        :type name: string

        :returns: The :class:`Style` named ``name``.
        """
        if not isinstance(name, str):
            raise TypeError('Style Name should be a string value.')

        normalized_name = make_identifier(name, lowercase = True)

        if normalized_name in self._styles:
            return self._styles[normalized_name]

        raise AttributeError('Unable to find Style ({name}) in Stylesheet.'
                             .format(name = name))

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
            raise ValueError('Style named "{style_name}" already exists.'
                             .format(style_name = style.name))

        self._styles[style.identifier_name] = style

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
        if not isinstance(style_name, str):
            raise TypeError('style_name must be a string')

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
        if not isinstance(style_name, str):
            raise TypeError('style_name must be a string')

        try:
            return_value = self[style_name]
        except AttributeError:
            return_value = None

        if return_value is None and fail_silently is False:
            raise LookupError('Style "{style_name}" not found in Stylesheet.'
                              .format(style_name = style_name))

        return return_value

    def remove_style(self, style_name):
        """Remove the :class:`Style` named ``style_name`` from the Stylesheet.

        :param style_name: The name of the :class:`Style` to remove.
        :type style_name: string

        :returns: The :class:`Style` object that was removed, or ``None`` if not present.
        :rtype: :class:`Style` / ``None``

        """
        if not isinstance(style_name, str):
            raise TypeError('style_name is expected to be a string')

        normalized_name = make_identifier(style_name, lowercase = True)

        return self._styles.pop(normalized_name, None)


class Style(object):
    """Defines the properties that affect how a unit of content is drawn in the PDF."""

    def __init__(self,
                 name,
                 from_style=None,
                 **kwargs):
        """Create a :class:`Style` object.

        :param name: The unique name that will be given to the Style.
        :type name: string

        :param from_style: An existing :class:`Style` whose properties will be
          copied to the new ``Style`` created.
        :type from_style: :class:`Style`

        :raises ValueError: If ``name`` is None.
        :raises TypeError: If ``name`` is not a string.

        """
        if name is None:
            raise ValueError('name expects a value, received None')
        if not isinstance(name, str):
            raise TypeError('name expects a string')

        #: Unqiue name given to the Style.
        self.name = name
        self._from_style = None
        self._properties = _get_default_style_properties()

        if from_style is not None:
            self._from_style = from_style.name
            self.properties = from_style.properties

        for key in kwargs:
            normalized_key = key.lower()
            if normalized_key in _STYLE_PROPERTIES:
                self._properties[normalized_key] = kwargs[key]

    def __repr__(self):
        """Return a string representation of the Style."""
        if self._from_style is not None:
            repr_string = 'Style({self.name}, from_style = "{self._from_style}")'
        else:
            repr_string = 'Style({self.name},\n'
            for key in self._properties:
                repr_string += '{} = {},\n'.format(key, self._properties[key])
            repr_string = repr_string[:-2]
            repr_string += ')'

        return repr_string

    def __str__(self):
        """Return an easily readable string representation of the object."""
        return 'Style: {self.name} ({self.id})'

    def __getitem__(self, item):
        """Return the :term:`Style Property` indicated by `item`.

        :param item: The :term:`Style Property` to return.
        :type item: string

        :returns: Value of the :term:`Style Property`.
        """
        if not isinstance(item, str):
            raise TypeError('item must be a string')

        return self._properties[item]

    def __getattr__(self, name):
        """Return the :class:`Style` property indicated by Name."""
        normalized_name = name.lower()
        if normalized_name not in _STYLE_PROPERTIES.keys():
            raise AttributeError('{name} not a valid Style attribute')

        return self._properties[normalized_name]

    def __setattr__(self, name, value):
        """Set the value of the :term:`Style Property` indicated."""
        if not isinstance(name, str):
            raise TypeError('name is expected to be a string')

        normalized_name = name.lower()
        if normalized_name in _STYLE_PROPERTIES:
            is_valid = _validate_style_property(normalized_name, value)
            if not is_valid:
                raise ValueError('value ({value}) is invalid for Style Property {name}')

            self._properties[normalized_name] = value
        else:
            super(self.__class__, self).__setattr__(name, value)

    @property
    def identifier_name(self):
        """Return an identifier-compatible version of the object's ``name``."""
        return make_identifier(self.name, lowercase = True)

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
            normalized_key = key.lower()
            if normalized_key not in _STYLE_PROPERTIES.keys():
                raise ValueError('Property {key} not recognized.')
            self._properties[normalized_key] = value[key]

    def to_platypus(self):
        """Return the ``Style`` as a ReportLab ``ParagraphStyle`` object.

        :rtype: ``reportlab.lib.styles.ParagraphStyle``
        """
        reportlab_properties = {}
        for key in self._properties:
            reportlab_key = _STYLE_PROPERTIES[key].reportlab_key
            if reportlab_key is None:
                continue

            conversion = _STYLE_PROPERTIES[key].conversion
            if conversion is not None:
                reportlab_properties[reportlab_key] = conversion(self._properties[key])
            else:
                reportlab_properties[reportlab_key] = self._properties[key]

        reportlab_style = platypus_styles.ParagraphStyle(self.name,
                                                         parent=None,
                                                         **reportlab_properties)

        return reportlab_style

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
        new_style._from_style = from_style.name
        new_style.properties = from_style.properties

        return new_style
