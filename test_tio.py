#!/usr/bin/python3
# coding=utf-8
import unittest
from pytio import Tio, TioRequest


class TestTIOResults(unittest.TestCase):
    tio = Tio()

    def test_valid_python3_request(self):
        request = TioRequest(lang='python3', code="print('Hello, World!')")
        response = self.tio.send(request)
        self.assertIsNone(response.error)
        self.assertIsInstance(response.result, str)
        self.assertEqual(response.result.strip('\n'), "Hello, World!")

    def test_invald_python3_request(self):
        request = TioRequest(lang='python3', code="I'm a teapot!")
        response = self.tio.send(request)
        self.assertIsNone(response.result)
        self.assertIsInstance(response.error, str)
        self.assertIn('EOL while scanning string literal', response.error)

    def test_valid_apl_request(self):
        request = TioRequest(lang='apl-dyalog', code="⎕←'Hello, World!'")
        response = self.tio.send(request)
        self.assertIsNone(response.error)
        self.assertIsInstance(response.result, str)
        self.assertEqual(response.result.strip('\n'), "Hello, World!")

    def test_invalid_apl_request(self):
        request = TioRequest(lang='apl-dyalog', code="I'm a teapot!")
        response = self.tio.send(request)
        self.assertIsNone(response.result)
        self.assertIsInstance(response.error, str)
        self.assertIn('error AC0607: unbalanced quotes detected', response.error)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
