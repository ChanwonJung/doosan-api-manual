.. _struct_CONFIG_WELDING_DETAIL_INFO:

CONFIG_WELDING_DETAIL_INFO
==========================

This structure defines detailed **analog welding channel parameters**,  
including the type, channel number, and configured minimum/maximum output limits.  
It provides low-level configuration data for current and voltage control channels.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iChannel``
     - ``unsigned char``
     - 0~2
     - **Channel index** |br|
       0: Not specified |br|
       1~2: Active analog channels
   * - 1
     - ``_iChannelType``
     - ``unsigned char``
     - 0~1
     - **Channel type** |br|
       0: Current channel |br|
       1: Voltage channel
   * - 2
     - ``_iRealMinOut``
     - ``float``
     - -
     - Real measured minimum output value
   * - 6
     - ``_iMinOut``
     - ``float``
     - -
     - Configured minimum output setpoint
   * - 10
     - ``_iRealMaxOut``
     - ``float``
     - -
     - Real measured maximum output value
   * - 14
     - ``_iMaxOut``
     - ``float``
     - -
     - Configured maximum output setpoint

Total size: 18 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_WELDING_DETAIL_INFO
   {
       /* Channel index: 0 = none, 1~2 = valid channels */
       unsigned char _iChannel;

       /* Channel type: 0 = current, 1 = voltage */
       unsigned char _iChannelType;

       /* Real minimum output value */
       float _iRealMinOut;

       /* Configured minimum output */
       float _iMinOut;

       /* Real maximum output value */
       float _iRealMaxOut;

       /* Configured maximum output */
       float _iMaxOut;

   } CONFIG_WELDING_DETAIL_INFO, *LPCONFIG_WELDING_DETAIL_INFO;