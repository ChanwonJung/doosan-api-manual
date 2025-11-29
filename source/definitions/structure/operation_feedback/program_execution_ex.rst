.. _struct_PROGRAM_EXECUTION_EX:

PROGRAM_EXECUTION_EX
====================

This structure provides extended information about program execution,  
including line tracking, elapsed time, and associated file name.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iLineNumber``
     - ``unsigned int``
     - ≥ 0
     - Line number currently being executed
   * - 4
     - ``_fElapseTime``
     - ``float``
     - s
     - Time elapsed since the start of program execution
   * - 8
     - ``_szFile``
     - ``char[MAX_STRING_SIZE]``
     - -
     - File name of the DRL program being executed

Total size: 264 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PROGRAM_EXECUTION_EX
   {
       /* line number currently executing */
       unsigned int _iLineNumber;

       /* total elapsed time (seconds) */
       float _fElapseTime;

       /* DRL program file name */
       char _szFile[MAX_STRING_SIZE];

   } PROGRAM_EXECUTION_EX, *LPPROGRAM_EXECUTION_EX;