.. _struct_CONFIG_WORLD_COORDINATE:

CONFIG_WORLD_COORDINATE
=======================

This structure defines the configuration of the **world coordinate system**.  
It specifies the coordinate mapping type and the target transformation pose  
expressed as six floating-point values (X, Y, Z, RX, RY, RZ).

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
     - Coordinate mapping configuration: |br|
       0: World → Base |br|
       1: Base → Reference |br| 
       2: World → Reference |br|
   * - 1
     - ``_fPosition``
     - ``float[NUM_TASK]``
     - [mm, deg]
     - Target pose (6D transformation: X, Y, Z, RX, RY, RZ)

Total size: 25 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_WORLD_COORDINATE
   {
       /* Coordinate mapping type
          0: World → Base
          1: Base → Reference
          2: World → Reference
       */
       unsigned char _iType;

       /* Target pose (X, Y, Z, RX, RY, RZ) */
       float         _fPosition[NUM_TASK];

   } CONFIG_WORLD_COORDINATE, *LPCONFIG_WORLD_COORDINATE;
