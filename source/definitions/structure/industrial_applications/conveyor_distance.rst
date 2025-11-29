.. _struct_CONVEYOR_DISTANCE:

CONVEYOR_DISTANCE
=================

This structure defines the **distance and motion configuration**  
for a conveyor system, including speed, distance limits, and tracking thresholds.  
It is typically used to fine-tune the synchronization between the robot  
and a moving conveyor.

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
     - -
     - Conveyor belt speed (m/s)
   * - 4
     - ``_iSpeedFilterSize``
     - ``unsigned int``
     - -
     - Size of moving average filter applied to speed measurement
   * - 8
     - ``_fMinDistance``
     - ``float``
     - -
     - Minimum allowed conveyor distance
   * - 12
     - ``_fWatchWinDist``
     - ``float``
     - -
     - Watch window distance threshold for object monitoring
   * - 16
     - ``_fMaxDistance``
     - ``float``
     - -
     - Maximum allowed conveyor distance
   * - 20
     - ``_fOutTrackingDist``
     - ``float``
     - -
     - Output tracking distance threshold for synchronization

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONVEYOR_DISTANCE
   {
       /* Conveyor speed (m/s) */
       float _fSpeed;
       /* Speed moving average filter window */
       unsigned int _iSpeedFilterSize;
       /* Minimum distance (m) */
       float _fMinDistance;
       /* Watch window distance (m) */
       float _fWatchWinDist;
       /* Maximum distance (m) */
       float _fMaxDistance;
       /* Output tracking distance (m) */
       float _fOutTrackingDist;

   } CONVEYOR_DISTANCE, *LPCONVEYOR_DISTANCE;