.. _struct_CONFIG_TCP_SYMBOL:

CONFIG_TCP_SYMBOL
=================

This structure defines the **TCP configuration symbol**, which maps a TCP (Tool Center Point) name  
to its detailed configuration parameters.

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
     - 32-byte identifier for the TCP name.
   * - 32
     - ``_tTCP``
     - :ref:`CONFIG_TCP <struct_CONFIG_TCP>`
     - -
     - TCP configuration object containing position and orientation offsets.

Total size: 56 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TCP_SYMBOL
   {
       /* tcp name */
       char _szSymbol[MAX_SYMBOL_SIZE];

       /* tcp data */
       CONFIG_TCP _tTCP;

   } CONFIG_TCP_SYMBOL, *LPCONFIG_TCP_SYMBOL;