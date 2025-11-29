.. _struct_MACHINE_TENDING_RESPONSE_FOCAS_CNC_PARAM:

MACHINE_TENDING_RESPONSE_FOCAS_CNC_PARAM
========================================

This structure defines the **response data** for CNC parameter requests made through the FOCAS interface.  
It includes error information, communication handle, and detailed parameter data (type and raw bytes).

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_ErrorCode``
     - ``short``
     - -
     - Response status code (0 = success, otherwise error)
   * - 2
     - ``_hHandle``
     - ``unsigned short``
     - -
     - FOCAS communication handle identifier
   * - 4
     - ``tData._iDataNumber``
     - ``short``
     - -
     - CNC data number (parameter index)
   * - 6
     - ``tData._iDataType``
     - ``short``
     - -
     - Axis number or parameter type
   * - 8
     - ``tData._Data[256]``
     - ``char[256]``
     - -
     - Raw parameter data block (byte array)

Total size: 264 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_RESPONSE_FOCAS_CNC_PARAM
   {
       short          _ErrorCode;     /* 0: success, otherwise error */
       unsigned short _hHandle;       /* FOCAS handle */
       struct
       {
           short  _iDataNumber;       /* parameter index */
           short  _iDataType;         /* axis number or type */
           char   _Data[256];         /* parameter data bytes */
       } tData;
   } MACHINE_TENDING_RESPONSE_FOCAS_CNC_PARAM, *LPMACHINE_TENDING_RESPONSE_FOCAS_CNC_PARAM;
