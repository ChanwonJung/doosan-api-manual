.. _struct_READ_IETHERNET_SLAVE_DATA:
.. _struct_MONITORING_IETHERNET_SLAVE:

READ_IETHERNET_SLAVE_DATA
=========================

This is a structure information to store **Industrial Ethernet (IE) slave data**.  
It defines the data type, address, and value used for **GPR (General Purpose Register)** monitoring or reading from a connected slave device.

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
     - ``_szData``
     - ``char[128]``
     - -
     - Data buffer containing the GPR value (string format)

Total size: 130 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _READ_IETHERNET_SLAVE_DATA
   {
       /* IE GPR data type 0 : bit, 1 : int, 2 : float */
       unsigned char      _iGprType;
       /* IE GPR data address */
       unsigned char      _iGprAddr;
       /* IE GPR data value */
       char               _szData[128];

   } READ_IETHERNET_SLAVE_DATA, *LPREAD_IETHERNET_SLAVE_DATA;

   typedef READ_IETHERNET_SLAVE_DATA
       MONITORING_IETHERNET_SLAVE, *LPMONITORING_IETHERNET_SLAVE;
