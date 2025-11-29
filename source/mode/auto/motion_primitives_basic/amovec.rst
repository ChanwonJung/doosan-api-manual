.. _auto_amovec:

amovec (Auto Mode)
------------------------------------------

As an asynchronous **movec**, it operates the same as :ref:`movec <auto_movec>` except for not having
the ``fBlendingRadius`` argument for blending. However, due to the asynchronous type, the command
**returns immediately when motion starts** and executes the next line **without waiting** for
termination.  

This function is available **only when ``DRCF_VERSION == 2``**. (It is not supported in version 3 or later.)

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 781)

.. code-block:: cpp

   bool amovec(float fTargetPos[2][NUM_TASK],
               float fTargetVel[2],
               float fTargetAcc[2],
               float fTargetTime = 0.f,
               MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
               MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_BASE,
               float fTargetAngle1 = 0.f,
               float fTargetAngle2 = 0.f,
               BLENDING_SPEED_TYPE eBlendingType = BLENDING_SPEED_TYPE_DUPLICATE,
               MOVE_ORIENTATION eOrientation = DR_MV_ORI_TEACH,
               DR_MV_APP eAppType = DR_MV_APP_NONE) {
       return _amovec_ex(_rbtCtrl, fTargetPos, fTargetVel, fTargetAcc, fTargetTime,
                         eMoveMode, eMoveReference, fTargetAngle1, fTargetAngle2,
                         eBlendingType, eOrientation, eAppType);
   };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos[0]
     - float[6]
     - -
     - Waypoint
   * - fTargetPos[1]
     - float[6]
     - -
     - Target location
   * - fTargetVel
     - float[2]
     - -
     - Linear Velocity, Angular Velocity
   * - fTargetAcc
     - float[2]
     - -
     - Linear Acceleration, Angular Acceleration
   * - fTargetTime
     - float
     - 0.f
     - Reach Time [sec]
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Refer to the Definition of Enumeration Type
   * - eMoveReference
     - :ref:`MOVE_REFERENCE <enum_move_reference>` 
     - ``MOVE_REFERENCE_BASE``
     - Refer to the Definition of Enumeration Type
   * - fTargetAngle1
     - float
     - 0.f
     - angle1
   * - fTargetAngle2
     - float
     - 0.f
     - angle2
   * - eBlendingType
     - :ref:`BLENDING_SPEED_TYPE <enum_blending_speed_type>` 
     - ``BLENDING_SPEED_TYPE_DUPLICATE``
     - Refer to the Definition of Enumeration Type
   * - eOrientation
     - :ref:`MOVE_ORIENTATION <enum_move_orientation>`
     - ``DR_MV_ORI_TEACH``
     - Orientation control option of the tool (teached / fixed / etc.)
   * - eAppType
     - :ref:`DR_MV_APP <enum_dr_mv_app>` 
     - ``DR_MV_APP_NONE``
     - Application hint for motion (if supported by controller)

.. Note::

  - If an argument is input to ``fTargetVel`` (e.g., ``{30, 0}``), the input corresponds to the **linear velocity**
    of the motion, while the **angular velocity** is determined **proportionally** to the linear velocity.
  - If an argument is input to ``fTargetAcc`` (e.g., ``{60, 0}``), the input corresponds to the **linear acceleration**
    of the motion, while the **angular acceleration** is determined **proportionally** to the linear acceleration.
  - If ``fTargetTime`` is specified, values are processed based on ``fTargetTime``, **ignoring** ``fTargetVel`` and ``fTargetAcc``.
  - If ``eMoveMode`` is ``MOVE_MODE_RELATIVE``, ``fTargetPos[0]`` and ``fTargetPos[1]`` are defined in the **relative**
    coordinate system of the previous position. (``fTargetPos[0]`` is the relative coordinate from the starting point,
    while ``fTargetPos[1]`` is the relative coordinate from ``fTargetPos[0]``.)
  - If ``fTargetAngle1`` is more than 0 and ``fTargetAngle2`` is 0, the **total rotated angle** on the circular path
    is applied to ``fTargetAngle1``.
  - When both ``fTargetAngle1`` and ``fTargetAngle2`` are specified (>0), ``fTargetAngle1`` refers to the **total rotating angle moving at a constant velocity** on the circular path, while ``fTargetAngle2`` refers to the **rotating angle in the accel/decel section**. In that case, the total moving angle is ``fTargetAngle1 + 2 × fTargetAngle2`` along the circular path.
  - Refer to the motion description of :ref:`moveb <auto_moveb>` for **blending** according to option ``eBlendingType`` and ``fTargetVel / fTargetAcc``.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

   // Example: Draw a clockwise circular arc through two task-space points asynchronously.
   // - Digital output 1 turns ON 3 seconds after motion starts.
   // - Uses BASE frame / ABSOLUTE mode / default orientation (teach).
   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // (Preconditions) Connected, Servo ON, Auto mode, and speed limits configured.

       // 1) Define two points on the arc: waypoint (x1[0]) and target (x1[1])
       float x1[2][NUM_TASK] = {
           { 559.f, 434.5f, 651.5f, 0.f, 180.f, 0.f },  // waypoint
           { 559.f, 434.5f, 251.5f, 0.f, 180.f, 0.f }   // end target
       };

       // 2) Set linear / angular velocity & acceleration
       float tVel[2] = { 50.f, 50.f };    // 50 mm/s, 50 deg/s
       float tAcc[2] = { 100.f, 100.f };  // 100 mm/s^2, 100 deg/s^2

       // 3) Execute asynchronous circular motion
       drfl.amovec(x1, tVel, tAcc);

       // 4) Do something else immediately (no wait)
       Sleep(3000);
       drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, 1);

       // 5) Ensure synchronization before next motion
       drfl.mwait();

       return 0;
   }

This example performs an asynchronous **circular motion** through two TCP points, then turns on a digital output after 3 seconds.  
The motion does not block the program flow, so additional actions or monitoring can run concurrently.
