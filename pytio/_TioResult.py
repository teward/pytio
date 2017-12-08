# coding=utf-8

from typing import AnyStr, List


class TioResult:
    _pieces = []

    def __init__(self, pieces: List[AnyStr]):
        self._pieces = pieces

        raise NotImplementedError

    @property
    def pieces(self):
        return self._pieces

    def has(self, field: AnyStr):
        try:
            if field.lower() == "output":
                return len(self._pieces) > 0
            elif field.lower()  == "debug":
                return len(self._pieces) > 1
            else:
                return False
        except IndexError:
            return False

    def get(self, field):
        if self.has('output') and field.lower() == "output":
            return self._pieces[0]
        elif self.has('debug') and field.lower() == "debug":
            return self._pieces[1]
