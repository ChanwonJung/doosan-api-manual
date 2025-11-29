.. _struct_CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA:

CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA
======================================

This structure defines the **mapping configuration for digital welding interfaces**,  
used to interpret and convert between digital I/O signals and analog welding parameters.  
It specifies data format, scaling, and bit/byte offsets for the controller’s digital communication.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bEnable``
     - ``unsigned char``
     - 0 or 1
     - Enable flag |br|
       (0: Disabled, 1: Enabled)
   * - 1
     - ``_nDataType``
     - ``unsigned char``
     - 0 or 1
     - **Data interpretation type** |br|
       0: On/Off signal |br|
       1: Value signal
   * - 2
     - ``_nPositionalNumber``
     - ``unsigned char``
     - 0~2
     - **Decimal position** |br|
       0: 1 |br|
       1: 0.1 |br|
       2: 0.001
   * - 3
     - ``_fMinData``
     - ``float``
     - -
     - Minimum mapped data value
   * - 7
     - ``_fMaxData``
     - ``float``
     - -
     - Maximum mapped data value
   * - 11
     - ``_nByteOffset``
     - ``unsigned char``
     - 0~255
     - Byte offset within the digital frame
   * - 12
     - ``_nBitOffset``
     - ``unsigned char``
     - 0~7
     - Bit offset within the specified byte
   * - 13
     - ``_nComnDataType``
     - ``unsigned char``
     - 0~7
     - Communication data type |br|
       (0: 1-bit (Low active), 1: 1-bit (High active), 2: 2-bit |br|
       3: 4-bit, 4: 8-bit, 5: 15-byte, 6: 16-bit, 7: 32-bit)
   * - 14
     - ``_nMaxDigitSize``
     - ``unsigned char``
     - -
     - Maximum digital range value allowed for conversion

Total size: 15 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA
   {
       /* Enable: 0 = Disabled, 1 = Enabled */
       unsigned char _bEnable;

       /* Data type: 0 = On/Off, 1 = Value */
       unsigned char _nDataType;

       /* Decimal position factor: 0 = ×1, 1 = ×0.1, 2 = ×0.001 */
       unsigned char _nPositionalNumber;

       /* Minimum mapped data value */
       float _fMinData;

       /* Maximum mapped data value */
       float _fMaxData;

       /* Byte offset within communication frame */
       unsigned char _nByteOffset;

       /* Bit offset within the byte */
       unsigned char _nBitOffset;

       /* Communication data type (1~32 bit mapping) */
       unsigned char _nComnDataType;

       /* Maximum digital range value */
       unsigned char _nMaxDigitSize;

   } CONFIG_DIGITAL_WELDING_IF_MAPPING_DATA, *LPCONFIG_DIGITAL_WELDING_IF_MAPPING_DATA;

.. note::
   - Used to **map welding parameters** (voltage, current, etc.) to **digital protocol bits**.  
   - Supports diverse data types (bit, byte, word, dword).  
   - ``_nPositionalNumber`` adjusts for scaling precision in numeric values.  
   - Enables integration with **PLC-based welding controllers** or **digital fieldbus interfaces**.




