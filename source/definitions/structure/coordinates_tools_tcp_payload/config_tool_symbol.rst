.. _struct_CONFIG_TOOL_SYMBOL:

CONFIG_TOOL_SYMBOL
==================

This structure defines a **tool configuration symbol**,  
which links a symbolic name to its corresponding physical tool configuration.  
Each symbol entry contains both the **tool name** and its **detailed parameters** defined in  
:ref:`CONFIG_TOOL <struct_CONFIG_TOOL>`.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szSymbol``
     - ``char[32]``
     - -
     - Tool symbol name (e.g., "Gripper", "Welder")
   * - 32
     - ``_tTool``
     - :ref:`CONFIG_TOOL <struct_CONFIG_TOOL>`
     - -
     - Tool configuration data (mass, center of mass, inertia)

Total size: 72 bytes  

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TOOL_SYMBOL
   {
       /* Tool symbol name */
       char _szSymbol[32];

       /* Tool configuration data */
       CONFIG_TOOL _tTool;

   } CONFIG_TOOL_SYMBOL, *LPCONFIG_TOOL_SYMBOL;
