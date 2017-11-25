# -*- coding: utf-8 -*-

"""
pdfdesigner.defaults.default_settings
######################################

Defines the ``DEFAULT_SETTINGS`` constant which is used to configure **PDFDesigner**.

"""

from pdfdesigner.utilities import PropertyReference, is_boolean, is_string, \
    is_numeric, is_member, is_tuple, is_color, lowercase

from pdfdesigner.design.layout.page_sizes import LETTER
from pdfdesigner.design import units

from reportlab.rl_settings import T1SearchPath as reportlab_T1SearchPath
from reportlab.rl_settings import TTFSearchPath as reportlab_TTFSearchPath
from reportlab.rl_settings import CMapSearchPath as reportlab_CMapSearchPath

_SETTINGS_DEFINITIONS = {
    'allow_table_bounds_errors': PropertyReference(True,
                                                   "allowTableBoundsErrors",
                                                   is_boolean,
                                                   None,
                                                   None),
    'check_shapes': PropertyReference(True,
                                      "shapeChecking",
                                      is_boolean,
                                      None,
                                      None),
    'default_encoding': PropertyReference('WinAnsiEncoding',
                                          "defaultEncoding",
                                          is_member,
                                          {
                                              "iterable": [
                                                  'WinAnsiEncoding',
                                                  'MacRomanEncoding'
                                              ]
                                          },
                                          None),
    'default_graphics_font_name': PropertyReference('Times-Roman',
                                                    "defaultGraphicsFontName",
                                                    is_string,
                                                    None,
                                                    None),
    'compress_pages': PropertyReference(True,
                                        "pageCompression",
                                        is_boolean,
                                        None,
                                        None),
    'use_A85': PropertyReference(True,
                                 "useA85",
                                 is_boolean,
                                 None,
                                 None),
    'default_page_size': PropertyReference(LETTER,
                                           "defaultPageSize",
                                           is_tuple,
                                           {
                                               'length': 2,
                                               'expected_type': (
                                                   {
                                                       'function': is_numeric,
                                                       'parameters': None
                                                   },
                                                   {
                                                       'function': is_numeric,
                                                       'parameters': None
                                                   })
                                           },
                                           None),
    'default_image_caching': PropertyReference(False,
                                               "defaultImageCaching",
                                               is_boolean,
                                               None,
                                               None),
    'zlib_warnings': PropertyReference(True,
                                       "ZLIB_WARNINGS",
                                       is_boolean,
                                       None,
                                       None),
    'warn_on_missing_font_glyphs': PropertyReference(False,
                                                     "warnOnMissingFontGlyphs",
                                                     is_boolean,
                                                     None,
                                                     None),
    'verbosity': PropertyReference(0,
                                   "verbose",
                                   is_numeric,
                                   None,
                                   None),
    'show_boundary': PropertyReference(False,
                                       "showBoundary",
                                       is_boolean,
                                       None,
                                       None),
    'on_empty_table': PropertyReference('ERROR',
                                        'emptyTableAction',
                                        is_member,
                                        {
                                            'iterable': [
                                                'ERROR',
                                                'INDICATE',
                                                'IGNORE'
                                            ],
                                            'allow_none': False
                                        },
                                        lowercase),
    'invariant': PropertyReference(False,
                                   'invariant',
                                   is_boolean,
                                   None,
                                   None),
    'eps_preview_transparent': PropertyReference(None,
                                                 'eps_preview_transparent',
                                                 is_color,
                                                 {
                                                     'allow_none': True
                                                 },
                                                 None),
    'eps_preview': PropertyReference(True,
                                     'eps_preview',
                                     is_boolean,
                                     None,
                                     None),
    'eps_ttf_embed': PropertyReference(True,
                                       'eps_ttf_embed',
                                       is_boolean,
                                       None,
                                       None),
    'eps_ttf_embed_uid': PropertyReference(False,
                                           'eps_ttf_embed_uid',
                                           is_boolean,
                                           None,
                                           None),
    'overlap_attached_space': PropertyReference(True,
                                                'overlapAttachedSpace',
                                                is_boolean,
                                                None,
                                                None),
    'optimize_long_tables': PropertyReference(True,
                                              'longTableOptimize',
                                              is_boolean,
                                              None,
                                              None),
    'auto_convert_encoding': PropertyReference(False,
                                               'autoConvertEncoding',
                                               is_boolean,
                                               None,
                                               None),
    'layout_fuzz': PropertyReference(1e-6,
                                     '_FUZZ',
                                     is_numeric,
                                     None,
                                     None),
    'wrap_A85': PropertyReference(False,
                                  'wrapA85',
                                  is_boolean,
                                  None,
                                  None),
    'fs_encodings': PropertyReference(('utf8',
                                       'cp1252',
                                       'cp430'),
                                      'fsEncodings',
                                      is_tuple,
                                      {
                                          'length': None,
                                          'expected_type': None
                                      },
                                      None),
    'odbc_driver': PropertyReference('odbc',
                                     'odbc_driver',
                                     is_string,
                                     None,
                                     None),
    'underline_links': PropertyReference(False,
                                         'platypus_link_underline',
                                         is_boolean,
                                         None,
                                         None),
    'base_font_name': PropertyReference('Helvetica',
                                        'canvas_basefontname',
                                        is_string,
                                        None,
                                        None),
    'allow_short_table_rows': PropertyReference(True,
                                                'allowShortTableRows',
                                                is_boolean,
                                                None,
                                                None),
    'image_reader_flags': PropertyReference(0,
                                            'imageReaderFlags',
                                            is_numeric,
                                            None,
                                            None),
    'offset_paragraph_font_size_height': PropertyReference(True,
                                                           'paraFontSizeHeightOffset',
                                                           is_boolean,
                                                           None,
                                                           None),
    'background_base_color': PropertyReference(None,
                                               'canvas_baseColor',
                                               is_color,
                                               {
                                                   'allow_none': True
                                               },
                                               None),
    'ignore_container_actions': PropertyReference(True,
                                                  'ignoreContainerActions',
                                                  is_boolean,
                                                  None,
                                                  None),
    'ttf_ascii_readable': PropertyReference(True,
                                            'ttfAsciiReadable',
                                            is_boolean,
                                            None,
                                            None),
    'multiline_pdf': PropertyReference(False,
                                       'pdfMultiLine',
                                       is_boolean,
                                       None,
                                       None),
    'pdf_comments': PropertyReference(False,
                                      'pdfComments',
                                      is_boolean,
                                      None,
                                      None),
    'debug_mode': PropertyReference(False,
                                    'debug',
                                    is_boolean,
                                    None,
                                    None),
    'rtl_support': PropertyReference(False,
                                     'rtlSupport',
                                     is_boolean,
                                     None,
                                     None),
    'wrap_on_fake_width': PropertyReference(True,
                                            'listWrapOnFakeWidth',
                                            is_boolean,
                                            None,
                                            None),
    'underline_proportion': PropertyReference(0.0,
                                              'baseUnderlineProportion',
                                              is_numeric,
                                              None,
                                              None),
    'decimal_symbol': PropertyReference('.',
                                        'decimalSymbol',
                                        is_string,
                                        None,
                                        None),
    'error_on_duplicate_page_label_page_number': PropertyReference(False,
                                                                   'errorOnDuplicatePageLabelPage',
                                                                   is_boolean,
                                                                   None,
                                                                   None),
    'auto_generate_missing_ttf_name': PropertyReference(False,
                                                        'autoGenerateMissingTTFName',
                                                        is_boolean,
                                                        None,
                                                        None),
    'space_shrinkage': PropertyReference(0.05,
                                         'spaceShrinkage',
                                         is_numeric,
                                         None,
                                         None),
    'T1SearchPath': PropertyReference(reportlab_T1SearchPath,
                                      'T1SearchPath',
                                      is_tuple,
                                      {
                                          'length': None,
                                          'expected_type': None
                                      },
                                      None),
    'TTFSearchPath': PropertyReference(reportlab_TTFSearchPath,
                                       'TTFSearchPath',
                                       is_tuple,
                                       {
                                           'length': None,
                                           'expected_type': None
                                       },
                                       None),
    'CMapSearchPath': PropertyReference(reportlab_CMapSearchPath,
                                        'CMapSearchPath',
                                        is_tuple,
                                        {
                                            'length': None,
                                            'expected_type': None
                                        },
                                        None),

    'default_unit': PropertyReference(units.POINT,
                                      None,
                                      is_numeric,
                                      None,
                                      None)
}


