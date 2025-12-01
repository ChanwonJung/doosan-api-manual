.. _struct_CONFIG_TCP_SYMBOL_EX:

CONFIG_TCP_SYMBOL_EX
====================

This structure defines an **extended Tool Center Point (TCP) symbol configuration**,  
which associates a TCP name with its detailed configuration including **orientation type**,  
**solution space**, and **multi-turn options**.  
It is an extended version of :ref:`CONFIG_TCP_SYMBOL <struct_CONFIG_TCP_SYMBOL>`.

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
     - TCP symbolic name (null-terminated string)
   * - 32
     - ``_tTCP``
     - :ref:`CONFIG_TCP_EX <struct_POSITION_EX>`
     - -
     - TCP configuration data containing position, orientation type, |br|
       solution space, and multi-turn flags

Total size: 105 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TCP_SYMBOL_EX
   {
       /* TCP symbolic name */
       char _szSymbol[MAX_SYMBOL_SIZE];

       /* TCP configuration with orientation, solution, and turn info */
       CONFIG_TCP_EX _tTCP;

   } CONFIG_TCP_SYMBOL_EX, *LPCONFIG_TCP_SYMBOL_EX;  // SUPPORT_ORIENTATION_TYPE
