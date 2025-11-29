.. _struct_SYSTEM_VERSION:

SYSTEM_VERSION
================

This is structure information for checking detailed version information of the robot controller, and is composed of the following fields.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szSmartTp``
     - ``char[32]``
     - -
     - Higher Level Controller (SmartTP) Version
   * - 32
     - ``_szController``
     - ``char[32]``
     - -
     - Lower Level Controller Version
   * - 64
     - ``_szInterpreter``
     - ``char[32]``
     - -
     - DRL Interpreter Version
   * - 96
     - ``_szInverter``
     - ``char[32]``
     - -
     - Inverter Version
   * - 128
     - ``_szSafetyBoard``
     - ``char[32]``
     - -
     - Safety Board Version
   * - 160
     - ``_szRobotSerial``
     - ``char[32]``
     - -
     - Robot Serial Number
   * - 192
     - ``_szRobotModel``
     - ``char[32]``
     - -
     - Robot Model Number
   * - 224
     - ``_szJTSBoard``
     - ``char[32]``
     - -
     - JTS Board Version
   * - 256
     - ``_szFlangeBoard``
     - ``char[32]``
     - -
     - Flange Board Version

Total size: 288 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SYSTEM_VERSION
   {
       char _szSmartTp[MAX_SYMBOL_SIZE];     /* Higher Level Controller */
       char _szController[MAX_SYMBOL_SIZE];  /* Lower Level Controller  */
       char _szInterpreter[MAX_SYMBOL_SIZE]; /* DRL Interpreter         */
       char _szInverter[MAX_SYMBOL_SIZE];    /* Inverter Info           */
       char _szSafetyBoard[MAX_SYMBOL_SIZE]; /* Safety Board Info       */
       char _szRobotSerial[MAX_SYMBOL_SIZE]; /* Robot Serial No.        */
       char _szRobotModel[MAX_SYMBOL_SIZE];  /* Robot Model No.         */
       char _szJTSBoard[MAX_SYMBOL_SIZE];    /* JTS Board Info          */
       char _szFlangeBoard[MAX_SYMBOL_SIZE]; /* Flange Board Info       */
   } SYSTEM_VERSION, *LPSYSTEM_VERSION;
