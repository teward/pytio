Python TIO.run Interaction Library
----------------------------------

Basic Information
~~~~~~~~~~~~~~~~~

.. raw:: html

   <table>

.. raw:: html

   <tr>

.. raw:: html

   <td align="center" valign="center">

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td align="center" valign="center">

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

Continuous Integration Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+---------------+
| CI Provider   | Status        |
+===============+===============+
| Travis CI     | |Travis-CI|   |
+---------------+---------------+
| CircleCI      | |CircleCI|    |
+---------------+---------------+
| AppVeyor      | |AppVeyor|    |
+---------------+---------------+

Description
-----------

This module was written to be a Python library which can interact with
`TryItOnline <https://tio.run>`__.

It was inspired by `the Java library to do the same, by SocraticPhoenix
over on GitHub. <https://github.com/SocraticPhoenix/TioJ>`__

Compatibility
-------------

This module was written to be Python 3 compatible. It does not function
with Python 2.

Installation / Usage
--------------------

Use PyPI
~~~~~~~~

This library is available from the PyPI repository.

Python 2:
^^^^^^^^^

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

Issues and feature requests can be reported on the `GitHub
project <https://tio.run>`__.

| Be sure to put ``[Feature Request]`` in the beginning of the title of
  your request, if it's a feature request. If you do
| not, your request may be treated as a bug report instead.

.. |Travis-CI| image:: https://travis-ci.org/teward/pytio.svg?branch=master
   :target: https://travis-ci.org/teward/pytio
.. |CircleCI| image:: https://circleci.com/gh/teward/pytio.svg?style=shield
   :target: https://circleci.com/gh/teward/pytio
.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/uvcfb3l6qwttwe72/branch/master?svg=true
   :target: https://ci.appveyor.com/project/teward/pytio/branch/master
