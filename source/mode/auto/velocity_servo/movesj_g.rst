.. _movesj_g:

movesj_g (Auto Mode)
------------------------------------------
This function performs **joint-space spline motion** through multiple waypoints,  
executing smooth and continuous trajectories using **spline interpolation**.  
Each waypoint is automatically blended with the next for seamless movement.

Also, this API operates only in **Auto (Run) mode**. It is **not available in Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 822)

.. code-block:: cpp

   bool movesj_g(float fTargetPos[MAX_SPLINE_POINT][NUM_JOINT],
                 unsigned char nPosCount,
                 float fTargetVel,
                 float fTargetAcc,
                 float fTargetTime = 0.f,
                 MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE)
   {
       return _movesj_g(_rbtCtrl, fTargetPos, nPosCount, fTargetVel, fTargetAcc, fTargetTime, eMoveMode);
   }

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[MAX_SPLINE_POINT][6]
     - -
     - List of joint waypoints to follow.
   * - nPosCount
     - unsigned char
     - -
     - Number of valid waypoints (max = MAX_SPLINE_POINT).
   * - fTargetVel
     - float
     - -
     - Target velocity for spline motion.
   * - fTargetAcc
     - float
     - -
     - Target acceleration for spline motion.
   * - fTargetTime
     - float
     - 0.0f
     - Motion duration [sec].
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>`
     - ``MOVE_MODE_ABSOLUTE``
     - Defines whether movement is absolute or relative.

**Return**

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed
   * - 1
     - Success

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Define spline waypoints in joint space
       float path[3][6] = {
           {0.f, -30.f, 90.f, 0.f, 60.f, 0.f},
           {10.f, -25.f, 85.f, 5.f, 65.f, 5.f},
           {20.f, -20.f, 80.f, 10.f, 70.f, 10.f}
       };

       drfl.movesj_g(path, 3, 50.f, 100.f, 2.0f);

       return 0;
   }

.. Note::

  - ``movesj_g`` provides **smooth, multi-point joint interpolation** using spline blending.  
  - Automatically adjusts blending based on velocity and acceleration limits.  
  - Ideal for **path teaching**, **motion streaming**, or **multi-point sequence execution**.  
  - Not linked with ``force/stiffness control`` or ``change_operation_speed()``.  
  - Ensure ``nPosCount`` ≤ MAX_SPLINE_POINT to avoid overflow.
