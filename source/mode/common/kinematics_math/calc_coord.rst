.. _calc_coord:

calc_coord
------------------------------------------
This function computes a **new user Cartesian coordinate system** by using up to 4 input poses  
(`fTargetPos1`–`fTargetPos4`) and an input mode (`nInputMode`).  
The reference system is defined by `eTargetRef`.  
This feature is available in controller firmware **M2.5 or higher**.

Depending on the number of input points and the mode, the algorithm determines  
the X-, Y-, and Z-axis directions as follows:

- **1 point (`nCnt = 1`)** → The coordinate system is identical to the pose of `fTargetPos1`.  
- **2 points (`nCnt = 2`)**
  - `nInputMode = 0`: Z-axis is defined by the current Tool-Z direction projected orthogonally to the plane formed by X-axis (from `x1` to `x2`).  
  - `nInputMode = 1`: Z-axis is defined based on the Z direction of `x1`, orthogonalized against the X-axis.  
- **3 points (`nCnt = 3`)** → X-axis is defined by `x1 → x2`, Z-axis by the cross product of `(x2 - x1)` and `(x3 - x1)`.  
- **4 points (`nCnt = 4`)** → Same as the 3-point definition, but uses the 4th point for orientation refinement.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 977)

.. code-block:: cpp

    LPROBOT_POSE calc_coord(
        unsigned short nCnt,
        unsigned short nInputMode,
        COORDINATE_SYSTEM eTargetRef,
        float fTargetPos1[NUM_TASK],
        float fTargetPos2[NUM_TASK],
        float fTargetPos3[NUM_TASK],
        float fTargetPos4[NUM_TASK]
    ) {
        return _calc_coord(_rbtCtrl, nCnt, nInputMode, eTargetRef, fTargetPos1, fTargetPos2, fTargetPos3, fTargetPos4);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - nCnt
     - unsigned short
     - -
     - Number of input task poses (1–4).
   * - nInputMode
     - unsigned short
     - -
     - Mode selector (valid only when `nCnt = 2`). |br|
       0: Z-axis defined by current tool direction  |br|
       1: Z-axis defined by X1’s Z direction
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for calculation.
   * - fTargetPos1
     - float[6]
     - -
     - Task-space pose of point #1.
   * - fTargetPos2
     - float[6]
     - -
     - Task-space pose of point #2.
   * - fTargetPos3
     - float[6]
     - -
     - Task-space pose of point #3.
   * - fTargetPos4
     - float[6]
     - -
     - Task-space pose of point #4 (optional).

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_POSE <struct_ROBOT_POSE>`
     - The resulting coordinate system (origin and orientation) expressed as a pose structure.

**Example**

.. code-block:: cpp

   float pos1[6] = { 200.f, 30.f, 150.f, 0.f, 0.f, 0.f };
   float pos2[6] = { 300.f, 30.f, 150.f, 0.f, 0.f, 0.f };
   float pos3[6] = { 300.f, 80.f, 150.f, 0.f, 0.f, 45.f };
   float pos4[6] = { 200.f, 80.f, 150.f, 0.f, 0.f, 0.f };

   LPROBOT_POSE new_user = drfl.calc_coord(
       4,                     // use 4 points
       0,                     // mode 0
       COORDINATE_SYSTEM_BASE,
       pos1, pos2, pos3, pos4
   );

   for (int i = 0; i < NUM_TASK; ++i)
       std::cout << new_user->_fPosition[i] << std::endl;

This example calculates a new coordinate system using **four task-space poses**,  
returns the result in `new_user`, and prints the calculated origin and axes.  
Commonly used to define **User Frames** or perform **3-point plane calibration**.
