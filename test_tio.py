# coding=utf-8
import platform
import unittest
from pytio import Tio, TioRequest


class TestTIOResults(unittest.TestCase):
    tio = Tio()

    def test_valid_python2_request(self):
        request = TioRequest(lang='python2', code="print \"Hello, World!\"")
        response = self.tio.send(request)
        self.assertIsNone(response.error)
        if platform.python_version() >= '3.0':
            self.assertIsInstance(response.result, str)
        else:
            # noinspection PyUnresolvedReferences
            self.assertIsInstance(response.result, (unicode, str))
        self.assertEqual(response.result.strip('\n'), "Hello, World!")

    def test_invald_python2_request(self):
        request = TioRequest(lang='python2', code="I'm a teapot!")
        response = self.tio.send(request)
        self.assertIsNone(response.result)
        if platform.python_version() >= '3.0':
            self.assertIsInstance(response.error, str)
        else:
            # noinspection PyUnresolvedReferences
            self.assertIsInstance(response.error, (unicode, str))
        self.assertIn('EOL while scanning string literal', response.error)

    def test_valid_python3_request(self):
        request = TioRequest(lang='python3', code="print('Hello, World!')")
        response = self.tio.send(request)
        self.assertIsNone(response.error)
        if platform.python_version() >= '3.0':
            self.assertIsInstance(response.result, str)
        else:
            # noinspection PyUnresolvedReferences
            self.assertIsInstance(response.result, (unicode, str))
        self.assertEqual(response.result.strip('\n'), "Hello, World!")

    def test_invald_python3_request(self):
        request = TioRequest(lang='python3', code="I'm a teapot!")
        response = self.tio.send(request)
        self.assertIsNone(response.result)
        if platform.python_version() >= '3.0':
            self.assertIsInstance(response.error, str)
        else:
            # noinspection PyUnresolvedReferences
            self.assertIsInstance(response.error, (unicode, str))
        self.assertIn('EOL while scanning string literal', response.error)

    def test_valid_apl_request(self):
        request = TioRequest(lang='apl-dyalog', code="⎕←'Hello, World!'")
        response = self.tio.send(request)
        self.assertIsNone(response.error)
        if platform.python_version() >= '3.0':
            self.assertIsInstance(response.result, str)
        else:
            # noinspection PyUnresolvedReferences
            self.assertIsInstance(response.result, (unicode, str))
        self.assertEqual(response.result.strip('\n'), "Hello, World!")

    def test_invalid_apl_request(self):
        request = TioRequest(lang='apl-dyalog', code="I'm a teapot!")
        response = self.tio.send(request)
        self.assertIsNone(response.result)
        if platform.python_version() >= '3.0':
            self.assertIsInstance(response.error, str)
        else:
            # noinspection PyUnresolvedReferences
            self.assertIsInstance(response.error, (unicode, str))
        self.assertIn('error AC0109: unbalanced quotes detected', response.error)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
