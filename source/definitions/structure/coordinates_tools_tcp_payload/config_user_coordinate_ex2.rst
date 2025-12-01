.. _struct_CONFIG_USER_COORDINATE_EX2:

CONFIG_USER_COORDINATE_EX2
==========================

This structure defines an **extended user coordinate configuration**,  
providing alignment with :ref:`POSITION_EX <struct_POSITION_EX>` for enhanced orientation support.  
It extends :ref:`CONFIG_USER_COORDINATE_EX <struct_CONFIG_USER_COORDINATE_EX>`  
by including padding bytes for alignment and extended orientation handling.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iTargetRef``
     - ``unsigned char``
     - -
     - Base: 0 / World: 2 (Coordinate Reference)
   * - 1
     - ``_iReserved[3]``
     - ``unsigned char[3]``
     - -
     - Reserved bytes for alignment
   * - 4
     - ``_tTargetPos``
     - :ref:`POSITION_EX <struct_POSITION_EX>`
     - [mm, deg]
     - Target position and orientation in task coordinates |br|
       (extended structure supporting orientation type)
   * - 28
     - ``_iUserID``
     - ``unsigned char``
     - -
     - User coordinate ID
   * - 29
     - ``_iReserved_[3]``
     - ``unsigned char[3]``
     - -
     - Reserved bytes for data alignment

Total size: 32 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_USER_COORDINATE_EX2
   {
       /* Reference coordinate system (0: Base, 2: World) */
       unsigned char _iTargetRef;
       /* Reserved bytes for alignment */
       unsigned char _iReserved[3];
       /* Target position and orientation [X, Y, Z, Rx, Ry, Rz] */
       POSITION_EX   _tTargetPos;
       /* User coordinate ID */
       unsigned char _iUserID;
       /* Reserved bytes for alignment */
       unsigned char _iReserved_[3];

   } CONFIG_USER_COORDINATE_EX2, *LPCONFIG_USER_COORDINATE_EX2;  // SUPPORT_ORIENTATION_TYPE
