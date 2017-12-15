# coding=utf-8

import collections

from ._Tio import Tio
from ._TioRequest import TioRequest
from ._TioResponse import TioResponse
from ._TioResult import TioResult

# Some of the items previously defined as individual classes can instead be defined as named tuples.
# So, use named tuples for those.
TioFile = collections.namedtuple('TioFile', ['name', 'content'])
TioVariable = collections.namedtuple('TioVariable', ['name', 'content'])

__title__ = 'PyTIO'
__author__ = 'Thomas Ward'
__version__ = '0.1.1'
__copyright__ = '2017 Thomas Ward'
__license__ = 'AGPLv3+'
__all__ = ('Tio', 'TioFile', 'TioRequest', 'TioResponse', 'TioResult', 'TioVariable')
