.. _struct_SERIAL_SEARCH:

SERIAL_SEARCH
=============

This structure is used to store the **search results of available serial devices**.  
Each detected device is represented by a :ref:`SERIAL_PORT_NAME <struct_SERIAL_PORT_NAME>` structure.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_nCount``
     - ``int``
     - -
     - Number of detected serial devices
   * - 4
     - ``_tSerial[10]``
     - :ref:`SERIAL_PORT_NAME <struct_SERIAL_PORT_NAME>` [10]
     - -
     - Array of serial device information structures

Total size: 1,444 bytes  

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SERIAL_SEARCH
   {
       /* Number of detected serial devices */
       int              _nCount;
       /* Serial port and name information for each device */
       SERIAL_PORT_NAME _tSerial[10];

   } SERIAL_SEARCH, *LPSERIAL_SEARCH;
