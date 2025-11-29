.. _struct_IETHERNET_SLAVE_DATA_EX:

IETHERNET_SLAVE_DATA_EX
=======================

This is a structure information to define **extended Industrial Ethernet (IE) slave data attributes**.  
It specifies the GPR (General Purpose Register) data type, address, and the direction of data flow (input/output).

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iGprType``
     - ``unsigned char``
     - 0 / 1 / 2
     - **GPR data type** |br|
       0: bit, 1: int, 2: float
   * - 1
     - ``_iGprAddr``
     - ``unsigned char``
     - -
     - GPR register address
   * - 2
     - ``_iInOut``
     - ``unsigned char``
     - 0 / 1
     - **Data direction** |br|
       0: Input, 1: Output

Total size: 3 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _IETHERNET_SLAVE_DATA_EX
   {
       unsigned char      _iGprType;
       unsigned char      _iGprAddr;
       unsigned char      _iInOut;

   } IETHERNET_SLAVE_DATA_EX, *LPIETHERNET_SLAVE_DATA_EX;
