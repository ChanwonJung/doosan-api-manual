.. _struct_CONFIG_TOOL_SHAPE:

CONFIG_TOOL_SHAPE
=================

This is a structure information to set the tool shape, and consists of the following fields.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iValidity``
     - ``unsigned char[5]``
     - -
     - Validity flag for each safety object |br|  
       (0: Invalid, 1: Valid)  
   * - 5
     - ``_tShape``
     - :ref:`SAFETY_OBJECT[5] <struct_SAFETY_OBJECT>`
     - -
     - Safety Object (e.g., sphere, capsule, cube).

Total size: 515 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_TOOL_SHAPE
   {
       /* validity of safety object: 0(invalid), 1(valid) */
       unsigned char _iValidity[5];

       /* safety object (sphere, capsule, cube, etc.) */
       SAFETY_OBJECT _tShape[5];

   } CONFIG_TOOL_SHAPE, *LPCONFIG_TOOL_SHAPE;