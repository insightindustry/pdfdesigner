# -*- coding: utf-8 -*-

"""
######################
pdfdesigner.templates
######################

This subpackage exposes classes that instantiate the templates to be applied to
multiple components within your PDF.

*********
Classes:
*********

  :class:`SectionTemplate` - Defines instructions for drawing
  :term:`Sections <Section>`.

  :class:`PageTemplate` - Defines instructions for drawing a :term:`Page`.

  :class:`StoryTemplate` - Defines instructions for drawing
  :term:`Stories <Story>`.

  :class:`ContainerTemplate` - Defines instructions for drawing a :term:`Container`.
"""

#from .section_template import SectionTemplate
#from .page_template import PageTemplate
#from .story_template import StoryTemplate
#from .design_target_template import ContainerTemplate

__all__ = [
    'SectionTemplate',
    'PageTemplate',
    'StoryTemplate',
    'ContainerTemplate'
]
