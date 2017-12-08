# coding=utf-8
import gzip
import io
import json
import platform
from typing import AnyStr, Union

from ._TioRequest import TioRequest
from ._TioResponse import TioResponse

# Version specific import handling.
if platform.python_version() <= '3.0':
    import urllib
else:
    # noinspection PyCompatibility
    import urllib.request
    # noinspection PyCompatibility
    import urllib.parse
    # noinspection PyCompatibility
    import urllib.error


class Tio:
    backend = "cgi-bin/run/api/"
    json = "languages.json"

    def __init__(self, url="https://tio.run"):
        # type: (AnyStr) -> None
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
    def new_request(lang, code):
        # type: (AnyStr, Union[AnyStr, bytes]) -> TioRequest
        return TioRequest(lang=lang, code=code)

    def query_languages(self):
        # type: () -> set
        try:
            response = urllib.request.urlopen(self.json)
            rawdata = json.loads(response.read().decode('utf-8'))
            return set(rawdata.keys())
        except (urllib.error.HTTPError, urllib.error.URLError):
            return set()
        except Exception:
            return set()

    def send(self, fmt):
        # type: (TioRequest) -> TioResponse
        return self.send_bytes(fmt.as_deflated_bytes())

    def send_bytes(self, message):
        # type: (bytes) -> TioResponse
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
