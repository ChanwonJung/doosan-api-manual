.. _servol:

servol (Auto Mode)
------------------------------------------
This function is an asynchronous type motion command and executes the next command at the same time as the motion starts. 
It is a motion that follows the most recent target position among consecutive commands within the maximum speed and acceleration.
Unlike ``servoj``, which operates in joint space, ``servol`` performs motion in **task (Cartesian) space**.

Also, this API works in **Auto (Run) mode only**. It is **not available in Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 813)

.. code-block:: cpp

   bool servol(float fTargetPos[NUM_TASK],
               float fLimitVel[2],
               float fLimitAcc[2],
               float fTargetTime)
   {
       return _servol(_rbtCtrl, fTargetPos, fLimitVel, fLimitAcc, fTargetTime);
   }

**Parameter**

.. list-table::
   :widths: 24 22 18 36
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[6]
     - -
     - Target TCP position for six axes [X, Y, Z, Rx, Ry, Rz].
   * - fLimitVel
     - float[2]
     - -
     - Translation and rotation velocity limits.
   * - fLimitAcc
     - float[2]
     - -
     - Translation and rotation acceleration limits.
   * - fTargetTime
     - float
     - -
     - Desired motion time [sec].  
       Automatically adjusted if infeasible.

**Return**

.. list-table::
   :widths: 16 84
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
       // Preconditions: Connected, servo ON, Auto mode active

       // Define Cartesian target pose
       float q0[6]   = {368.f, 34.5f, 442.f, 50.f, -180.f, 50.f};
       float jvel[2] = {10.f, 10.f};
       float jacc[2] = {20.f, 20.f};

       // Execute Cartesian motion
       drfl.servol(q0, jvel, jacc, -10000.f);

       return 0;
   }

.. Note::

  - If ``fTargetTime`` is entered but cannot be maintained due to speed or acceleration limits,  
    the controller automatically adjusts the motion time and displays a notification message.  
  - ``servol`` is **not linked** with the speed adjustment function ``change_operation_speed``.  
  - When ``DR_VAR_VEL`` (variable velocity) mode is used among singularity options,  
    it is automatically converted to ``DR_AVOID`` mode and a warning message is shown.  
  - ``servol`` is **not linked** with force/stiffness control commands.  
  - Used for smooth Cartesian interpolation and real-time target updates in automatic operation.
