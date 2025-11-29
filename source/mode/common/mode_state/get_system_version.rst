.. _get_system_version:

get_system_version
------------------------------------------
This is a function for checking version information on each subsystem that constitutes the robot controller.
It returns details such as controller firmware, motion, and communication versions through the `SYSTEM_VERSION` structure.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 687)

.. code-block:: cpp

    bool get_system_version(LPSYSTEM_VERSION pVersion) { return _get_system_version(_rbtCtrl, pVersion); };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - *pVersion*
     - :ref:`SYSTEM_VERSION <struct_system_version>` *
     - -
     - Pointer to a structure that stores the version information of each subsystem.

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to retrieve version information.
   * - 1
     - int
     - Success — version information successfully obtained.

**Example**

.. code-block:: cpp

   SYSTEM_VERSION tSysVerion = { '\0', };
   DrFl.get_system_version(&tSysVerion);
   cout << "version: " << tSysVerion._szController << endl;

This example retrieves detailed version information of the robot controller  
and prints the controller’s version string to the console.