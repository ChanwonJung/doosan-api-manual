.. _struct_MONITORING_MISC:

MONITORING_MISC
===============

This structure provides **miscellaneous monitoring data** such as internal clock counter,  
flange I/O status, brake and button states, and motor electrical information.  
It is used internally to track auxiliary signals and robot status in real time.

.. list-table::
   :widths: 10 28 15 8 39
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_dSyncTime``
     - ``double``
     - -
     - Internal clock counter (synchronization time)
   * - 8
     - ``_iActualDI``
     - ``unsigned char[6]``
     - -
     - Flange Digital Input status (6 channels)
   * - 14
     - ``_iActualDO``
     - ``unsigned char[6]``
     - -
     - Flange Digital Output status (6 channels)
   * - 20
     - ``_iActualBK``
     - ``unsigned char[6]``
     - -
     - Brake state of each joint |br| 
       0: Released, 1: Locked
   * - 26
     - ``_iActualBT``
     - ``unsigned int[5]``
     - -
     - Robot button state (5 buttons; on/off status)
   * - 46
     - ``_fActualMC``
     - ``float[6]``
     - -
     - Motor input current (per joint, in amperes)
   * - 70
     - ``_fActualMT``
     - ``float[6]``
     - -
     - Motor temperature per joint (°C)

Total size: 94 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_MISC
   {
       /* inner clock counter */
       double         _dSyncTime;
       /* Flange Digital Input data */
       unsigned char  _iActualDI[NUM_FLANGE_IO];
       /* Flange Digital Output data */
       unsigned char  _iActualDO[NUM_FLANGE_IO];
       /* Brake state */
       unsigned char  _iActualBK[NUM_JOINT];
       /* Robot button state */
       unsigned int   _iActualBT[NUM_BUTTON];
       /* Motor input current */
       float          _fActualMC[NUM_JOINT];
       /* Motor temperature */
       float          _fActualMT[NUM_JOINT];
   } MONITORING_MISC, *LPMONITORING_MISC;

.. note::
   - ``_iActualBK`` corresponds to the joint brake status (0: released, 1: locked).  
   - ``_iActualBT`` represents the on/off state of five physical robot buttons.  
   - ``_fActualMC`` and ``_fActualMT`` allow temperature/current monitoring per joint.
