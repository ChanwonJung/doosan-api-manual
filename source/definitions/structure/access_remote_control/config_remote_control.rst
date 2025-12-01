.. _struct_CONFIG_REMOTE_CONTROL:

CONFIG_REMOTE_CONTROL
=====================

This structure defines the **remote control configuration**  
for assigning digital input functions to external control devices.  
It allows mapping of up to **8 remote control functions** for both input and output types.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bEnable``
     - ``unsigned char``
     - 0 or 1
     - Enable flag for remote control |br|
       (0: Disabled, 1: Enabled)
   * - 1
     - ``_tFunc[TYPE_LAST][NUM_REMOTE_CONTROL]``
     - :ref:`CONFIG_IO_FUNC <struct_CONFIG_IO_FUNC>` [2][8]
     - -
     - I/O function mapping table for remote control signals |br|
       "TYPE_LAST = 2": Input/Output |br|
       "NUM_REMOTE_CONTROL = 8": Up to 8 functions per type

Total size: 33 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_REMOTE_CONTROL
   {
       /* Enable remote control (0: disable, 1: enable) */
       unsigned char _bEnable;

       /* Function mapping table
          TYPE_LAST = 2 → (Input / Output)
          NUM_REMOTE_CONTROL = 8 → functions per type
       */
       CONFIG_IO_FUNC _tFunc[2][8];

   } CONFIG_REMOTE_CONTROL, *LPCONFIG_REMOTE_CONTROL;

.. note::
   - Each remote control function can be mapped to any available digital port (0–15).  
   - Unused ports are marked with ``-1``.  
   - Used for external start/stop, mode switching, or digital input-based robot control.  
   - Extended from the :ref:`CONFIG_IO_FUNC <struct_CONFIG_IO_FUNC>` base structure  
     to support structured input/output mapping.