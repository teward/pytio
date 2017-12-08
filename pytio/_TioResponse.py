# coding=utf-8

from typing import Optional, Any


class TioResponse:
    _code = 0
    _data = None
    _result = None
    _error = None

    def __init__(self, code, data: Optional[Any] = None, error: Optional[Any] = None):
        self._code = code
        self._data = data
        if data is None:
            self._splitdata = [None, error]
        else:
            self._splitdata = self._data.split(self._data[:16])

        if not self._splitdata[1] or self._splitdata[1] == b'':
            self._error = b''.join(self._splitdata[2:])
            self._result = None
        else:
            self._error = None
            self._result = self._splitdata[1]

    @property
    def code(self):
        return self._code.decode('utf-8')

    @property
    def result(self):
        if self._result:
            return self._result.decode('utf-8')
        else:
            return None

    @property
    def error(self):
        if self._error:
            return self._error.decode('utf-8')
        else:
            return None

    @property
    def raw(self):
        return self._data

    def get_code(self):
        return self.code

    def get_result(self):
        return self.result

    def get_error(self):
        return self.error
