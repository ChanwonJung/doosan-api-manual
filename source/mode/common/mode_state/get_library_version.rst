.. _get_library_version:

get_library_version
------------------------------------------
This is a function for checking information on this API.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 688)

.. code-block:: cpp

    const char* get_library_version() { return _get_library_version(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - Character String (Maximum 32 byte)
     - Version information of the API (e.g., GL013300)

**Example**

.. code-block:: cpp

   const char* lpszLibVersion = drfl.get_library_version();
   cout << "LibVersion: " << lpszLibVersion << endl;

This example retrieves the current API library version  
and prints the version string to the console.