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
    # noinspection PyCompatibility,PyUnresolvedReferences
    from urllib2 import urlopen
    # noinspection PyCompatibility,PyUnresolvedReferences
    from urllib2 import HTTPError, URLError
else:
    # noinspection PyCompatibility
    from urllib.request import urlopen
    # noinspection PyCompatibility
    from urllib.error import HTTPError, URLError


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
            response = urlopen(self.json)
            rawdata = json.loads(response.read().decode('utf-8'))
            return set(rawdata.keys())
        except (HTTPError, URLError):
            return set()
        except Exception:
            return set()

    def send(self, fmt):
        # type: (TioRequest) -> TioResponse
        return self.send_bytes(fmt.as_deflated_bytes())

    def send_bytes(self, message):
        # type: (bytes) -> TioResponse
        req = urlopen(self.backend, data=message)
        reqcode = req.getcode()
        if req.code == 200:
            if platform.python_version() >= '3.0':
                content_type = req.info().get_content_type()
            else:
                content_type = req.info()['content-type']

            if content_type == 'application/octet-stream':
                buf = io.BytesIO(req.read())
                gzip_f = gzip.GzipFile(fileobj=buf)
                fulldata = gzip_f.read()
            else:
                fulldata = req.read()

            return TioResponse(reqcode, fulldata, None)
        else:
            return TioResponse(reqcode, None, None)
