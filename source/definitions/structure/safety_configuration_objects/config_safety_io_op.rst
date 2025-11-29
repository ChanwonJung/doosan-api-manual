.. _struct_CONFIG_SAFETY_IO_OP:

CONFIG_SAFETY_IO_OP
===================

This is a structure information to configure the operation options for the safety I/O,  
including I/O port states, TBSFT input option, and additional I/O options.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iIO[TYPE_LAST][16]``
     - ``unsigned char[2][16]``
     - -
     - 2D array storing current safety I/O port states. |br| 
       "TYPE_LAST" represents input/output type, and each dimension supports up to 16 ports.
   * - 32
     - ``_iTBI_Op``
     - ``unsigned char``
     - -
     - TBSFT (Tool Box Safety Function Test) input option flag. |br|
       Used for enabling or configuring input-level testing.
   * - 33
     - ``_iReserved``
     - ``unsigned char``
     - -
     - Reserved field for future use.
   * - 34
     - ``_iIO_Op[TYPE_LAST][16]``
     - ``unsigned char[2][16]``
     - -
     - Safety I/O operation option array corresponding to each port. |br|
       Defines operational parameters or behavior for input/output channels.

Total size: 66 bytes 

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_SAFETY_IO_OP
   {
       /* Safety I/O */
       unsigned char _iIO[TYPE_LAST][16];
       /* TBSFT Input Option */
       unsigned char _iTBI_Op;
       /* Reserved */
       unsigned char _iReserved;
       /* Safety I/O Option */
       unsigned char _iIO_Op[TYPE_LAST][16];
   } CONFIG_SAFETY_IO_OP, *LPCONFIG_SAFETY_IO_OP;