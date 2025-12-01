.. _struct_IETHERNET_SLAVE_RESPONSE_DATA_EX:

IETHERNET_SLAVE_RESPONSE_DATA_EX
================================

This is a structure information to store **Industrial Ethernet (IE) slave response data** with extended information.  
It includes the GPR (General Purpose Register) data type, address, direction, and the corresponding response data buffer.

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
     - GPR data type |br|
       (0: bit, 1: int, 2: float)
   * - 1
     - ``_iGprAddr``
     - ``unsigned char``
     - -
     - GPR register address
   * - 2
     - ``_iInOut``
     - ``unsigned char``
     - 0 / 1
     - Data direction |br|
       (0: Input, 1: Output)
   * - 3
     - ``_szData``
     - ``char[128]``
     - -
     - Data buffer containing the slave's response value (string format)

Total size: 131 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _IETHERNET_SLAVE_RESPONSE_DATA_EX
   {
       unsigned char      _iGprType;
       unsigned char      _iGprAddr;
       unsigned char      _iInOut;
       char               _szData[128];

   } IETHERNET_SLAVE_RESPONSE_DATA_EX, *LPIETHERNET_SLAVE_RESPONSE_DATA_EX;
