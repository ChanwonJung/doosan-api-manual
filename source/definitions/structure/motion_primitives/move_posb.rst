.. _struct_MOVE_POSB:

MOVE_POSB
=========

This is a structure for setting waypoint information when moveb motion is controlled in the robot controller, and is composed of the following fields.

.. list-table::
   :widths: 10 28 18 10 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fTargetPos``
     - ``float[2][NUM_TASK]``
     - -
     - Location Information (#1, #2) — information on six task spaces
   * - 48
     - ``_iBlendType``
     - ``unsigned char``
     - 0x00~0x01
     - Motion Type (combination of first and second motion) |br|
       0: Line, 1: Circle
   * - 49
     - ``_fBlendRad``
     - ``float``
     - -
     - Curve Curvature — radius information (mm)

Total size: 53 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MOVE_POSB 
   {
       float         _fTargetPos[2][NUM_TASK]; /* q: two locations (#1,#2) in task space */
       unsigned char _iBlendType;              /* blending motion type (line:0, circle:1) */
       float         _fBlendRad;               /* blending radius (mm) */
   } MOVE_POSB, *LPMOVE_POSB;


.. note::
   - ``moveb`` is a **blended motion** combining linear and circular segments. |br|
     - **Line motion** requires one waypoint (excluding the start point). |br|
     - **Circle motion** requires two waypoints (excluding the start point). |br|
     Thus, the second position (#2) is ignored in line mode. |br|
   - The **base coordinate** is used as the reference frame when operating in **base mode**,  
     while the **tool coordinate** is used when operating in **tool mode**.