.. _struct_CONVEYOR_BASIC:

CONVEYOR_BASIC
===============

This structure defines the **basic conveyor configuration**,  
including motion type (linear/circular), external encoder input,  
and digital output configuration for conveyor control.

It serves as a foundational structure for higher-level conveyor operations,  
such as synchronization, tracking, and speed regulation.

.. list-table::
   :widths: 10 28 22 8 45
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iType``
     - ``unsigned char``
     - 0~1
     - **Conveyor motion type** |br|
       0: Linear conveyor |br|
       1: Circular conveyor
   * - 1
     - ``ExtEncoderInput``
     - *struct*
     - -
     - **External encoder input configuration block:** |br|
       ``_iEncoderChannel``: Encoder channel index (0~1) |br|
       ``_iTriggerChannel``: Trigger input index (0~1) |br|
       ``_iTriggerEdgeType``: Edge type (0: falling, 1: rising) |br|
       ``_fTriggerMuteTime``: Trigger mute interval (sec) 
   * - 10
     - ``DigitalOutput[2]``
     - *struct[2]*
     - -
     - **Digital output configuration array:** |br|
       ``_iChannel``: Output channel (-1: not used, 0~15: used) |br|
       ``_iValue``: Output state (0: low, 1: high)

Total size: 19 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONVEYOR_BASIC
   {
       /* Motion type (0: linear, 1: circular) */
       unsigned char _iType;

       /* External encoder input configuration */
       struct {
           unsigned char _iEncoderChannel;   /* encoder index: 0~1 */
           unsigned char _iTriggerChannel;   /* trigger input: 0~1 */
           unsigned char _iTriggerEdgeType;  /* 0: falling, 1: rising */
           float          _fTriggerMuteTime; /* mute time (seconds) */
       } ExtEncoderInput;

       /* Conveyor digital output configuration */
       struct {
           char          _iChannel;   /* output channel (-1: not used, 0~15: used) */
           unsigned char _iValue;     /* output value (0: low, 1: high) */
       } DigitalOutput[2];

   } CONVEYOR_BASIC, *LPCONVEYOR_BASIC;

.. note::
   - ``CONVEYOR_BASIC`` defines low-level conveyor I/O control setup.  
   - The **ExtEncoderInput** block manages synchronization and triggering.  
   - The **DigitalOutput** array allows control of up to **two outputs** for conveyor operation.  
   - Commonly used with higher-level conveyor setup APIs like  
     :ref:`config_conveyor <struct_CONFIG_CONVEYOR>`.
