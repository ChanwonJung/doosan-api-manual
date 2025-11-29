.. _struct_CONFIG_CONFIGURABLE_IO:

CONFIG_CONFIGURABLE_IO
======================

This is a structure information to set IO input and consists of the following fields.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iIO``
     - ``unsigned char[TYPE_LAST][NUM_DIGITAL]``
     - -
     - Information of Safety I/O |br|
       The first dimension (2) indicates I/O type: 
       (0: Input, 1: Output) |br|
       The second dimension (16) corresponds to  
       each channel index (0-15).

Total size : 32 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_CONFIGURABLE_IO
   {
       /* Safety or user-defined I/O
          TYPE_LAST : number of I/O categories
          NUM_DIGITAL : number of digital channels per category
       */
       unsigned char _iIO[TYPE_LAST][NUM_DIGITAL];

   } CONFIG_CONFIGURABLE_IO, *LPCONFIG_CONFIGURABLE_IO;