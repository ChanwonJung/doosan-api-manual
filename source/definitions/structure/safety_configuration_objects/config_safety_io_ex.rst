.. _struct_CONFIG_SAFETY_IO_EX:

CONFIG_SAFETY_IO_EX
===================

This is a structure information to set the safety I/O (extended version),  
and consists of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iIO[TYPE_LAST][NUM_SAFETY * 2]``
     - ``unsigned char[2][16]``
     - -
     - Each subarray represents input/output and safety channel index
   * - 32
     - ``_bLevel[TYPE_LAST][NUM_SAFETY]``
     - ``unsigned char[2][8]``
     - -
     - Optional trigger-level configuration (commented out in header) |br|
       Reserved for future firmware or hardware revisions

Total size: 48 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_SAFETY_IO_EX
   {
       /* Safety I/O */
       unsigned char _iIO[TYPE_LAST][NUM_SAFETY * 2];
       ///* trigger level */
       //unsigned char _bLevel[TYPE_LAST][NUM_SAFETY];
   } CONFIG_SAFETY_IO_EX, *LPCONFIG_SAFETY_IO_EX;