.. _struct_MEASURE_CONVEYOR_DISTANCE_RESPONSE:

MEASURE_CONVEYOR_DISTANCE_RESPONSE
==================================

This structure defines the **conveyor distance measurement result**,  
providing information about conveyor speed, distance thresholds, and synchronization distance.  
It is typically used for verifying conveyor tracking parameters in a robot-conveyor integration setup.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fSpeed``
     - ``float``
     - [mm/s]
     - Conveyor belt speed
   * - 4
     - ``_fMinDistance``
     - ``float``
     - [mm]
     - Minimum measurable distance
   * - 8
     - ``_fWatchWinDist``
     - ``float``
     - [mm]
     - Watch window (active sensing range)
   * - 12
     - ``_fMaxDistance``
     - ``float``
     - [mm]
     - Maximum measurable distance
   * - 16
     - ``_fSyncOutDist``
     - ``float``
     - [mm]
     - Sync-out trigger distance for conveyor-robot synchronization

Total size: 20 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MEASURE_CONVEYOR_DISTANCE_RESPONSE
   {
       /* Conveyor speed (mm/s) */
       float _fSpeed;

       /* Minimum measurable distance (mm) */
       float _fMinDistance;

       /* Watch window distance (mm) */
       float _fWatchWinDist;

       /* Maximum measurable distance (mm) */
       float _fMaxDistance;

       /* Sync-out trigger distance (mm) */
       float _fSyncOutDist;

   } MEASURE_CONVEYOR_DISTANCE_RESPONSE, *LPMEASURE_CONVEYOR_DISTANCE_RESPONSE;
