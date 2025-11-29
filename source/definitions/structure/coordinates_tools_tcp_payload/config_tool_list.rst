.. _struct_CONFIG_TOOL_LIST:

CONFIG_TOOL_LIST
================

This structure defines a list containing multiple **tool configuration symbols**.  
Each element represents an individual tool entry defined by  
:ref:`CONFIG_TOOL_SYMBOL <struct_CONFIG_TOOL_SYMBOL>` and includes its corresponding configuration data.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iToolCount``
     - ``int``
     - -
     - Number of tools registered in the list
   * - 4
     - ``_tTooList``
     - :ref:`CONFIG_TOOL_SYMBOL <struct_CONFIG_TOOL_SYMBOL>` ``[50]``
     - -
     - Array of tool configuration symbols (maximum 50 entries)

Total size: 3604 bytes  

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TOOL_LIST
   {
       /* Number of registered tools */
       int _iToolCount;

       /* Array of tool configuration symbols (up to 50) */
       CONFIG_TOOL_SYMBOL _tTooList[50];

   } CONFIG_TOOL_LIST, *LPCONFIG_TOOL_LIST;
