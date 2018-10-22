## Python TIO.run Interaction Library

**NOTICE!  The GitHub repository is simply a mirror of the GitLab repository.  All development now takes place on GitLab.
Please do not open issues here on GitHub, they will get no attention at all and not be addressed.**

### Basic Information 

<table>
<tr><td align=center valign=center><a href="http://www.gnu.org/licenses/agpl-3.0" target="_blank"><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" title="AGPL 3.0" /></a></td></tr>
<tr><td align=center valign=center><a href="https://pypi.python.org/pypi/pytio" target="_blank"><img src="http://img.shields.io/pypi/v/pytio.svg" title="PyPI Version" /></a></td></tr>
</table>


### Continuous Integration Status

| CI Provider | Status                                                                                                                           |
|:-----------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| GitLab CI   | [![pipeline status](https://gitlab.com/teward/pytio/badges/master/pipeline.svg)](https://gitlab.com/teward/pytio/commits/master) |                                                 |


## Description

This module was written to be a Python library which can interact with [TryItOnline][1].

It was inspired by [the Java library to do the same, by SocraticPhoenix over on GitHub.][2]

## Compatibility

This module was written to be Python 2.7 and 3.0+ compatible.  It does not function with Python 2.6 or earlier.


## Installation / Usage

### Use PyPI

This library is available from the PyPI repository.

#### Python 2:

    pip install pytio
    
#### Python 3:

    pip3 install pytio

### Install from Source Code

#### Dependencies

First, install the dependencies from PyPI.

##### Python 2

For system-wide installation:

    pip install --upgrade -r requirements.txt
    
For user-space installation:

    pip install --user --upgrade -r requirements.txt
    
##### Python 3

For system-wide installation:

    pip3 install --upgrade -r requirements.txt

For user-space installation:

    pip3 install --user --upgrade -r requirements.txt

### Installing / Importing in Code

Simply copy the `pytio` package folder into your working directory for your Python script or program.


## FAQ

### Where can I report issues or make Feature Requests?

Issues and feature requests can be reported on the [GitLab project][3].

Be sure to put `[Feature Request]` in the beginning of the  title of your request, if it's a feature request. If you do  
not, your request may be treated as a bug report instead.

[1]: https://tio.run
[2]: https://github.com/SocraticPhoenix/TioJ
[3]: https://gitlab.com/teward/pytio