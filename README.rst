Python TIO.run Interaction Library
----------------------------------

**NOTICE! The GitHub repository is simply a mirror of the GitLab
repository. All development now takes place on GitLab. Please do not
open issues here on GitHub, they will get no attention at all and not be
addressed.**

Basic Information
-----------------
.. raw:: html

    <table>
    <tr><td align=center valign=center><a href="http://www.gnu.org/licenses/agpl-3.0" target="_blank"><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" title="AGPL 3.0" /></a></td></tr>
    <tr><td align=center valign=center><a href="https://pypi.python.org/pypi/pytio" target="_blank"><img src="http://img.shields.io/pypi/v/pytio.svg" title="PyPI Version" /></a></td></tr>
    </table>

Continuous Integration Status
-----------------------------

.. raw:: html

    <table>
    <tr><th align=center valign=center>CI Provider</th><th align=center valign=center>Status</th></tr>
    <tr><td align=center valign=center>GitLab CI</td><td align=center valign=center><a href="https://gitlab.com/teward/pytio/commits/master"><img alt="pipeline status" src="https://gitlab.com/teward/pytio/badges/master/pipeline.svg" /></a></td>
    <tr><td align=center valign=center>AppVeyor</td><td align=center valign=center><a href="https://ci.appveyor.com/project/teward/pytio"><img alt="AppVeyor CI" src="https://ci.appveyor.com/api/projects/status/02ic4swejbae3drc?svg=true" /></a></td></tr>
    <tr><td align=center valign=center>CircleCI (via GitHub)</td><td align=center valign=center><a href="https://circleci.com/gh/teward/pytio"><img alt="CircleCI" src="https://circleci.com/gh/teward/pytio.svg?style=svg" /></a></td></tr>
    <tr><td align=center valign=center>TravisCI (via GitHub)</td><td align=center valign=center><a href="https://travis-ci.org/teward/pytio"><img alt="Travis CI" src="https://travis-ci.org/teward/pytio.svg?branch=master" /></a></td></tr>
    </table>

Description
-----------

This module was written to be a Python library which can interact with
`TryItOnline <https://tio.run>`__.

It was inspired by `the Java library to do the same, by SocraticPhoenix
over on GitHub. <https://github.com/SocraticPhoenix/TioJ>`__

Compatibility
-------------

This module was written to be Python 2.7 and 3.0+ compatible. It does
not function with Python 2.6 or earlier.

Installation / Usage
--------------------

Use PyPI
~~~~~~~~

This library is available from the PyPI repository.

Python 2:
^^^^^^^^^

::

    pip install pytio

Python 3:
^^^^^^^^^

::

    pip3 install pytio

Install from Source Code
~~~~~~~~~~~~~~~~~~~~~~~~

Dependencies
^^^^^^^^^^^^

First, install the dependencies from PyPI.

Python 2
''''''''

For system-wide installation:

::

    pip install --upgrade -r requirements.txt

For user-space installation:

::

    pip install --user --upgrade -r requirements.txt

Python 3
''''''''

For system-wide installation:

::

    pip3 install --upgrade -r requirements.txt

For user-space installation:

::

    pip3 install --user --upgrade -r requirements.txt

Installing / Importing in Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simply copy the ``pytio`` package folder into your working directory for
your Python script or program.

FAQ
---

Where can I report issues or make Feature Requests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Issues and feature requests can be reported on the `GitLab
project <https://gitlab.com/teward/pytio>`__.

| Be sure to put ``[Feature Request]`` in the beginning of the title of
  your request, if it's a feature request. If you do
| not, your request may be treated as a bug report instead.
