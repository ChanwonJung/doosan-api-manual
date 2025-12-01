.. _struct_PROGRAM_WATCH_VARIABLE:

PROGRAM_WATCH_VARIABLE
======================

This structure defines a variable entry for program **watch mode**,  
allowing monitoring of DRL variables during execution.

.. list-table::
   :widths: 10 30 20 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iDivision``
     - ``unsigned char``
     - 0 or 1
     - **Variable scope** |br|
       0: Installation variable |br|
       1: General variable
   * - 1
     - ``_iType``
     - ``unsigned char``
     - 0~6
     - **Variable data type** |br|
       (0: Bool, 1: Int, 2: Float 3: String |br|
       4: POSJ, 5: POSX, 6: Unknown)
   * - 2
     - ``_szName``
     - ``char[128]``
     - -
     - Variable name
   * - 130
     - ``_szData``
     - ``char[128]``
     - -
     - Variable data (string representation)

Total size: 258 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _PROGRAM_WATCH_VARIABLE
   {
       /* variable scope: installation(0) or general(1) */
       unsigned char _iDivision;

       /* variable type: bool(0), int(1), float(2), string(3), posj(4), posx(5), unknown(6) */
       unsigned char _iType;

       /* variable name */
       char _szName[128];

       /* variable value as string */
       char _szData[128];

   } PROGRAM_WATCH_VARIABLE, *LPPROGRAM_WATCH_VARIABLE;