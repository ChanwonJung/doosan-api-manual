.. _auto_amoveb:

amoveb (Auto Mode)
------------------------------------------

As an asynchronous **moveb**, this function operates the same as the :ref:`moveb <auto_moveb>` function  
except for the **asynchronous process**, and executes the next line immediately after motion starts  
without waiting for its termination.  

A new motion command generated before the current asynchronous motion ends (for example, terminated by ``amovesj()``)  
may cause an error for safety reasons. Therefore, the **termination of the amoveb()** motion must be confirmed  
using the ``mwait()`` function between ``amoveb()`` and the next motion command before the new motion is executed.  

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 788)

.. code-block:: cpp

   bool amoveb(MOVE_POSB tTargetPos[MAX_MOVEB_POINT],
               unsigned char nPosCount,
               float fTargetVel[2],
               float fTargetAcc[2],
               float fTargetTime = 0.f,
               MOVE_MODE eMoveMode = MOVE_MODE_ABSOLUTE,
               MOVE_REFERENCE eMoveReference = MOVE_REFERENCE_BASE,
               DR_MV_APP eAppType = DR_MV_APP_NONE) {
       return _amoveb(_rbtCtrl, tTargetPos, nPosCount, fTargetVel, fTargetAcc,
                      fTargetTime, eMoveMode, eMoveReference, eAppType);
   };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - tTargetPos
     - :ref:`MOVE_POSB <struct_MOVE_POSB>` [MAX_MOVEB_POINT]
     - -
     - Maximum 25 path information
   * - nPosCount
     - unsigned char
     - -
     - Number of valid paths
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

.. Note::

  - When ``fTargetTime`` is specified, motion is processed based on ``fTargetTime`` while ignoring ``fTargetVel``.  
  - When ``eMoveMode`` is ``MOVE_MODE_RELATIVE``, each position in ``tTargetPos`` is defined as a **relative coordinate** for the preceding path.  
  - This function does **not** support online blending of previous and subsequent motions.

.. Caution::

  - A user input error occurs if the blending radius in ``tTargetPos`` is 0.  
  - A user input error occurs when duplicated ``Line`` segments are defined in the same direction.  
  - If blending conditions cause rapid directional change, a user input error is generated to prevent sudden acceleration.  
  - This function does **not** support online blending of previous and subsequent motions.

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

   // Example: Execute an asynchronous multi-segment motion with blending.
   // Digital output 1 turns ON 3 seconds after motion starts.
   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       MOVE_POSB xb[4];
       memset(xb, 0, sizeof(xb));
       int seqNum = 4;
       float tVel[2] = { 50, 50 };   // Linear / Angular Velocity
       float tAcc[2] = { 100, 100 }; // Linear / Angular Acceleration

       xb[0]._blendType = 0;  // Line
       xb[0]._fBlendRad = 50;
       xb[0]._fTargetPos[0] = 559;
       xb[0]._fTargetPos[1] = 234.5;
       xb[0]._fTargetPos[2] = 651.5;
       xb[0]._fTargetPos[3] = 0;
       xb[0]._fTargetPos[4] = 180;
       xb[0]._fTargetPos[5] = 0;

       xb[1]._blendType = 1;  // Circle
       xb[1]._fBlendRad = 50;
       xb[1]._fTargetPos[0] = 559;
       xb[1]._fTargetPos[1] = 234.5;
       xb[1]._fTargetPos[2] = 651.5;
       xb[1]._fTargetPos[3] = 0;
       xb[1]._fTargetPos[4] = 180;
       xb[1]._fTargetPos[5] = 0;

       xb[2]._blendType = 0;  // Line
       xb[2]._fBlendRad = 50;
       xb[2]._fTargetPos[0] = 559;
       xb[2]._fTargetPos[1] = 434.5;
       xb[2]._fTargetPos[2] = 451.5;
       xb[2]._fTargetPos[3] = 0;
       xb[2]._fTargetPos[4] = 180;
       xb[2]._fTargetPos[5] = 0;

       xb[3]._blendType = 0;  // Line
       xb[3]._fBlendRad = 50;
       xb[3]._fTargetPos[0] = 559;
       xb[3]._fTargetPos[1] = 234.5;
       xb[3]._fTargetPos[2] = 451.5;
       xb[3]._fTargetPos[3] = 0;
       xb[3]._fTargetPos[4] = 180;
       xb[3]._fTargetPos[5] = 0;

       // Execute asynchronous motion
       drfl.amoveb(xb, seqNum, tVel, tAcc);

       // Trigger output after 3 seconds
       Sleep(3000);
       drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_1, 1);

       return 0;
   }

This example performs an **asynchronous blended multi-segment motion** composed of lines and circular paths.  
After motion begins, digital output 1 is turned on after 3 seconds while the robot continues its movement.
