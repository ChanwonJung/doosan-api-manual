.. _struct_CONFIG_IO_FUNC:

CONFIG_IO_FUNC
===============

This structure defines the configuration for a single **I/O function port**,  
including its assigned port number and active signal level.  
It is primarily used in remote control or configurable I/O settings  
to map logical functions to specific digital I/O channels.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iPort``
     - ``char``
     - -1 ~ 15
     - Digital port number assigned to this I/O function |br|
       (-1: Not used, 0-15: Active port index)
   * - 1
     - ``_bLevel``
     - ``char``
     - 0 or 1
     - Active signal level for the port |br|
       (0: Low active, 1: High active)

Total size: 2 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_IO_FUNC
   {
       /* Port number (-1: unused, 0–15: valid port index) */
       char _iPort;

       /* Signal level (0: low, 1: high) */
       char _bLevel;

   } CONFIG_IO_FUNC, *LPCONFIG_IO_FUNC;

.. note::
   - This structure is a **fundamental component** of higher-level I/O configurations  
     such as :ref:`CONFIG_REMOTE_CONTROL <struct_CONFIG_REMOTE_CONTROL>`.  
   - Use ``_iPort = -1`` to deactivate a function or leave it unassigned.  
   - The ``_bLevel`` field defines the **trigger logic** for detecting or outputting signals.
