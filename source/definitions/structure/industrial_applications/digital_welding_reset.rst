.. _struct_DIGITAL_WELDING_RESET:

DIGITAL_WELDING_RESET
=====================

This structure defines the **digital welding reset command** used to clear  
errors, alarms, or process states in a digital welding system.  
It contains a single flag to trigger reset operations.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bReset``
     - ``unsigned char``
     - 0 or 1
     - **Reset trigger flag** |br|
       0: No action |br|
       1: Execute reset

Total size: 1 byte

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _DIGITAL_WELDING_RESET
   {
       unsigned char _bReset;   // 0: No reset, 1: Reset
   } DIGITAL_WELDING_RESET, *LPDIGITAL_WELDING_RESET;

.. note::
   - Used to **reset welding control states** or recover from faults.  
   - Commonly called before reinitializing or restarting a digital welding process.