def _get_default_settings():
    """Return a ``dict`` of the **PDFDesigner** default settings."""
    default_settings = {}

    for key in _SETTINGS_DEFINITIONS:
        default_settings[key] = _SETTINGS_DEFINITIONS[key].default

    return default_settings


class PDFDesignerSettings(object):
    """Collection of configuration settings for the **PDFDesigner**."""

    def __init__(self,
                 **kwargs):
        """Create a :class:`PDFDesignerSettings` object."""
        self._settings = _get_default_settings()

        for key in kwargs:
            if key in _SETTINGS_DEFINITIONS:
                self.__setattr__(key, kwargs[key])

    def __repr__(self):
        """Return a string representation of the object."""
        return 'PDFDesignerSettings()'

    def __contains__(self, item):
        """Return whether the item is contained within the settings."""
        return item in self._settings

    def __iter__(self):
        """Return an iterator of the settings."""
        return iter(self._settings)

    def __len__(self):
        """Return the number of settings configured."""
        return len(self._settings)

    def __getattr__(self, name):
        """Return the configuration setting identified by name."""
        if name in self._settings:
            return self._settings[name]

        raise AttributeError('{name} is not a recognized configuration setting')

    def __setattr__(self, name, value):
        """Set the configuration setting to the value supplied."""
        if name in _SETTINGS_DEFINITIONS:
            validation_function = _SETTINGS_DEFINITIONS[name].validation
            validation_parameters = _SETTINGS_DEFINITIONS[name].parameters

            if validation_parameters is None:
                is_valid = validation_function(value)
            else:
                is_valid = validation_function(value, **validation_parameters)

            if not is_valid:
                raise ValueError('value ({value}) is not valid for setting {name}')

            self._settings[name] = value
        else:
            super(self.__class__, self).__setattr__(name, value)

    def apply_setting(self, name, value):
        """Apply the value to the named setting.

        :param name: The name of the setting to configure.
        :type name: string

        :param value: The value to apply to the setting.

        :raises ValueError: If the ``value`` is invalid for the setting.

        """
        if name is not None and not isinstance(name, str):
            raise TypeError('name expects a string')

        normalized_name = name.lower()
        if normalized_name not in _SETTINGS_DEFINITIONS:
            raise ValueError('Seting ({name}) not a valid configuration setting.')

        self.__setattr__(normalized_name, value)

    def get_reportlab_setting(self, name):
        """Convert a PDFDesigner Setting to its ReportLab key and value.

        :param name: The name of a PDFDesigner Setting.
        :type name: str

        :returns: A tuple of form ``(key, value)`` where ``key`` is the ReportLab
          setting name, and ``value`` is the ReportLab-compatible value.
        :rtype: tuple

        """
        if not isinstance(name, str):
            raise TypeError('name expects a string')
        if name not in _SETTINGS_DEFINITIONS:
            raise ValueError('name ({name}) is not a valid PDFDesigner Setting')

        definition = _SETTINGS_DEFINITIONS[name]
        reportlab_key = definition.reportlab_key
        conversion_function = definition.conversion
        default_value = definition.default

        if name not in self:
            value = default_value
        else:
            value = self._settings[name]

        if conversion_function is not None:
            reportlab_value = conversion_function(value)
        else:
            reportlab_value = value

        return reportlab_key, reportlab_value

    def to_reportlab(self):
        """Return a ``dict`` that is compatible with ReportLab's ``rl_config``."""
        rl_settings = {}
        for key in _SETTINGS_DEFINITIONS:
            reportlab_key, reportlab_value = self.get_reportlab_setting(key)

            rl_settings[reportlab_key] = reportlab_value

        return rl_settings


#: Set of default **PDFDesigner** Configuration Settings.
DEFAULT_SETTINGS = PDFDesignerSettings()
