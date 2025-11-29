.. _struct_SYSTEM_VERSION_EX:

SYSTEM_VERSION_EX
=================

This structure contains extended version information of the robot controller, including per-axis inverter versions and additional board information.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szPackage``
     - ``char[32]``
     - -
     - Package Version
   * - 32
     - ``_szSmartTp``
     - ``char[32]``
     - -
     - Higher Level Controller (SmartTP) Version
   * - 64
     - ``_szController``
     - ``char[32]``
     - -
     - Lower Level Controller Version
   * - 96
     - ``_szInterpreter``
     - ``char[32]``
     - -
     - DRL Interpreter Version
   * - 128
     - ``_szInverter``
     - ``char[NUM_AXIS][32]``
     - -
     - Inverter Version (per axis), starts at byte 128
   * - 320
     - ``_szSafetyBoard``
     - ``char[32]``
     - -
     - Safety Board Version
   * - 352
     - ``_szRobotSerial``
     - ``char[32]``
     - -
     - Robot Serial Number
   * - 384
     - ``_szRobotModel``
     - ``char[32]``
     - -
     - Robot Model Number
   * - 416
     - ``_szJTSBoard``
     - ``char[32]``
     - -
     - JTS Board Version
   * - 448
     - ``_szFlangeBoard``
     - ``char[32]``
     - -
     - Flange Board Version
   * - 480
     - ``_szSVMBoard``
     - ``char[32]``
     - -
     - SVM Board Version

Total size: 512 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_VERSION_EX
   {
       char                        _szPackage[MAX_SYMBOL_SIZE];
       /* smarttp version */
       char                        _szSmartTp[MAX_SYMBOL_SIZE];
       /* controller version */
       char                        _szController[MAX_SYMBOL_SIZE];
       /* interpreter version */
       char                        _szInterpreter[MAX_SYMBOL_SIZE];
       /* inverter version */
       char                        _szInverter[NUM_AXIS][MAX_SYMBOL_SIZE];
       /* SafetyBoard version */
       char                        _szSafetyBoard[MAX_SYMBOL_SIZE];
       /* robot serial number */
       char                        _szRobotSerial[MAX_SYMBOL_SIZE];
       /* robot model number*/
       char                        _szRobotModel[MAX_SYMBOL_SIZE];
       /* jts board version */
       char                        _szJTSBoard[MAX_SYMBOL_SIZE];
       /* flange board version */
       char                        _szFlangeBoard[MAX_SYMBOL_SIZE];
       /* flange board version */
       char                        _szSVMBoard[MAX_SYMBOL_SIZE];
   } SYSTEM_VERSION_EX, *LPSYSTEM_VERSION_EX;
