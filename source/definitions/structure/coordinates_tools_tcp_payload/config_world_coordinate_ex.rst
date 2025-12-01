.. _struct_CONFIG_WORLD_COORDINATE_EX:

CONFIG_WORLD_COORDINATE_EX
==========================

This structure defines an **extended world coordinate configuration**,  
providing orientation type support through :ref:`POSITION_EX <struct_POSITION_EX>`.  
It extends :ref:`CONFIG_WORLD_COORDINATE <struct_CONFIG_WORLD_COORDINATE>` by  
adding data alignment bytes and a detailed orientation representation.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iType``
     - ``unsigned char``
     - 0-2
     - **Coordinate mapping type and flag** |br|
       0: world→base |br|
       1: base→ref |br|
       2: world→ref  
   * - 1
     - ``_iReserved[3]``
     - ``unsigned char[3]``
     - -
     - Reserved bytes for alignment
   * - 4
     - ``_tPosition``
     - :ref:`POSITION_EX <struct_POSITION_EX>`
     - [mm, deg]
     - Target position and orientation |br|
       (supports orientation type: Euler, Quaternion, etc.)

Total size: 32 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_WORLD_COORDINATE_EX
   {
       /* Setting type:
          0: world→base
          1: base→ref
          2: world→ref
          (Enable flag handled internally as bit field)
       */
       unsigned char _iType;

       /* Reserved bytes for alignment */
       unsigned char _iReserved[3];

       /* Target pose and orientation */
       POSITION_EX   _tPosition;

   } CONFIG_WORLD_COORDINATE_EX, *LPCONFIG_WORLD_COORDINATE_EX;  // SUPPORT_ORIENTATION_TYPE
