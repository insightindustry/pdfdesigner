# -*- coding: utf-8 -*-

"""
####################################
pdfdesigner.defaults.default_styles
####################################

Defines the default :class:`Styles <Style>` that are used by **PDFDesigner** and
the default :class:`Stylesheet`.

"""
from pdfdesigner.design.content import Stylesheet, Style

normal = Style('normal')

heading1 = Style('Heading1',
                 font_name = 'Helvetica-Bold',
                 font_size = 16,
                 leading = 16 * 1.2,
                 space_before = 6,
                 space_after = 18,
                 word_wrap = 'LTR',
                 allow_widows = False,
                 allow_orphans = False)
heading2 = Style('Heading2',
                 based_on = heading1,
                 font_size = 14,
                 leading = 14 * 1.2,
                 space_before = 6,
                 space_after = 16)
heading3 = Style('Heading3',
                 based_on = heading2,
                 font_name = 'Helvetica',
                 space_before = 3,
                 space_after = 12)
heading4 = Style('Heading4',
                 based_on = heading3,
                 font_name = 'Helvetica-Bold',
                 font_size = 12,
                 leading = 12 * 1.2,
                 space_before = 3,
                 space_after = 8)
heading5 = Style('Heading5',
                 based_on = heading4,
                 font_name = 'Helvetica-Italic')
heading6 = Style('Heading6',
                 based_on = heading5,
                 font_name = 'Helvetica-Bold',
                 font_size = 11,
                 leading = 11 * 1.2,
                 space_before = 3,
                 space_fater = 6)

title = Style('Title',
              font_name = 'Helvetica-Bold',
              font_size = 18,
              leading = 18 * 1.2,
              space_before = 18,
              space_after = 18,
              word_wrap = 'LTR',
              allow_widows = False,
              allow_orphans = False)
subtitle = Style('Subtitle',
                 based_on = 'Title',
                 font_name = 'Helvetica',
                 font_size = 14,
                 leading = 14 * 1.2,
                 space_before = 0,
                 space_after = 12)
footer = Style('Footer',
               based_on = normal,
               font_name = 'Helvetica',
               font_size = 9,
               leading = 9 * 1.2,
               space_before = 0,
               space_after = 0)
bulletlist = Style('BulletList',
                   based_on = normal,
                   bullet_font_name = 'Symbol',
                   bullet_font_size = 10,
                   bullet_indent = 18,
                   left_indent = 54)


DEFAULT_STYLESHEET = Stylesheet('default',
                                styles = [
                                    normal,
                                    bulletlist,
                                    title,
                                    subtitle,
                                    heading1,
                                    heading2,
                                    heading3,
                                    heading4,
                                    heading5,
                                    heading6,
                                    footer
                                ])
