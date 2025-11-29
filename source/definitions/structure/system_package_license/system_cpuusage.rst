.. _struct_SYSTEM_CPUUSAGE:

SYSTEM_CPUUSAGE
================
This structure represents CPU usage statistics for the entire system and a specific process.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTotalUsage``
     - ``float``
     - -
     - Total CPU usage percentage
   * - 4
     - ``_iProcessUsage``
     - ``float``
     - -
     - CPU usage percentage of the monitored process

Total size: 8 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_CPUUSAGE
   {
       /* total cpu usage */
       float _iTotalUsage;
       /* specific process usage */
       float _iProcessUsage;
   } SYSTEM_CPUUSAGE, *LPSYSTEM_CPUUSAGE;