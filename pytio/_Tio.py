# coding=utf-8
import gzip
import io
import json
# noinspection PyCompatibility
import urllib.request
# noinspection PyCompatibility
import urllib.parse
# noinspection PyCompatibility
import urllib.error

from ._TioRequest import TioRequest
from ._TioResponse import TioResponse
from typing import Union


class Tio:
    backend = "cgi-bin/run/api/"
    json = "languages.json"

    def __init__(self, url="https://tio.run"):
        self.backend = url + '/' + self.backend
        self.json = url + '/' + self.json

    @staticmethod
    def read_in_chunks(stream_object, chunk_size=1024):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = stream_object.read(chunk_size)
            if not data:
                break
            yield data

    @staticmethod
    def new_request():
        return TioRequest

    def query_languages(self):
        try:
            response = urllib.request.urlopen(self.json)
            rawdata = json.loads(response.read().decode('utf-8'))
            return set(rawdata.keys())
        except (urllib.error.HTTPError, urllib.error.URLError):
            return set()
        except Exception:
            return set()

    def send(self, fmt: TioRequest):
        return self.send_bytes(fmt.as_deflated_bytes())

    def send_bytes(self, message: bytes):
        req = urllib.request.urlopen(self.backend, data=message)
        reqcode = req.getcode()
        if req.code == 200:
            if req.info().get_content_type() == 'application/octet-stream':
                buf = io.BytesIO(req.read())
                gzip_f = gzip.GzipFile(fileobj=buf)
                fulldata = gzip_f.read()
            else:
                fulldata = req.read()

            return TioResponse(reqcode, fulldata, None)
        else:
            return TioResponse(reqcode, None, None)

    def prepare(self, response: Union[bytes, bytearray]):
        raise NotImplementedError
