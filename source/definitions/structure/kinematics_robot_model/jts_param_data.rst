.. _struct_JTS_PARAM_DATA:

JTS_PARAM_DATA
===============
This structure defines the **joint torque sensor (JTS)** calibration parameters, including offset and scale values per joint.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fOffset``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - JTS offset for each joint
   * - 24
     - ``_fScale``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - JTS scale factor for each joint

Total size: 48 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _JTS_PARAM_DATA
   {
       /* jts offset */
       float _fOffset[NUMBER_OF_JOINT];
       /* jts scale */
       float _fScale[NUMBER_OF_JOINT];
   } JTS_PARAM_DATA, *LPJTS_PARAM_DATA;
   
    typedef JTS_PARAM_DATA
        CALIBRATE_JTS_RESPONSE, *LPCALIBRATE_JTS_RESPONSE;