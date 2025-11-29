.. _troubleshooting_poco_not_found:

7.3 Build Error: Poco Not Found
====================================

A. Error Case
-------------

During build, you may encounter:

.. code-block:: bash

   fatal error: Poco/SharedPtr.h: No such file or directory

B. Root Cause Analysis
----------------------

The **Poco C++ Libraries** are missing from your system or not properly linked in CMake.

C. Solution
-----------

Install the dependency manually:

.. code-block:: bash

   sudo apt install libpoco-dev

Then re-run CMake:

.. code-block:: bash

   cd build && cmake .. && make
