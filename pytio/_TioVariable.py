# coding=utf-8

from typing import AnyStr, List


class TioVariable:
    _name = str()
    _content = []

    def __init__(self, name: AnyStr, content: List[AnyStr]):
        self._name = name
        self._content = content

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content

    def get_name(self):
        return self.name

    def get_content(self):
        return self.content
