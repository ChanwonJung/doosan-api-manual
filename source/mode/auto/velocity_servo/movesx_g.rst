.. _movesx_g:

movesx_g (Auto Mode)
------------------------------------------
This function executes **Cartesian spline motion** through multiple TCP waypoints,  
enabling smooth and continuous trajectory generation in Cartesian space.

Also, this API operates only in **Auto (Run) mode**. It is **not available in Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 821)

.. code-block:: cpp

   bool movesx_g(float fTargetPos[MAX_SPLINE_POINT][NUM_TASK],
                 unsigned char nPosCount,
                 float fTargetVel[2],
                 float fTargetAcc[2],
                 float fTargetTime = 0.f,
                 MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
                 MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_BASE,
                 SPLINE_VELOCITY_OPTION eVelOpt = SPLINE_VELOCITY_OPTION_DEFAULT)
   {
       return _movesx_g(_rbtCtrl, fTargetPos, nPosCount, fTargetVel, fTargetAcc, fTargetTime, eMoveMode, eMoveReference, eVelOpt);
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
     - List of Cartesian waypoints [X, Y, Z, Rx, Ry, Rz].
   * - nPosCount
     - unsigned char
     - -
     - Number of waypoints (max = MAX_SPLINE_POINT).
   * - fTargetVel
     - float[2]
     - -
     - Translational and rotational velocity limits.
   * - fTargetAcc
     - float[2]
     - -
     - Translational and rotational acceleration limits.
   * - fTargetTime
     - float
     - 0.0f
     - Total spline motion duration [sec].
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>`
     - ``MOVE_MODE_ABSOLUTE``
     - Defines movement mode (absolute/relative).
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>`
     - ``MOVE_REFERENCE_BASE``
     - Reference coordinate system.
   * - eVelOpt
     - :ref:`SPLINE_VELOCITY_OPTION <enum_spline_velocity_option>`
     - ``SPLINE_VELOCITY_OPTION_DEFAULT``
     - Defines velocity blending strategy for spline motion.

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

       // Define Cartesian spline path
       float path[3][6] = {
           {400.f, 100.f, 200.f, 180.f, 0.f, 0.f},
           {420.f, 120.f, 180.f, 180.f, 10.f, 0.f},
           {440.f, 140.f, 160.f, 180.f, 20.f, 0.f}
       };

       float vel[2] = {200.f, 100.f};
       float acc[2] = {300.f, 150.f};

       drfl.movesx_g(path, 3, vel, acc, 2.5f);

       return 0;
   }

.. Note::

  - ``movesx_g`` generates **smooth TCP trajectories** via spline blending between waypoints.  
  - Supports flexible control via **velocity**, **acceleration**, and **reference frame** settings.  
  - Automatically adjusts blending when physical limits are reached.  
  - Use for **precision path execution**, **contour following**, or **surface scanning** tasks.  
  - Not linked with ``force/stiffness control`` or ``change_operation_speed()`` functions.