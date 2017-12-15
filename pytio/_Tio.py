# coding=utf-8
import gzip
import io
import json
import platform
from typing import AnyStr

from ._TioRequest import TioRequest
from ._TioResponse import TioResponse

# Version specific import handling.
if platform.python_version() <= '3.0':
    # Python 2: The specific URLLib sections are in urllib2.

    # noinspection PyCompatibility,PyUnresolvedReferences
    from urllib2 import urlopen
    # noinspection PyCompatibility,PyUnresolvedReferences
    from urllib2 import HTTPError, URLError
else:
    # Python 3: The specific URLLib sections are in urllib submodules.

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
    def new_request(*args, **kwargs):
        # type: () -> None
        raise DeprecationWarning("The Tio.new_request() method is to be removed in a later release; please call "
                                 "TioRequest and its constructor directly..")

    def query_languages(self):
        # type: () -> set
        # Used to get a set containing all supported languages on TIO.run.
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
        # Command alias to use send_bytes; this is more or less a TioJ cutover.
        return self.send_bytes(fmt.as_deflated_bytes())

    def send_bytes(self, message):
        # type: (bytes) -> TioResponse
        req = urlopen(self.backend, data=message)
        reqcode = req.getcode()
        if req.code == 200:
            if platform.python_version() >= '3.0':
                content_type = req.info().get_content_type()
            else:
                # URLLib requests/responses in Python 2 don't have info().get_content_type(),
                # so let's get it the old fashioned way.
                content_type = req.info()['content-type']

            # Specially handle GZipped responses from the server, and unzip them.
            if content_type == 'application/octet-stream':
                buf = io.BytesIO(req.read())
                gzip_f = gzip.GzipFile(fileobj=buf)
                fulldata = gzip_f.read()
            else:
                # However, if it's not compressed, just read it directly.
                fulldata = req.read()

            # Return a TioResponse object, containing the returned data from TIO.
            return TioResponse(reqcode, fulldata, None)
        else:
            # If the HTTP request failed, we need to give a TioResponse object with no data.
            return TioResponse(reqcode, None, None)
