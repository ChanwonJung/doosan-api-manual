.. _struct_LOG_ALARM:

LOG_ALARM
==========

This is structure information for checking functional and operational errors when they occur due to inside/outside factors in the robot controller, and is composed of the following fields.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**

   * - 0
     - ``_iLevel``
     - ``unsigned char``
     - -
     - 0: Info, 1: Warning, 2: Alarm

   * - 1
     - ``_iGroup``
     - ``unsigned char``
     - -
     - Classification Number (Classification Code)

   * - 2
     - ``_iIndex``
     - ``unsigned int``
     - -
     - Log Number (Message Number)

   * - 6
     - ``_szParam1``
     - ``char[256]``
     - -
     - Reservation Space: 256

   * - 262
     - ``_szParam2``
     - ``char[256]``
     - -
     - Reservation Space: 256

   * - 518
     - ``_szParam3``
     - ``char[256]``
     - -
     - Reservation Space: 256

Total size: 774 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _LOG_ALARM
   {
       unsigned char _iLogLevel;   /* Info:0, Warning:1, Alarm:2 */
       unsigned char _iCategory;   /* Classification code */
       unsigned int  _iLogNo;      /* Message number */
       char          _szParam1[256];
       char          _szParam2[256];
       char          _szParam3[256];
   } LOG_ALARM, *LPLOG_ALARM;

   typedef LOG_ALARM MONITORING_ALARM;

Classification and error messages deliver previously defined contents and send related parameters if needed. Refer to the log and alarm definition part for further details.
