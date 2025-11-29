.. _struct_CONVEYOR_TRACK:

CONVEYOR_TRACK
===============

This structure represents a **conveyor tracking status**,  
defining whether tracking is active, the synchronization state,  
and the tracking duration information.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iConId``
     - ``unsigned char``
     - 0~255
     - Conveyor identifier index
   * - 1
     - ``_bTracking``
     - ``unsigned char``
     - 0 or 1
     - **Tracking state flag** |br|
       0: Untracking |br|
       1: Tracking active
   * - 2
     - ``_bMate``
     - ``unsigned char``
     - 0 or 1
     - **Synchronization (“mate”) flag** |br|
       0: Not mated |br| 
       1: Mated
   * - 3
     - ``_fDuration``
     - ``float``
     - -
     - Tracking duration time (seconds)
   * - 7
     - ``_fDummy[5]``
     - ``float[5]``
     - -
     - Reserved buffer for internal data alignment

Total size: 27 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONVEYOR_TRACK
   {
       /* Conveyor ID */
       unsigned char _iConId;

       /* Tracking flag (0: untracking, 1: tracking) */
       unsigned char _bTracking;

       /* Mate flag (0: not mated, 1: mated) */
       unsigned char _bMate;

       /* Tracking duration time */
       float _fDuration;

       /* Reserved dummy array */
       float _fDummy[5];

   } CONVEYOR_TRACK, *LPCONVEYOR_TRACK;

.. note::
   - ``MONITOR_CONVEYOR`` → checks conveyor on/off state.  
   - ``CONVEYOR_OBJECT`` → defines an object carried on the conveyor.  
   - ``CONVEYOR_TRACK`` → tracks synchronization and runtime status.  
   - These structures work together for conveyor-based material handling and vision tracking.