.. _struct_MONITORING_DATA:

MONITORING_DATA
===============

This structure aggregates overall robot monitoring information, combining  
**control-related data** (state, joint, task, torque) and  
**miscellaneous I/O data** (clock, I/O, brake, button, current, temperature).  
It serves as the **top-level monitoring packet** received from the robot controller.

.. list-table::
   :widths: 10 28 15 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tCtrl``
     - :ref:`MONITORING_CONTROL <struct_MONITORING_CONTROL>`
     - -
     - Control-related monitoring data (state, joint, task, torque)
   * - 423
     - ``_tMisc``
     - :ref:`MONITORING_MISC <struct_MONITORING_MISC>`
     - -
     - Miscellaneous data (clock, I/O, brake, buttons, current, temperature)

Total size: 517 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_DATA
   {
       MONITORING_CONTROL          _tCtrl;
       /* misc. */
       MONITORING_MISC             _tMisc;

   } MONITORING_DATA, *LPMONITORING_DATA;

.. note::
   - ``_tCtrl`` corresponds to :ref:`MONITORING_CONTROL <struct_MONITORING_CONTROL>`,  
     which includes robot state, joint, task, and torque information.  
   - ``_tMisc`` corresponds to :ref:`MONITORING_MISC <struct_MONITORING_MISC>`,  
     containing controller I/O and thermal data.  
   - Together, they form the **complete robot monitoring packet** periodically updated by the controller.
