.. _struct_CONFIG_TCP_LIST:

CONFIG_TCP_LIST
================
This is a structure information to set multiple tcp names. It consists of the following fields as structure information.

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
     - Number of tool
   * - 4
     - ``_tTooList``
     - :ref:`CONFIG_TCP_SYMBOL[50] <struct_CONFIG_TCP_SYMBOL>`
     - -
     - TCP name object list (Maximum 50)

Total size: 2,804 bytes     

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TCP_LIST
   {
       /* Number of TCPs */
       int _iToolCount;

       /* List of TCP symbol objects (symbol + configuration) */
       CONFIG_TCP_SYMBOL _tTooList[MAX_CONFIG_TCP_SIZE];
   } CONFIG_TCP_LIST, *LPCONFIG_TCP_LIST;