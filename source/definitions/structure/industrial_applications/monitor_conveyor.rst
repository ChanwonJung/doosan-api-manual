.. _struct_MONITOR_CONVEYOR:

MONITOR_CONVEYOR
================

This structure defines the **monitoring state** of a conveyor system.  
It is used to check whether the conveyor is active or stopped during operation.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szName``
     - ``char[32]``
     - -
     - Conveyor name identifier
   * - 32
     - ``_bStart``
     - ``unsigned char``
     - 0 or 1
     - **Conveyor state flag** |br|
       0: Stopped |br|
       1: Running

Total size: 33 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITOR_CONVEYOR
   {
       /* Conveyor name */
       char _szName[MAX_SYMBOL_SIZE];
       /* Conveyor start flag (0: stop, 1: start) */
       unsigned char _bStart;

   } MONITOR_CONVEYOR, *LPMONITOR_CONVEYOR;