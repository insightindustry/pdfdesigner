# -*- coding: utf-8 -*-

"""
pdfdesigner.design.layout
##########################

Defines classes used to represent layout elements in your PDF.

.. contents:: :local:

*********
Classes:
*********

    :class:`Section` - Defines a collection of `Pages <:class:Page>`.

    :class:`Story` - Defines a collection of content that spans multiple
    :term:`Containers <Container>`.

    :class:`Page` - Defines a single page that will be drawn within your PDF.

    :class:`Container` - Defines a :term:`Container` where content will
    be drawn within your PDF.

"""

#from .section import Section
#from .story import Story
#from .page import Page
#from .design_target import Container

__all__ = [
    'Section',
    'Story',
    'Page',
    'Container'
]
