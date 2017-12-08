# coding=utf-8

import zlib
from typing import List, AnyStr, Union
from ._TioFile import TioFile
from ._TioVariable import TioVariable


class TioRequest:

    def __init__(self, lang: AnyStr = None, code: Union[AnyStr, bytes] = None):
        self._files = []
        self._variables = []
        self._bytes = bytes()

        if lang:
            self.set_lang(lang)

        if code:
            self.add_file_bytes('.code.tio', code)

    def add_file(self, file: TioFile):
        if file in self._files:
            self._files.remove(file)
        self._files.append(file)

    def add_file_bytes(self, name: AnyStr, content: bytes):
        self._files.append(TioFile(name, content))

    def add_variable(self, variable: TioVariable):
        if (len(variable.content.split(' ')), variable) in self._variables:
            self._variables.remove(variable)
        self._variables.append(variable)

    def add_variable_string(self, name: AnyStr, value: Union[List[AnyStr], AnyStr]):
        self._variables.append(TioVariable(name, value))

    def set_lang(self, lang: AnyStr):
        self.add_variable_string('lang', lang)

    def set_code(self, code: AnyStr):
        self.add_file_bytes('.code.tio', code)

    def set_input(self, input_data: AnyStr):
        self.add_file_bytes('.input.tio', input_data.encode('utf-8'))

    def set_compiler_flags(self, flags: AnyStr):
        self.add_variable_string('TIO_CFLAGS', flags)

    def set_commandline_flags(self, flags: AnyStr):
        self.add_variable_string('TIO_OPTIONS', flags)

    def set_arguments(self, args: AnyStr):
        self.add_variable_string('args', args)

    def write_variable(self, name: AnyStr, content):
        if content:
            self._bytes += bytes("V" + name + '\x00' + str(len(content.split(' '))) + '\x00', 'utf-8')
            self._bytes += bytes(content + '\x00', 'utf-8')

    def write_file(self, name: AnyStr, contents: AnyStr):
        if isinstance(contents, str):
            length = len(contents.encode('utf-8'))
        elif isinstance(contents, (bytes, bytearray)):
            length = len(contents)
        else:
            raise ValueError("Can only pass UTF-8 strings or bytes at this time.")
        self._bytes += bytes("F" + name + '\x00' + str(length) + '\x00', 'utf-8')
        self._bytes += bytes(contents + '\x00', 'utf-8')

    def as_bytes(self):
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
        return zlib.compress(self.as_bytes(), 9)[2:-4]
