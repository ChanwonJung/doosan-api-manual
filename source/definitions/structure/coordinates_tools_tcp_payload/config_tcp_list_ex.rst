.. _struct_CONFIG_TCP_LIST_EX:

CONFIG_TCP_LIST_EX
==================

This structure defines a **list of extended Tool Center Point (TCP) configurations**,  
each containing detailed TCP information including **orientation type**, **solution space**,  
and **multi-turn options**.  
It is an extended version of :ref:`CONFIG_TCP_LIST <struct_CONFIG_TCP_LIST>`.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTcpCount``
     - ``int``
     - -
     - Number of TCP entries in the list
   * - 4
     - ``_tTcpList``
     - :ref:`CONFIG_TCP_SYMBOL_EX[50] <struct_CONFIG_TCP_SYMBOL_EX>`
     - -
     - Array of extended TCP configuration symbols (maximum 50)

Total size: 5,254 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TCP_LIST_EX
   {
       /* Number of TCPs */
       int _iTcpCount;

       /* Extended TCP list with orientation and solution info */
       CONFIG_TCP_SYMBOL_EX _tTcpList[MAX_CONFIG_TCP_SIZE];

   } CONFIG_TCP_LIST_EX, *LPCONFIG_TCP_LIST_EX;  // SUPPORT_ORIENTATION_TYPE
