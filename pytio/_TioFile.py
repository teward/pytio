# coding=utf-8

from typing import AnyStr


class TioFile:
    _name = str()
    _content = bytes()

    def __init__(self, name: AnyStr, content: bytes):
        self._name = name
        self._content = content

    def get_name(self):
        return self.name

    def get_content(self):
        return self.content

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content
