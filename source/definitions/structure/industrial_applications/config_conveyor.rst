.. _struct_CONFIG_CONVEYOR:

CONFIG_CONVEYOR
================

This structure defines the **complete conveyor configuration**,  
combining basic conveyor setup, coordinate calibration, and distance control parameters.  
It allows a robot to interact with and track conveyor systems precisely.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_szName``
     - ``char[32]``
     - -
     - Conveyor name identifier
   * - 32
     - ``_tBasic``
     - :ref:`CONVEYOR_BASIC <struct_CONVEYOR_BASIC>`
     - -
     - Basic conveyor configuration (motion type, I/O setup)
   * - 51
     - ``_tCoord``
     - :ref:`CONVEYOR_COORD_EX <struct_CONVEYOR_COORD_EX>`
     - -
     - Conveyor coordinate calibration and reference system
   * - 80
     - ``_tDistance``
     - :ref:`CONVEYOR_DISTANCE <struct_CONVEYOR_DISTANCE>`
     - -
     - Distance and motion control parameters

Total size: 104 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONFIG_CONVEYOR
   {
       /* Conveyor name (identifier string) */
       char _szName[MAX_SYMBOL_SIZE];

       /* Basic conveyor setup */
       CONVEYOR_BASIC _tBasic;

       /* Coordinate calibration data */
       CONVEYOR_COORD_EX _tCoord;

       /* Distance and tracking configuration */
       CONVEYOR_DISTANCE _tDistance;

   } CONFIG_CONVEYOR, *LPCONFIG_CONVEYOR;

.. note::
   - ``CONFIG_CONVEYOR`` encapsulates all conveyor-related configurations.  
   - It integrates three views: |br|
     :ref:`CONVEYOR_BASIC <struct_CONVEYOR_BASIC>` → Physical setup |br|
     :ref:`CONVEYOR_COORD_EX <struct_CONVEYOR_COORD_EX>` → Spatial calibration |br| 
     :ref:`CONVEYOR_DISTANCE <struct_CONVEYOR_DISTANCE>` → Tracking parameters |br|
   - Used with conveyor-based tracking and vision synchronization features in automation systems.