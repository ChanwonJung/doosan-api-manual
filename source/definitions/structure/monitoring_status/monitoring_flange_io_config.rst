.. _struct_MONITORING_FLANGE_IO_CONFIG:

MONITORING_FLANGE_IO_CONFIG
===========================

This structure provides detailed monitoring information on the **flange I/O configuration**,  
including analog/digital pin multiplexing, serial port settings, and safety modes.

.. list-table::
   :widths: 10 28 15 10 37
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualAI``
     - ``float[MAX_FLANGE_AI]``
     - -
     - Actual analog input values (AI0~AI3)
   * - 16
     - ``_iX1Rs485FAIPinMux``
     - ``unsigned char``
     - -
     - X1 RS485 / Analog Input pin multiplexing
   * - 17
     - ``_iX2Rs485FAIPinMux``
     - ``unsigned char``
     - -
     - X2 RS485 / Analog Input pin multiplexing
   * - 18
     - ``_iX1DOBjtType``
     - ``unsigned char``
     - -
     - X1 Digital Output transistor type (BJT)
   * - 19
     - ``_iX2DOBjtType``
     - ``unsigned char``
     - -
     - X2 Digital Output transistor type (BJT)
   * - 20
     - ``_iVoutLevel``
     - ``unsigned char``
     - -
     - Voltage output level setting
   * - 21
     - ``_iFAI0Mode``
     - ``unsigned char``
     - -
     - Analog Input 0 mode (0: voltage, 1: current)
   * - 22
     - ``_iFAI1Mode``
     - ``unsigned char``
     - -
     - Analog Input 1 mode (0: voltage, 1: current)
   * - 23
     - ``_iFAI2Mode``
     - ``unsigned char``
     - -
     - Analog Input 2 mode (0: voltage, 1: current)
   * - 24
     - ``_iFAI3Mode``
     - ``unsigned char``
     - -
     - Analog Input 3 mode (0: voltage, 1: current)
   * - 25
     - ``_szX1Baudrate``
     - ``unsigned char[7]``
     - "0115200" (ASCII)
     - X1 RS485 baudrate string
   * - 32
     - ``_szX1DataLength``
     - ``unsigned char``
     - 0~7
     - X1 Serial data bit length (0: 1bit, 7: 8bit)
   * - 33
     - ``_szX1Parity``
     - ``unsigned char``
     - 0x00~0x02
     - X1 Serial parity (0: None, 1: Odd, 2: Even)
   * - 34
     - ``_szX1StopBit``
     - ``unsigned char``
     - 0x01~0x02
     - X1 Serial stop bit count
   * - 35
     - ``_szX2Baudrate``
     - ``unsigned char[7]``
     - "0115200" (ASCII)
     - X2 RS485 baudrate string
   * - 42
     - ``_szX2DataLength``
     - ``unsigned char``
     - 0~7
     - X2 Serial data bit length (0: 1bit, 7: 8bit)
   * - 43
     - ``_szX2Parity``
     - ``unsigned char``
     - 0x00~0x02
     - X2 Serial parity (0: None, 1: Odd, 2: Even)
   * - 44
     - ``_szX2StopBit``
     - ``unsigned char``
     - 0x01~0x02
     - X2 Serial stop bit count
   * - 45
     - ``_iServoSafetyMode``
     - ``unsigned char``
     - -
     - Servo safety mode flag
   * - 46
     - ``_iInterruptSafetyMode``
     - ``unsigned char``
     - -
     - Interrupt safety mode flag

Total size: 63 bytes
 
**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_FLANGE_IO_CONFIG
   {
       float          _iActualAI[MAX_FLANGE_AI];   /* Analog input values */
       unsigned char  _iX1Rs485FAIPinMux;          /* X1 RS485/AI pin mux */
       unsigned char  _iX2Rs485FAIPinMux;          /* X2 RS485/AI pin mux */
       unsigned char  _iX1DOBjtType;               /* X1 DO transistor type */
       unsigned char  _iX2DOBjtType;               /* X2 DO transistor type */
       unsigned char  _iVoutLevel;                 /* Voltage output level */
       unsigned char  _iFAI0Mode;                  /* AI0 mode (0: V, 1: I) */
       unsigned char  _iFAI1Mode;                  /* AI1 mode */
       unsigned char  _iFAI2Mode;                  /* AI2 mode */
       unsigned char  _iFAI3Mode;                  /* AI3 mode */
       unsigned char  _szX1Baudrate[7];            /* RS485 X1 baudrate string */
       unsigned char  _szX1DataLength;             /* Data bits (0~7) */
       unsigned char  _szX1Parity;                 /* 0:None, 1:Odd, 2:Even */
       unsigned char  _szX1StopBit;                /* Stop bit count */
       unsigned char  _szX2Baudrate[7];            /* RS485 X2 baudrate string */
       unsigned char  _szX2DataLength;             /* Data bits (0~7) */
       unsigned char  _szX2Parity;                 /* 0:None, 1:Odd, 2:Even */
       unsigned char  _szX2StopBit;                /* Stop bit count */
       unsigned char  _iServoSafetyMode;           /* Servo safety mode */
       unsigned char  _iInterruptSafetyMode;       /* Interrupt safety mode */
   } MONITORING_FLANGE_IO_CONFIG, *LPMONITORING_FLANGE_IO_CONFIG;
