.. _struct_MONITORING_COCKPIT:

MONITORING_COCKPIT
==================

This structure provides monitoring information for **cockpit (external)** digital button states.  
It reports the on/off status of each cockpit button connected to the robot controller.

.. list-table::
   :widths: 10 28 15 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualBS``
     - ``unsigned char[6]``
     - -
     - Cockpit digital button states |br| 0: Off, 1: On

Total size: 6 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_COCKPIT
   {
       /* digital button state */
       unsigned char _iActualBS[NUM_BUTTON_EX];
   } MONITORING_COCKPIT, *LPMONITORING_COCKPIT;

.. note::
   - ``NUM_BUTTON_EX`` represents the number of cockpit buttons physically available (default: 6).  
   - Each element in ``_iActualBS`` corresponds to one cockpit button.  
   - Value **0** means "not pressed", **1** means "pressed".  
   - Typically used for **external cockpit hardware**, such as Smart TP grip buttons or optional control modules.
