.. _struct_CONFIG_ENCODER_MODE:

CONFIG_ENCODER_MODE
===================

This structure defines the **encoder input mode configuration** for each encoder channel.  
It specifies how the A/B/Z/S signals are interpreted, their polarity or counting mode,  
and the pulse-per-revolution configuration.  
This is mainly used when setting up **external encoders** or **conveyor tracking encoders**.

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
     - 0~1
     - Encoder channel index
   * - 1
     - ``_iABMode``
     - ``unsigned char``
     - 0~4
     - **A/B phase mode configuration** |br|
       0: A/B not used |br|
       1: A(QEP), B(QEP) |br|
       2: A(Count), B(Direction) |br|
       3: A(Up Count), B(Not Used) |br|
       4: A(Down Count), B(Not Used)
   * - 2
     - ``_iZMode``
     - ``unsigned char``
     - 0~2
     - **Z-phase signal mode** |br|
       0: Not used |br|
       1: Cumulative compensation |br|
       2: Count clear
   * - 3
     - ``_iSMode``
     - ``unsigned char``
     - 0
     - S-phase signal mode (0: Not used)
   * - 4
     - ``_iInvMode``
     - ``unsigned char``
     - 0 or 1
     - Inversion mode (0: Forward, 1: Inversed)
   * - 8
     - ``_nPulseAZ``
     - ``unsigned int``
     - 0~100000
     - Number of A pulses per Z pulse (counts per revolution)

Total size: 12 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_ENCODER_MODE
   {
       /* Encoder channel: 0~1 */
       unsigned char _iChannel;

       /* A/B polarity mode
          0: A(Not Used), B(Not Used)
          1: A(QEP), B(QEP)
          2: A(Count), B(Direction)
          3: A(Up Count), B(Not Used)
          4: A(Down Count), B(Not Used)
       */
       unsigned char _iABMode;

       /* Z polarity mode
          0: Not Used
          1: Count Cumulative Compensation
          2: Count Clear
       */
       unsigned char _iZMode;

       /* S polarity mode (0: Not Used) */
       unsigned char _iSMode;

       /* Inversion mode (0: forward, 1: inversed) */
       unsigned char _iInvMode;

       /* A pulse count per Z pulse (0 ~ 100000) */
       unsigned int _nPulseAZ;

   } CONFIG_ENCODER_MODE, *LPCONFIG_ENCODER_MODE;
