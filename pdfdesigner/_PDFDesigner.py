# -*- coding: utf-8 -*-

"""
pdfdesigner._PDFDesigner.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module defines the _PDFDesigner class, which is the internal (hidden) class
that is responsible for interfacing with the ReportLab library and actually
generating the PDF.
"""

import reportlab
from reportlab import platypus
from reportlab.platypus import FrameBreak, PageBreak, Frame, PageTemplate
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.utils import ImageReader

from pdfdesigner.defaults import DEFAULT_SETTINGS, DEFAULT_STYLESHEET
from pdfdesigner.defaults.default_settings import PDFDesignerSettings
from pdfdesigner.design.content import Stylesheet, Style


class _PDFDesigner(object):
    """The internal _PDFDesigner object that generates the PDF.

    You never call this class or inherit it directly. It is used internally
    within the :mod:`pdfdesigner` namespace.
    """

    def __init__(self,
                 settings = None,
                 title = None,
                 author = None,
                 stylesheet = None,
                 default_style = 'normal'):
        """Create a :class:`_PDFDesigner` instance.

        :param settings: Configuration settings to apply to **PDFDesigner**.
        :type settings: :class:`PDFDesignerSettings`

        :param title: The title to apply to the PDF.
        :type title: string

        :param author: The author of the PDF.
        :type author: string

        :param stylesheet: The :class:`Stylesheet` to apply to the PDF.
        :type stylesheet: :class:`Stylesheet`

        :param default_style: The name of the :class:`Style` to use as the
          default for :class:`Paragraph` :term:`Content Elements <Content Element>`.
        :type default_style: string / :class:`Style`

        """
        if settings is not None and not isinstance(settings, PDFDesignerSettings):
            raise TypeError('settings expected to be a PDFDesignerSettings object')

        if title is not None and not isinstance(title, str):
            raise TypeError('title expected to be a string')

        if author is not None and not isinstance(author, str):
            raise TypeError('author expected to be a string')

        if stylesheet is not None and not isinstance(stylesheet, Stylesheet):
            raise TypeError('stylesheet expected to be a Stylesheet object')

        if default_style is not None:
            if not isinstance(default_style, str) and \
               not isinstance(default_style, Style):
                raise TypeError('default_style expected to be a string or Style object')

            if isinstance(default_style, str):
                default_style_name = default_style
            elif isinstance(default_style, Style):
                default_style_name = default_style.name

        if settings is None:
            settings = DEFAULT_SETTINGS

        if stylesheet is None:
            stylesheet = DEFAULT_STYLESHEET

        if default_style_name:
            if default_style_name not in stylesheet:
                raise ValueError('default_style ({default_style_name}) not found in' +
                                 ' Stylesheet')
        else:
            default_style_name = None

        #: A :class:`PDFDesignerSettings` instance that manages configuration.
        self.settings = settings

        #: The title that will be applied to the PDF.
        self.title = title

        #: The author that will be used in the PDF's properties.
        self.author = author

        #: If the PDF's content or configuration has changed, returns ``True``.
        self.is_outdated = False

        #: The :class:`Stylesheet` that contains :class:`Styles <Style>` that
        #: will apply to the PDF.
        self.stylesheet = stylesheet

        #: The name of the default style to apply to
        #: :term:`Content Elements <Content Element>`
        self.default_style_name = default_style_name

        self._binary_data = None

    @property
    def default_unit(self):
        """The default unit of measurement used for this PDF."""
        return self.settings.default_unit

    @property
    def binary_data(self):
        """The :ref:`io.bytesIO` object with the PDF's binary data.

        Returns ``None`` if the PDF is outdated.
        """
        if self.is_outdated:
            return None

        return self._binary_data

    def generate_pdf(self,
                     target_filename = None,
                     suppress_warnings = False,
                     log_filename = None,
                     print_grid = False,
                     print_crop_marks = False):
        """Generate the PDF.

        :param target_filename: If not ``None``, writes the PDF to the indicated
          file.
        :type target_filename: string

        :param supress_warnings: If ``True``, will hide :term:`Warnings <Warning>`.
        :type supress_warnings: bool

        :param log_filename: If not ``None``, writes a copy of the log to the
          file indicated.
        :type log_filename: string

        :param print_grid: If ``True``, will print the :term:`Page Grid` overlaid
          above the PDF content.
        :type print_grid: bool

        :param print_crop_marks: If ``True``, will print :term:`Crop Marks` at
          the margins of each page.

        :returns: Binary data of the generated PDF.
        :rtype: :ref:`io.BytesIO`

        :raises IOError: If cannot write to either ``target_filename`` or
          ``log_filename``.

        :raises TypeError: If parameters are not of expected types.
        """
        if target_filename is not None and not isinstance(target_filename, str):
            raise TypeError('target_filename expects a string')

        if log_filename is not None and not isinstance(log_filename, str):
            raise TypeError('log_filename expects a string')

        if suppress_warnings is not None and not isinstance(suppress_warnings, bool):
            raise TypeError('supress_warnings expects a bool')

        if print_grid is not None and not isinstance(print_grid, bool):
            raise TypeError('print_grid expects a bool')

        if print_crop_marks is not None and not isinstance(print_crop_marks, bool):
            raise TypeError('print_crop_marks expects a bool')

        raise NotImplementedError()

        self.is_outdated = False

    def generate_page_map(self,
                          target_filename = None,
                          suppress_warnings = False,
                          log_filename = None,
                          include_content = False,
                          include_labels = True,
                          print_grid = True,
                          print_crop_marks = True):
        """Generate the :term:`Page Map` of the PDF.

        :param target_filename: If not ``None``, writes the :term:`Page Map` to
          the indicated file.
        :type target_filename: string

        :param supress_warnings: If ``True``, will hide :term:`Warnings <Warning>`.
        :type supress_warnings: bool

        :param log_filename: If not ``None``, writes a copy of the log to the
          file indicated.
        :type log_filename: string

        :param include_content: If ``True``, will print the PDF's content with
          the :term:`Page Map` overlaid over it.
        :type include_content: bool

        :param include_labels: If ``True``, will print labels for
          :term:`Content Targets <Content Target>`.
        :type include_labels: bool

        :param print_grid: If ``True``, will print the :term:`Page Grid` overlaid
          above the PDF content.
        :type print_grid: bool

        :param print_crop_marks: If ``True``, will print :term:`Crop Marks` at
          the margins of each page.

        :returns: Binary data of the generated PDF.
        :rtype: :ref:`io.BytesIO`

        :raises IOError: If cannot write to either ``target_filename`` or
          ``log_filename``.

        :raises TypeError: If parameters are not of expected types.
        """
        if target_filename is not None and not isinstance(target_filename, str):
            raise TypeError('target_filename expects a string')

        if log_filename is not None and not isinstance(log_filename, str):
            raise TypeError('log_filename expects a string')

        if suppress_warnings is not None and not isinstance(suppress_warnings, bool):
            raise TypeError('supress_warnings expects a bool')

        if include_content is not None and not isinstance(include_content, bool):
            raise TypeError('include_content expects a bool')

        if include_labels is not None and not isinstance(include_labels, bool):
            raise TypeError('include_labels expects a bool')

        if print_grid is not None and not isinstance(print_grid, bool):
            raise TypeError('print_grid expects a bool')

        if print_crop_marks is not None and not isinstance(print_crop_marks, bool):
            raise TypeError('print_crop_marks expects a bool')

        raise NotImplementedError()

        self.is_outdated = False

    def apply_setting(self, name, value):
        """Apply the value to the named setting.

        :param name: The name of the setting to configure.
        :type name: string

        :param value: The value to apply to the setting.

        :raises ValueError: If the ``value`` is invalid for the setting.

        """
        self.settings.apply_setting(name, value)
        self.is_outdated = True



class Singleton(object):
    """A non-thread-safe helper class to ease implementing singletons.

    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    """

    def __init__(self, decorated):
        """Create the Singleton."""
        self._decorated = decorated

    def Instance(self):
        """Return the singleton instance.

        Upon its first call, it creates a new instance of the decorated class
          and calls its ``__init__`` method. On all subsequent calls, the already
          created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        """Raise a TypeError."""
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        """Return ``True`` if ``inst`` is a :class:`Singleton`."""
        return isinstance(inst, self._decorated)
