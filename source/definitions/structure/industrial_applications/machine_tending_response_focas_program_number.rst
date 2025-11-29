.. _struct_MACHINE_TENDING_RESPONSE_FOCAS_PROGRAM_NUMBER:

MACHINE_TENDING_RESPONSE_FOCAS_PROGRAM_NUMBER
=============================================

This structure defines the **CNC program information response** from FOCAS,  
including both currently running and main program numbers.

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
     - Response status (0 = success)
   * - 2
     - ``_hHandle``
     - ``unsigned short``
     - -
     - FOCAS communication handle
   * - 4
     - ``_iRunningProgramNumber``
     - ``short``
     - -
     - Program number currently being executed
   * - 6
     - ``_iMainProgramNumber``
     - ``short``
     - -
     - Main (parent) program number

Total size: 8 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MACHINE_TENDING_RESPONSE_FOCAS_PROGRAM_NUMBER
   {
       short          _ErrorCode;               /* 0: success */
       unsigned short _hHandle;                 /* FOCAS handle */
       short          _iRunningProgramNumber;   /* running program number */
       short          _iMainProgramNumber;      /* main program number */
   } MACHINE_TENDING_RESPONSE_FOCAS_PROGRAM_NUMBER, *LPMACHINE_TENDING_RESPONSE_FOCAS_PROGRAM_NUMBER;
