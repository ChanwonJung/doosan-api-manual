.. _servoj:

servoj (Auto Mode)
------------------------------------------
The command is the asynchronous motion command, and the next command is executed at the same time the motion begins. 
When the mode is set to Override mode, it follows the most recent target joint position in a motion within the 
maximum speed and acceleration among the continuously delivered commands. 
When the mode is set to Queue mode, it can store up to 100 previous commands and sequentially follow the 
path. When 100 waypoints have been stored in Queue mode, the command will not return until reaching the next waypoint. 
If an Override command is input during Queue mode, it ignores the previously stored waypoints and follows the most recent target joint position.

Also, this API works in **Auto (Run) mode only**. It does **not** operate in **Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 812)

.. code-block:: cpp

   bool servoj(float fTargetPos[NUM_JOINT],
               float fLimitVel[NUM_JOINT],
               float fLimitAcc[NUM_JOINT],
               float fTargetTime = 0.f,
               DR_SERVOJ_TYPE eTargetMod = DR_SERVO_QUEUE)
   {
       return _servoj(_rbtCtrl, fTargetPos, fLimitVel, fLimitAcc, fTargetTime, eTargetMod);
   }

**Parameter**

.. list-table::
   :widths: 22 18 18 42
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[6]
     - -
     - Target **joint** position for six axes [deg or rad per system setting].
   * - fLimitVel
     - float[6]
     - -
     - Per-axis **velocity limit** applied to this command.
   * - fLimitAcc
     - float[6]
     - -
     - Per-axis **acceleration limit** applied to this command.
   * - fTargetTime
     - float
     - 0
     - Desired motion time [sec] for the segment (see **Notes**).
   * - eTargetMod
     - ``DR_SERVOJ_TYPE``
     - ``DR_SERVO_QUEUE``
     - Waypoint execution mode: |br|
       ``DR_SERVO_OVERRIDE``: Follow the **most recent** command (override previous). |br|
       ``DR_SERVO_QUEUE``: **Queue** waypoints (keep and execute in order).

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
       // Preconditions: Connected, servo ON, **Auto mode** active

       // Target joint pose and limits
       float q[6]    = { 0.f, 0.f, 90.f, 0.f, 0.f, 0.f };
       float jvel[6] = { 10.f, 10.f, 10.f, 10.f, 10.f, 10.f };
       float jacc[6] = { 10.f, 10.f, 10.f, 10.f, 10.f, 10.f };

       // Override: keep following the most recent target
       drfl.servoj(q, jvel, jacc, 0.02f, DR_SERVO_OVERRIDE);

       // Queue example (buffer waypoints)
       // drfl.servoj(q, jvel, jacc, 0.02f, DR_SERVO_QUEUE);

       return 0;
   }

.. Note::

  - If ``fTargetTime`` cannot be satisfied due to **max velocity/acceleration** limits, the controller **automatically adjusts** the timing and may display a notification.  
  - Not linked to the operation speed adjustment of ``change_operation_speed`` (no coupling with that setting).  
  - Up to **100 waypoints** can be stored in **Queue** mode; an **Override** call during Queue mode clears the buffered path and follows the latest command.
