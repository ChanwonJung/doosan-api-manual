.. _struct_CONFIG_TOOL_SHAPE_LIST:

CONFIG_TOOL_SHAPE_LIST
======================

This structure defines a **list of tool shape configurations**,  
each identified by a symbolic name and its associated safety geometry.  
It is used by the robot controller to manage multiple tool shape profiles for different tools or end-effectors.

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
     - Number of registered tool shapes in the list
   * - 4
     - ``_tTooList``
     - :ref:`CONFIG_TOOL_SHAPE_SYMBOL[50] <struct_CONFIG_TOOL_SHAPE_SYMBOL>`
     - -
     - Array of tool shape configurations (symbol + shape definition)

Total size: 27,354 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TOOL_SHAPE_LIST
   {
       /* Number of tool shape configurations */
       int _iToolCount;

       /* Tool shape symbol list (symbol + safety geometry) */
       CONFIG_TOOL_SHAPE_SYMBOL _tTooList[MAX_CONFIG_TOOL_SIZE];

   } CONFIG_TOOL_SHAPE_LIST, *LPCONFIG_TOOL_SHAPE_LIST;
