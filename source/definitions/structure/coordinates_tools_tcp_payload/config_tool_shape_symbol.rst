.. _struct_CONFIG_TOOL_SHAPE_SYMBOL:

CONFIG_TOOL_SHAPE_SYMBOL
========================

This structure defines a **named tool shape configuration**,  
combining a symbolic tool identifier with its associated :ref:`CONFIG_TOOL_SHAPE <struct_CONFIG_TOOL_SHAPE>` data.  
It is typically used for managing multiple tool shape profiles in the controller’s configuration database.

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
     - Tool shape symbolic name (null-terminated if shorter)
   * - 32
     - ``_tToolShape``
     - :ref:`CONFIG_TOOL_SHAPE <struct_CONFIG_TOOL_SHAPE>`
     - -
     - Tool safety shape configuration (5 safety objects)

Total size: 547 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TOOL_SHAPE_SYMBOL
   {
       /* Tool shape symbolic name */
       char _szSymbol[MAX_SYMBOL_SIZE];

       /* Tool safety shape configuration (contains up to 5 safety objects) */
       CONFIG_TOOL_SHAPE _tToolShape;

   } CONFIG_TOOL_SHAPE_SYMBOL, *LPCONFIG_TOOL_SHAPE_SYMBOL;
