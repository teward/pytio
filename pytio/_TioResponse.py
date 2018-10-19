# coding=utf-8

from typing import Optional, Any, Union, AnyStr


class TioResponse:
    _code = 0
    _data = None
    _result = None
    _error = None
    _debug = None

    def __init__(self, code, data=None, error=None):
        # type: (Union[int, AnyStr], Optional[Any], Optional[Any]) -> None
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

        if self._splitdata[2] or self._splitdata[2] != b'':
            self._debug = self._splitdata[2]

    @property
    def code(self):
        # type: () -> Union[int, AnyStr]
        if isinstance(self._code, int) or isinstance(self._code, str):
            return self._code
        elif isinstance(self._code, bytes):
            return self._code.decode('utf-8')
        else:
            return self._code

    @property
    def result(self):
        # type: () -> Optional[AnyStr]
        if self._result:
            return self._result.decode('utf-8')
        else:
            return None

    @property
    def error(self):
        # type: () -> Optional[AnyStr]
        if self._error:
            return self._error.decode('utf-8')
        else:
            return None

    @property
    def debug(self):
        # type: () -> Optional[AnyStr]
        if self._debug:
            return self._debug

    @property
    def raw(self):
        # type: () -> Any
        return self._data

    def get_code(self):
        # type: () -> Union[int, AnyStr]
        return self.code

    def get_result(self):
        # type: () -> Optional[AnyStr]
        return self.result

    def get_error(self):
        # type: () -> Optional[AnyStr]
        return self.error

    def get_debug(self):
        # type: () -> Optional[AnyStr]
        return self.debug
