.. _struct_PROGRAM_ERROR:

PROGRAM_ERROR
=============

This structure stores **program-level error information**,  
including the error code, line number, and DRL file name in which the error occurred.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iError``
     - ``unsigned int``
     - -
     - Error code (see DRL error definitions)
   * - 4
     - ``_nLine``
     - ``unsigned int``
     - ≥ 0
     - Line number where the error occurred
   * - 8
     - ``_szFile``
     - ``char[MAX_STRING_SIZE]``
     - -
     - File name in which the error was detected

Total size: 264 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PROGRAM_ERROR
   {
       /* DRL error code */
       unsigned int _iError;

       /* line number of error occurrence */
       unsigned int _nLine;

       /* associated file name */
       char _szFile[MAX_STRING_SIZE];

   } PROGRAM_ERROR, *LPPROGRAM_ERROR;