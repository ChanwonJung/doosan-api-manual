.. _struct_CONVEYOR_COORD_EX:

CONVEYOR_COORD_EX
=================

This structure defines the **conveyor coordinate configuration**,  
including encoder count-to-distance conversion, conveyor position,  
and reference coordinate system.  
It is used for conveyor calibration, tracking, and synchronization with the robot’s motion system.

.. list-table::
   :widths: 10 28 22 8 32
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iDistance2Count``
     - ``int``
     - -
     - Encoder counts per unit distance (used for linear conversion)
   * - 4
     - ``_tPosConCoord``
     - :ref:`POSITION <struct_POSITION>`
     - -
     - Conveyor coordinate origin position
   * - 28
     - ``_iTargetRef``
     - ``unsigned char``
     - 0 or 2
     - **Reference coordinate system** |br|
       0: Base frame |br|
       2: World frame

Total size: 29 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _CONVEYOR_COORD_EX
   {
       /* Count per unit distance */
       int _iDistance2Count;

       /* Conveyor coordinate origin position */
       POSITION _tPosConCoord;

       /* Reference coordinate system (0: base, 2: world) */
       unsigned char _iTargetRef;

   } CONVEYOR_COORD_EX, *LPCONVEYOR_COORD_EX;