.. _struct_MODBUS_DATA:

MODBUS_DATA 
================

This is a structure information to store Modbus data, and consists of the following fields.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iType``
     - ``unsigned char``
     - -
     - 0: TCP, 1: RTU
   * - 1
     - ``_tData``
     - Union of :ref:`WRITE_MODBUS_TCP_DATA <struct_WRITE_MODBUS_DATA>` / :ref:`WRITE_MODBUS_RTU_DATA <struct_WRITE_MODBUS_RTU_DATA>`
     - -
     - Contains one of the following members based on ``_iType``
       
       - **_tcp**: 
         Modbus communication via **Ethernet (TCP/IP)**  
         Includes IP address, port, slave ID, and register information.  
       
       - **_rtu**: 
         Modbus communication via **serial interface (RS-485/RS-232)**  
         Includes TTY port, baud rate, parity, stop bits, and register data.  
       
       - **_szBuffer[70]** : ``unsigned char``  
         70-byte raw memory buffer used for serialization,  
         byte-level access, or network data packing.

Total size: 112 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MODBUS_DATA
   {
       /* 0: TCP, 1: RTU */
       unsigned char _iType;

       union {
           /* Modbus TCP (see WRITE_MODBUS_DATA) */
           WRITE_MODBUS_DATA     _tcp;   /* a.k.a. WRITE_MODBUS_TCP_DATA in some codebases */
           /* Modbus RTU (see WRITE_MODBUS_RTU_DATA) */
           WRITE_MODBUS_RTU_DATA _rtu;
           /* raw buffer for packing */
           unsigned char         _szBuffer[70];
       } _tData;

   } MODBUS_DATA, *LPMODBUS_DATA;