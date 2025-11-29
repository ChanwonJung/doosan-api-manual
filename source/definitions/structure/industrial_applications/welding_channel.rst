.. _struct_WELDING_CHANNEL:

WELDING_CHANNEL
================

This structure defines the configuration parameters for an **analog welding channel**,  
including channel selection, signal type, constant values, and operating limits.  
It is used to set parameters for current and voltage channels in the welding interface.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_bTargetCh``
     - ``unsigned char``
     - 0~2
     - **Welding channel index** |br|
       (0: None, 1-2: Active channel)
   * - 1
     - ``_bTargetAT``
     - ``unsigned char``
     - 0 or 1
     - **Analog signal type** |br|
       (0: Current, 1: Voltage)
   * - 2
     - ``_ConstValue[2]``
     - ``float[2]``
     - -
     - Constant coefficients (A, B) used for linear conversion
   * - 10
     - ``_fMinValue``
     - ``float``
     - -
     - Minimum measurable or output value (default: 0)
   * - 14
     - ``_fMaxValue``
     - ``float``
     - -
     - Maximum measurable or output value (default: 0)

Total size: 18 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _WELDING_CHANNEL
   {
       /* Channel index: none(0), 1~2 */
       unsigned char _bTargetCh;

       /* Type: 0(current), 1(voltage) */
       unsigned char _bTargetAT;

       /* Constant parameters (A, B) */
       float _ConstValue[2];

       /* Minimum valid value */
       float _fMinValue;

       /* Maximum valid value */
       float _fMaxValue;

   } WELDING_CHANNEL, *LPWELDING_CHANNEL;