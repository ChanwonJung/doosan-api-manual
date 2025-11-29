.. _struct_RT_INPUT_DATA_LIST:

RT_INPUT_DATA_LIST
==================

This structure contains **real-time external input/output data** used for  
external control mode (Realtime External Control).  
It aggregates force/torque sensor data, digital/analog I/O, and reserved fields  
for extended interface support.

.. list-table::
   :widths: 10 28 18 8 36
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fExternalForceTorque``
     - ``float[NUM_JOINT]``
     - -
     - External force/torque values applied to each joint |br|
       (Typically 6 channels: Fx, Fy, Fz, Tx, Ty, Tz)
   * - 24
     - ``_iExternalDI``
     - ``unsigned short``
     - -
     - External digital input bitfield |br|
       (Each bit corresponds to an external DI channel)
   * - 26
     - ``_iExternalDO``
     - ``unsigned short``
     - -
     - External digital output bitfield |br|
       (Each bit corresponds to an external DO channel)
   * - 28
     - ``_fExternalAnalogInput``
     - ``float[6]``
     - -
     - External analog input channels (up to 6)
   * - 52
     - ``_fExternalAnalogOutput``
     - ``float[6]``
     - -
     - External analog output channels (up to 6)
   * - 76
     - ``_iReserved``
     - ``unsigned char[256]``
     - -
     - Reserved for future expansion or vendor-specific data

Total size: 518 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _RT_INPUT_DATA_LIST
   {
       /* External Force Torque */
       float          _fExternalForceTorque[NUM_JOINT];
       /* External Digital Input */
       unsigned short _iExternalDI;
       /* External Digital Output */
       unsigned short _iExternalDO;
       /* external analog input (6 channel) */
       float          _fExternalAnalogInput[6];
       /* external analog output (6 channel) */
       float          _fExternalAnalogOutput[6];
       /* Reserved */
       unsigned char  _iReserved[256];
   } RT_INPUT_DATA_LIST, *LPRT_INPUT_DATA_LIST;

.. note::
   - ``_fExternalForceTorque`` provides the real-time measured external forces/torques on each joint.  
   - ``_iExternalDI`` and ``_iExternalDO`` represent bitmapped I/O data.  
   - ``_fExternalAnalogInput`` / ``_fExternalAnalogOutput`` store voltage or current values.  
   - ``_iReserved`` is **reserved for future firmware updates** or custom interfaces.