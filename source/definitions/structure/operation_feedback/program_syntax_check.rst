.. _struct_PROGRAM_SYNTAX_CHECK:

PROGRAM_SYNTAX_CHECK
====================

This structure represents a syntax validation request for a program source.  
It specifies the text length of the DRL (Doosan Robot Language) program to be checked.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTextLength``
     - ``unsigned int``
     - ≥ 0
     - Length of the DRL source text (bytes)
   * - 4
     - ``_lpszTextString``
     - ``char*``
     - *(optional)*
     - Pointer to the program source text (not serialized)

Total size: **4 bytes**

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PROGRAM_SYNTAX_CHECK
   {
       /* source text length */
       unsigned int _iTextLength;

       /* optional pointer to text string (unused in struct serialization) */
       // char* _lpszTextString;

   } PROGRAM_SYNTAX_CHECK, *LPPROGRAM_SYNTAX_CHECK;