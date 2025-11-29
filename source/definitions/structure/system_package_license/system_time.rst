.. _struct_SYSTEM_TIME:

SYSTEM_TIME
============
This structure represents the system’s date and time information.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szDate``
     - ``char[8]``
     - -
     - Date (YYMMDD format)
   * - 8
     - ``_szTime``
     - ``char[8]``
     - -
     - Time (HHMMSS format)

Total size: 16 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_TIME
   {
       /* YYMMDD */
       char _szDate[8];
       /* HHMMSS */
       char _szTime[8];
   } SYSTEM_TIME, *LPSYSTEM_TIME;