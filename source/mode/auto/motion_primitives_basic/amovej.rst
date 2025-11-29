.. _auto_amovej:

amovej (Auto Mode)
------------------------------------------

As an asynchronous **movej**, this function operates the same as the :ref:`movej <auto_movej>` function  
except for not having the ``fBlendingRadius`` argument for blending.  
Due to its asynchronous nature, the command **returns immediately after motion starts**,  
allowing the next line of code to execute **without waiting** for the motion to complete.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 773)

.. code-block:: cpp

   bool amovej(float fTargetPos[NUM_JOINT],
               float fTargetVel,
               float fTargetAcc,
               float fTargetTime = 0.f,
               MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
               BLENDING_SPEED_TYPE eBlendingType = BLENDING_SPEED_TYPE_DUPLICATE) {
       return _amovej(_rbtCtrl, fTargetPos, fTargetVel, fTargetAcc,
                      fTargetTime, eMoveMode, eBlendingType);
   };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[6]
     - -
     - Target joint location for six axes
   * - fTargetVel
     - float
     - -
     - Velocity
   * - fTargetAcc
     - float
     - -
     - Acceleration
   * - fTargetTime
     - float
     - 0.f
     - Reach Time [sec]
   * - eMoveMode
     - :ref:`MOVE_MODE <enum_move_mode>` 
     - ``MOVE_MODE_ABSOLUTE``
     - Refer to the Definition of Enumeration Type
   * - fBlendingRadius
     - float
     - 0.f
     - Radius for blending
   * - eBlendingType
     - :ref:`BLENDING_SPEED_TYPE <enum_blending_speed_type>` 
     - ``BLENDING_SPEED_TYPE_DUPLICATE``
     - Refer to the Definition of Enumeration Type

**Note**

- When ``fTargetTime`` is specified, motion is processed based on ``fTargetTime`` while ignoring ``fTargetVel`` and ``fTargetAcc``.  
- Refer to the motion description of :ref:`movej <auto_movej>` for blending details according to ``eBlendingType`` and velocity/acceleration settings.

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

   // Example: Perform asynchronous joint-space motion sequence with mwait synchronization.
   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float q0[6] = { 0.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f };
       float q1[6] = { 90.0f, 0.0f, 90.0f, 0.0f, 90.0f, 0.0f };
       float q99[6] = { 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };
       float jvel = 10.f;   // Joint velocity [deg/s]
       float jacc = 20.f;   // Joint acceleration [deg/s²]

       // 1) Move to initial position synchronously
       drfl.movej(q0, jvel, jacc);

       // 2) Wait 3 seconds before next command
       Sleep(3000);

       // 3) Start asynchronous motion to q1 (no wait)
       drfl.amovej(q1, jvel, jacc);

       // 4) Wait for motion completion before next move
       drfl.mwait();

       // 5) Move to home position after synchronization
       drfl.movej(q99, jvel, jacc);

       return 0;
   }

This example performs an **asynchronous joint-space motion** using `amovej()`, then synchronizes with `mwait()` before continuing to the next move.  
It demonstrates how asynchronous motion allows other tasks or I/O operations to run concurrently until synchronization is explicitly called.
