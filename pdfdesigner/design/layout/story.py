# -*- coding: utf-8 -*-

"""
pdfdesigner.design.layout.story
######################################

Implements the base class for defining :term:`Stories <Story>.`

"""
from collections import OrderedDict

import pdfdesigner
from pdfdesigner.utilities import is_iterable, increment_name
from pdfdesigner.design.layout import Container
from pdfdesigner.design.content import ContentElement


class Story(object):
    """Object representation of a :term:`Story`.

    A collection of :class:`Container` objects and associated
      :class:`ContentElement` objects which comprise a logical unit.

    The primary role of a :term:`Story` is to group a series of
      :class:`Containers <Container>` objects into a single whole.
      :term:`Flowable Content` that is assigned to the :term:`Story` will be
      drawn in the :class:`Story's <Story>` :class:`Containers <Container>` in
      order, regardless of the page on which a given :class:`Container` may be
      drawn.

    """

    def __init__(self,
                 name,
                 containers = None,
                 content = None,
                 show_jumplines = True):
        """Create a :class:`Story` object.

        :param name: The human-readable name given to the :class:`Story`.
        :type name: string

        :param show_jumplines: If ``True``, will display :term:`Jump Lines` for
          :class:`Containers <Container>` other than the last.
        :type show_jumplines: bool

        :param containers: The :class:`Container` objects where the story's
          :class:`ContentElements <ContentElement>` will be drawn.

          .. note::

            **Order matters!** The :class:`Container` objects will be processed
            in order, and if a given :class:`Container` has :class:`ContentElement`
            objects associated with it, those objects will be processed in order
            as well.

          .. caution::

            By adding a :class:`Container` to a :class:`Story`, you will de-associate
            any associated :class:`ContentElement` objects. This means that if
            you really want your third :class:`Paragraph` to appear in your second
            :class:`Container`, you should not include either in a :class:`Story`.

        :type containers: Order-sensitive iterable of :class:`Container` objects

        :param content: :class:`ContentElement` objects that are not already
          associated with any :class:`Container` object.
        :type content: Order-sensitive iterable of :class:`ContentElement` objects.

        """
        self.id = hash(name)
        self._name = name
        self.show_jumplines = show_jumplines

        self._containers = OrderedDict()
        self._container_ids = []
        self._page_container_mapping = {}
        self._container_page_mapping = {}

        self._contents = OrderedDict()
        self._content_ids = []

        if containers is not None:
            self.add_containers(containers)

        if content is not None:
            self.add_content_elements(content)

    def __repr__(self):
        """Return a string representation of the object."""
        return_string = '{}(name={}, '.format(self.__class__.__name__,
                                              self.name) + \
                        'containers={}, contents={}, '.format(self.containers,
                                                              self.contents) + \
                        'show_jumplines={})'.format(self.show_jumplines)

        return return_string

    def __contains__(self, item):
        """Return whether ``item`` is in the :class:`Story` object's containers
          or content.
        """
        if not isinstance(item, int) and \
           not isinstance(item, str) and \
           not isinstance(item, Container) and \
           not isinstance(item, ContentElement):
            return False

        if isinstance(item, str):
            item_id = hash(item)
        elif isinstance(item, int):
            item_id = item
        else:
            item_id = item.id

        return item_id in self._content_ids or item_id in self._container_ids

    @property
    def name(self):
        """Return the human-readable name of the :class:`Story`."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the value of the human-readable name of the :class:`Story`."""
        self._name = value
        self.id = hash(value)

    def add_containers(self, containers):
        """Add :class:`Container` objects contained in ``containers`` to the Story.

        :param containers: :class:`Containers <Container>` to add to the :class:`Story`
        :type containers: Iterable of :class:`Container` objects.

        """
        if not is_iterable(containers, min_length = 1) and \
           not isinstance(containers, Container):
            raise TypeError('containers must be a single Container object or iterable')

        if is_iterable(containers, min_length = 1):
            for item in containers:
                self.add_container(item)
        else:
            self.add_container(containers)

    def add_container(self, container):
        """Add a :class:`Container` object to the :class:`Story`.

        :param container: The :class:`Container` object to add to the Story.
        :type container: :class:`Container`
        """
        self._containers[container.id] = container
        self._container_ids.append(container.id)

        page_number = pdfdesigner.get_page_number(container.id)
        self._container_page_mapping[container.id] = page_number

        self.add_content_elements(container.contents)

    def get_container(self,
                      container_id,
                      fail_silently = True):
        """Return the :class:`Container` object provided in ``container_id``.

        :param container_id: Identifier or name of the :class:`Container`
          object to return.
        :type container_id: int / string

        :param fail_silently: If ``True``, will return ``None`` if not found.
          Otherwise, will raise ``LookupError``.
        :type fail_silently: bool

        :returns: :class:`Container`

        :raises LookupError: If ``fail_silently is False`` and :class:`Container`
          object is not found in the :class:`Story`.
        """
        if isinstance(container_id, str):
            container_id = hash(container_id)

        if container_id in self._container_ids:
            return self._containers[container_id]

        if fail_silently is False:
            raise LookupError('container_id ({}) not found in '
                              .format(container_id) +
                              'Story (name:{})'.format(self.name))

        return None

    def remove_container(self,
                         container,
                         remove_contents = True):
        """Remove the indicated :class:`Container` object from the :class:`Story`.

        :param container: The :class:`Container` to remove from the :class:`Story`.
        :type container: int / string / :class:`Container`.

        :returns: The removed :class:`Container` object, or ``None``.
        :rtype: :class:`Container` / ``None``

        :raises TypeError: If ``container`` is not a :class:`Container` object,
          integer, or string.
        """
        if isinstance(container, int) or isinstance(container, str):
            container = self.get_container(container)
        elif not isinstance(container, Container):
            raise TypeError('container must be a Container object, integer, or string.')

        if container.id in self._container_ids:
            if remove_contents:
                self.remove_content_elements(container,
                                             remove_duplicates = False)

            self._container_ids.remove(container.id)
            self._container_page_mapping.pop(container.id, None)
            return self._containers.pop(container.id, None)

        return None

    def add_content_elements(self,
                             content_elements,
                             overwrite = False,
                             duplicate = True):
        """Add :class:`ContentElement` objects to the :class:`Story`.

        :param content_elements: The :class:`ContentElement` objects to add to
          the :class:`Story`. Their order matters.
        :type content_elements: :class:`ContentElement`` object / Iterable  of
          :class:`ContentElement` objects.

        """
        if not isinstance(content_elements, ContentElement) and \
           not is_iterable(content_elements, min_length = 1):
            raise TypeError('content_elements must be a ContentElement or an ' +
                            'iterable of ContentElements')

        if is_iterable(content_elements):
            for item in content_elements:
                self.add_content_element(item,
                                         overwrite = overwrite,
                                         duplicate = duplicate)
        else:
            self.add_content_element(content_elements,
                                     overwrite = overwrite,
                                     duplicate = duplicate)

    def add_content_element(self,
                            content_element,
                            overwrite = False,
                            duplicate = True):
        """Add a :class:`ContentElement` to the :class:`Story`.

        .. note::

          Duplication is determined by :ref`ContentElement.id`. Content is not
          checked to determine duplication. Here's what this means in a practical
          example::

            first_paragraph(name = 'duplicating_paragraph', text = 'my original paragraph')
            second_paragraph(name = 'duplicating_paragraph', text = 'my second paragraph')
            
            story.add_content_element(first_paragraph)
            # Will now draw one paragraph that reads "my original paragraph"
            
            story.add_content_element(second_paragraph, overwrite=False, duplicate=True)
            # Will now produce two paragraphs that both read "my original paragraph"
            
            story.add_content_element(second_paragraph, overwrite=True, duplicate=False)
            # Will produce two paragraphs that all read "my second paragraph"
            
            story.add_content_element(second_paragraph, overwrite=False, duplicate=False)
            # Will raise a ValueError

        :param content_element: The :class:`ContentElement` to add.
        :type content_element: :class:`ContentElement`
        
        :param overwrite: Determines whether a previously added :class:`ContentElement` with the same ``id`` will be replaced by the instance being added.
        :type overwrite: bool
        
        :param duplicate: Determines whether to add a new instance of the :class:`ContentElement` if a previous one with the same ``id`` is already present.
        :type duplicate: bool
        """
        if not isinstance(content_element, ContentElement):
            raise TypeError('content_element must be a ContentElement')

        is_duplicating = content_element.id in self._content_ids

        if overwrite is True or not is_duplicating:
            self._contents[content_element.id] = content_element

        if not is_duplicating or (is_duplicating and duplicate is True):
            self._content_ids.append(content_element.id)
        elif is_duplicating and overwrite is False and duplicate is False:
            raise ValueError('content (id:{}) already exists, but both overwrite '
                             .format(content_element.id) +
                             'and duplicate are set to False')

    def get_content_element(self,
                            content_element_id,
                            fail_silently = True):
        """Return the :class:`ContentElement` object provided in ``content_element_id``.

        :param content_element_id: Identifier or name of the :class:`ContentElement`
          object to return.
        :type content_element_id: int / string

        :param fail_silently: If ``True``, will return ``None`` if not found.
          Otherwise, will raise ``LookupError``.
        :type fail_silently: bool

        :returns: :class:`ContentElement`

        :raises LookupError: If ``fail_silently is False`` and :class:`ContentElement`
          object is not found in the :class:`Story`.
        """
        if isinstance(content_element_id, str):
            content_element_id = hash(content_element_id)

        if content_element_id in self._content_ids:
            return self._contents[content_element_id]

        if fail_silently is False:
            raise LookupError('content_element_id ({}) not found in '
                              .format(content_element_id) +
                              'Story (name:{})'.format(self.name))

        return None

    def remove_content_elements(self,
                                content_elements,
                                remove_duplicates = True):
        """Remove content elements in ``content_elements`` from the :class:`Story`.

        :param content_elements: Iterable collection of :class:`ContentElement`
          objects.
        :type content_elements: iterable of :class:`ContentElement` objects

        :param remove_duplicates: If ``True``, will also remove other
          :class:`ContentElement` objets which are duplicates of those supplied.
        :type remove_duplicates: bool
        """
        for item in content_elements:
            self.remove_content_element(item,
                                        remove_duplicates = remove_duplicates)

    def remove_content_element(self,
                               content_element,
                               remove_duplicates = True):
        """Remove the ``content_element`` from the :class:`Story`.

        :param content_element: The :class:`ContentElement` to remove.
        :type content_elements: :class:`ContentElement`

        :param remove_duplicates: If ``True``, will also remove other
          :class:`ContentElement` objets which are duplicates of the one supplied.
        :type remove_duplicates: bool

        :returns: The :class:`ContentElement` object removed, or ``None`` if not found.
        :rtype: :class:`ContentElement` / ``None``

        """
        if isinstance(content_element, int) or isinstance(content_element, str):
            content_element = self.get_content_element(content_element)
        elif not isinstance(content_element, ContentElement):
            raise TypeError('content_element must be a ContentElement, int, or string.')

        is_duplicate = content_element.id in self._duplicate_id_original_mapping
        is_duplicated = content_element.id in self._duplicate_content_counts

        if remove_duplicates and is_duplicated:
            for index in range(0, self._duplicate_content_counts[content_element.id]):
                new_name = increment_name(content_element.name,
                                          index)
                new_id = hash(new_name)
                self.remove_content_element(new_id,
                                            remove_duplicates = False)

        if content_element.id in self._content_ids:
            if is_duplicate:
                original_id = self._duplicate_id_original_mapping[content_element.id]

                current_duplicate_count = self._duplicate_content_counts[original_id]
                if current_duplicate_count > 0:
                    self._duplicate_content_counts[original_id] = current_duplicate_count - 1
                else:
                    self._duplicate_content_counts.pop(original_id, None)

                self._duplicate_id_original_mapping.pop(content_element.id, None)

            self._content_ids.remove(content_element.id)
            return self._contents.pop(content_element.id, None)

        return None
