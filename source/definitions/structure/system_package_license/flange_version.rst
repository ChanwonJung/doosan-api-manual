.. _struct_FLANGE_VERSION:

FLANGE_VERSION
===============

This structure provides version information about the **robot flange board**,  
including its hardware version and packet type.

.. list-table::
   :widths: 10 25 15 10 40
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``BoardNo``
     - ``unsigned char``
     - -
     - Flange board number (ID of the connected flange)
   * - 1
     - ``PacketType``
     - ``unsigned short``
     - -
     - Communication packet type used by the flange board
   * - 3
     - ``res``
     - ``unsigned char``
     - -
     - Reserved (for future use)
   * - 4
     - ``iFlangeHwVer``
     - ``unsigned char``
     - -
     - Flange hardware version number

Total size: 5 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _FLANGE_VERSION
   {
       unsigned char  BoardNo;        /* Flange board number */
       unsigned short PacketType;     /* Communication packet type */
       unsigned char  res;            /* Reserved */
       unsigned char  iFlangeHwVer;   /* Hardware version */
   } FLANGE_VERSION, *LPFLANGE_VERSION;
