# coding=utf-8

import zlib
from typing import List, AnyStr, Union
from ._TioFile import TioFile
from ._TioVariable import TioVariable


class TioRequest:

    def __init__(self, lang=None, code=None):
        # type: (AnyStr, Union[AnyStr, bytes]) -> None
        self._files = []
        self._variables = []
        self._bytes = bytes()

        if lang:
            self.set_lang(lang)

        if code:
            self.add_file_bytes('.code.tio', code)

    def add_file(self, file):
        # type: (TioFile) -> None
        if file in self._files:
            self._files.remove(file)
        self._files.append(file)

    def add_file_bytes(self, name, content):
        # type: (AnyStr, bytes) -> None
        self._files.append(TioFile(name, content))

    def add_variable(self, variable: TioVariable):
        # type: (TioVariable) -> None
        self._variables.append(variable)

    def add_variable_string(self, name, value):
        # type: (AnyStr, Union[List[AnyStr], AnyStr]) -> None
        self._variables.append(TioVariable(name, value))

    def set_lang(self, lang):
        # type: (AnyStr) -> None
        self.add_variable_string('lang', lang)

    def set_code(self, code):
        # type: (AnyStr) -> None
        self.add_file_bytes('.code.tio', code)

    def set_input(self, input_data):
        # type: (AnyStr) -> None
        self.add_file_bytes('.input.tio', input_data.encode('utf-8'))

    def set_compiler_flags(self, flags):
        # type: (AnyStr) -> None
        self.add_variable_string('TIO_CFLAGS', flags)

    def set_commandline_flags(self, flags):
        # type: (AnyStr) -> None
        self.add_variable_string('TIO_OPTIONS', flags)

    def set_arguments(self, args):
        # type: (AnyStr) -> None
        self.add_variable_string('args', args)

    def write_variable(self, name, content):
        # type: (AnyStr, AnyStr) -> None
        if content:
            self._bytes += bytes("V" + name + '\x00' + str(len(content.split(' '))) + '\x00', 'utf-8')
            self._bytes += bytes(content + '\x00', 'utf-8')

    def write_file(self, name, contents):
        # type: (AnyStr, AnyStr) -> None
        if isinstance(contents, str):
            length = len(contents.encode('utf-8'))
        elif isinstance(contents, (bytes, bytearray)):
            length = len(contents)
        else:
            raise ValueError("Can only pass UTF-8 strings or bytes at this time.")
        self._bytes += bytes("F" + name + '\x00' + str(length) + '\x00', 'utf-8')
        self._bytes += bytes(contents + '\x00', 'utf-8')

    def as_bytes(self):
        # type: () -> bytes
        try:
            for var in self._variables:
                if hasattr(var, 'name') and hasattr(var, 'content'):
                    self.write_variable(var.name, var.content)

            for file in self._files:
                if hasattr(file, 'name') and hasattr(file, 'content'):
                    self.write_file(file.name, file.content)

            self._bytes += b'R'

        except IOError:
            raise RuntimeError("IOError generated during bytes conversion.")

        return self._bytes

    def as_deflated_bytes(self):
        # type: () -> bytes
        return zlib.compress(self.as_bytes(), 9)[2:-4]
