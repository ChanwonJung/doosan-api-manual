.. _struct_FLANGE_SERIAL_DATA:

FLANGE_SERIAL_DATA
==================

Serial communication information is defined using a **union**, composed of:

- Serial communication **setting information** (``_tConfig``)
- Serial communication **data information** (``_tValue``)

It is used with ``_iCommand`` to determine which field is valid: 

- ``0`` : Open
- ``1`` : Close
- ``2`` : Send
- ``3`` : Receive

.. list-table::
   :widths: 10 30 18 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iCommand``
     - ``unsigned char``
     - 0~3
     - Serial communication command |br|
       (0: Open, 1: Close, 2: Send, 3: Recv)
   * - 1
     - ``_tData``
     - ``union``
     - -
     - Contains either configuration info or data buffer.

**_tConfig structure (Serial Configuration):** |br|
Union for serial communication information is defined as follows.

.. list-table::
   :widths: 10 25 18 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tConfig._szBaudrate``
     - ``unsigned char[7]``
     - ASCII
     - 7byte baudrate value (e.g., ``"0115200"``)
   * - 7
     - ``_tConfig._szDataLength``
     - ``unsigned char``
     - 0~7
     - byte size
   * - 8
     - ``_tConfig._szParity``
     - ``unsigned char``
     - 0: None, 1: Odd, 2: Even
     - Parity Check
   * - 9
     - ``_tConfig._szStopBit``
     - ``unsigned char``
     - 1 or 2
     - Stop bits

**_tValue structure (Serial Data Buffer):** |br|
Serial communication data information is defined as follows.

.. list-table::
   :widths: 10 25 18 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tValue._iLength``
     - ``unsigned short``
     - -
     - RX/TX data length (bytes)
   * - 2
     - ``_tValue._szValue``
     - ``unsigned char[MAX_SYMBOL_SIZE]``
     - -
     - Data buffer (up to 32 bytes)

Total size: 36 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _FLANGE_SERIAL_DATA
   {
       unsigned char _iCommand;   // 0: Open, 1: Close, 2: Send, 3: Recv
       union {
           struct {
               unsigned char _szBaudrate[7];  // "0115200"(ASCII)
               unsigned char _szDataLength;   // 0: 1bit, 7: 8bit
               unsigned char _szParity;       // 0x00: None, 0x01: Odd, 0x02: Even
               unsigned char _szStopBit;      // 0x01: 1 Stop bit, 0x02: 2 Stop bits
           } _tConfig;

           struct {
               unsigned short _iLength;             // RX Data Length
               unsigned char  _szValue[MAX_SYMBOL_SIZE]; // RX/TX Data (32 bytes)
           } _tValue;
       } _tData;
   } FLANGE_SERIAL_DATA, *LPFLANGE_SERIAL_DATA;