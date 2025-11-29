.. _servol_g:

servol_g (Auto Mode)
------------------------------------------
This function performs **asynchronous Cartesian interpolation** using velocity and acceleration blending,  
enabling smooth, continuous TCP (Tool Center Point) motion.  
It updates position targets in real time while maintaining the specified kinematic constraints.  

Also, this API operates only in **Auto (Run) mode**. It is **not available in Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 819)

.. code-block:: cpp

   bool servol_g(float fTargetPos[NUM_TASK],
                 float fTargetVel[2],
                 float fTargetAcc[2],
                 float fTargetTime = 0.f)
   {
       return _servol_g(_rbtCtrl, fTargetPos, fTargetVel, fTargetAcc, fTargetTime);
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
     - float[6]
     - -
     - Target Cartesian pose [X, Y, Z, Rx, Ry, Rz].
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
     - Transition time [sec]. Automatically adjusted as needed.

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
       // Preconditions: Connected, servo ON, Auto mode active

       float tcp[6] = {400.f, 200.f, 300.f, 180.f, 0.f, 0.f};
       float vel[2] = {100.f, 50.f};
       float acc[2] = {200.f, 100.f};

       drfl.servol_g(tcp, vel, acc, 0.4f);

       return 0;
   }

.. Note::

  - ``servol_g`` provides **continuous TCP motion** with velocity/acceleration blending.  
  - Ideal for **path streaming**, **sensor-based control**, and **hybrid trajectory updates**.  
  - If ``fTargetTime`` cannot be met, motion parameters are internally optimized.  
  - It is not linked with ``change_operation_speed()`` or ``force/stiffness control`` APIs.  
  - Use for **smooth Cartesian trajectory generation** and **real-time feedback control**.
