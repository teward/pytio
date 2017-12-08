# coding=utf-8

from typing import Any, AnyStr, List


class TioResult:
    _pieces = []

    def __init__(self, pieces):
        # type: (List[AnyStr]) -> None
        self._pieces = pieces

        raise NotImplementedError

    @property
    def pieces(self):
        # type: () -> List
        return self._pieces

    def has(self, field):
        # type: (AnyStr) -> bool
        try:
            if field.lower() == "output":
                return len(self._pieces) > 0
            elif field.lower() == "debug":
                return len(self._pieces) > 1
            else:
                return False
        except IndexError:
            return False

    def get(self, field):
        # type: (AnyStr) -> Any
        if self.has('output') and field.lower() == "output":
            return self._pieces[0]
        elif self.has('debug') and field.lower() == "debug":
            return self._pieces[1]
