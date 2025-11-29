.. _struct_SERIAL_PORT_NAME:

SERIAL_PORT_NAME
================

This structure defines the **name and port information** of a detected serial device.  
It is used when listing or identifying serial communication interfaces available on the system.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szPort``
     - ``char[16]``
     - ASCII
     - Serial port identifier (e.g., ``"COM3"``, ``"/dev/ttyUSB0"``)
   * - 16
     - ``_szName``
     - ``char[128]``
     - ASCII
     - Serial device name or description |br|
       (e.g., ``"FTDI USB-Serial Converter"``)

Total size: 144 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SERIAL_PORT_NAME
   {
       /* Serial port identifier (e.g., COM3, /dev/ttyUSB0) */
       char _szPort[16];
       /* Serial device name (e.g., FTDI USB-Serial Converter) */
       char _szName[128];

   } SERIAL_PORT_NAME, *LPSERIAL_PORT_NAME;