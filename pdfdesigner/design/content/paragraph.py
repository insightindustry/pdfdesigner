# -*- coding: utf-8 -*-

"""
pdfdesigner.design.content.paragraph
######################################

Implements the class for defining a Paragraph.

"""
from reportlab import platypus

import pdfdesigner
from pdfdesigner.design.content import Style, ContentElement
from pdfdesigner.utilities import is_boolean


class Paragraph(ContentElement):
    """:term:`Content Element` that contains text only."""

    def __init__(self,
                 text,
                 style = None,
                 bullet = None,
                 list_position = None,
                 encoding = 'utf8',
                 case_sensitive_markup = False,
                 alignment = None):
        """Create a Paragraph object.

        :param text: The textual content of the paragraph. XML-like markup including the tags:
          ``<b> ... </b>`` - bold
          ``<i> ... </i>`` - italics
          ``<u> ... </u>`` - underline
          ``<strike> ... </strike>`` - strike through
          ``<super> ... </super>`` - superscript
          ``<sub> ... </sub>`` - subscript
          ``<font name=fontfamily/fontname color=colorname size=float>``
          ``<span name=fontfamily/fontname color=colorname backcolor=colorname size=float style=stylename>``
          ``<onDraw name=callable label="a label"/>``
          ``<index [name="callablecanvasattribute"] label="a label"/>``
          ``<link>link text</link>`` with attributes:
              ``size``/``fontSize``=number
              ``name``/``face``/``fontName`` = name
              ``fg``/``textColor``/``color`` = color
              ``backcolor``/``backColor``/``bgcolor`` = color
              ``dest``/``destination``/``target``/``href``/``link`` = target
          ``<a>anchor text</a>`` with attributes:
              ``fontSize``= number
              ``fontName``= name
              ``fg``/``textColor``/``color`` = color
              ``backcolor``/``backColor``/``bgcolor`` = color
              ``href`` = href
          ``<a name="anchorpoint"/>``
          ``<unichar name="unicode character name"/>``
          ``<unichar value="unicode code point"/>``

          The whole may be surrounded by <para> </para> tags

          The <b> and <i> tags will work for the built-in fonts (Helvetica /Times
          / Courier).  For other fonts you need to register a family of fonts
          using :ref:`pdfdesigner.register_font_family`.

          It will also be able to handle any MathML specified Greek characters.
        :type text: string

        :param style: The name of the :class:`Style` to apply to the paragraph,
          or the actual :class:`Style` object to apply. By default, will apply
          the PDF's configured ``default_style``.
        :type style: string / :class:`Style`

        :param bullet: The content to display as the bullet if the paragraph is
          a bulleted paragraph. Overrides the paragraph's default style.
        :type bullet: string

        :param encoding: Indication of encoding to apply to the Paragraph.
        :type encoding: string

        :param case_sensitive_markup: If ``True``, XML-like markup tags are
          expected to be case-sensitive. If ``False``, their case does not matter.
        :type case_sensitive_markup: bool

        :param alignment: Indicates how the Paragraph should be aligned. Overrides
          the :class:`Style` object's configured alignment.
        :type alignment: string, member of: ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY')
        """
        super(self.__class__, self).__init__(style)

        self.text = text
        self._list_position = list_position

        self._case_sensitive_markup = case_sensitive_markup

        if bullet is None:
            self._bullet_text = self.style.get_bullet_text(list_position)
        else:
            if not isinstance(bullet, str):
                raise TypeError('bullet must be a string or None')

            self._bullet_text = bullet

        if alignment is not None:
            self.style.alignment = alignment

        self.encoding = encoding

    def __repr__(self):
        """Return a string representation of the :class:`Paragraph` object."""
        return_tuple = ('Paragraph("{}", style = {}, '
                        .format(self.text, self.style),
                        'bullet = "{}", list_position = {}, '
                        .format(self._bullet_text, self._list_position),
                        'encoding = "{}", '
                        .format(self.encoding),
                        'case_sensitive_markup = {}, '
                        .format(self._case_sensitive_markup),
                        'alignment = "{}")'.format(self.alignment))

        return ''.join(return_tuple)

    @property
    def alignment(self):
        """Return the Paragraph's alignment."""
        return self.style.alignment

    @alignment.setter
    def alignment(self, value):
        """Set the Paragraph's alignment."""
        self.style.alignment = value

    @property
    def case_sensitive_markup(self):
        """Return whether in-line markup should be treated as case-sensitive."""
        return self._case_sensitive_markup

    @case_sensitive_markup.setter
    def case_sensitive_markup(self, value):
        """Set the value of ref:`case_sensitive_markup`."""
        if not is_boolean(value):
            raise TypeError('case_sensitive_markup must be a boolean value')

        self._case_sensitive_markup = value

    def to_platypus(self):
        """Return a ReportLab ``platypus.Paragraph`` version of the object."""
        return platypus.Paragrah(self.text,
                                 self.style.to_platypus(),
                                 bulletText = self._bullet_text,
                                 frags = None,
                                 caseSensitive = self._case_sensitive_markup,
                                 encoding = self.encoding)
