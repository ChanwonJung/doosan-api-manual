.. _servoj_g:

servoj_g (Auto Mode)
------------------------------------------
This function sends an **asynchronous joint-space motion command** for continuous trajectory execution  
using **blended velocity and acceleration profiles**.  
It updates the target joint position in real time and smoothly transitions to the next motion command.  

Also, this API operates only in **Auto (Run) mode**. It is **not available in Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 818)

.. code-block:: cpp

   bool servoj_g(float fTargetPos[NUM_JOINT],
                 float fTargetVel[NUM_JOINT],
                 float fTargetAcc[NUM_JOINT],
                 float fTargetTime = 0.f)
   {
       return _servoj_g(_rbtCtrl, fTargetPos, fTargetVel, fTargetAcc, fTargetTime);
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
     - Target joint position for six axes.
   * - fTargetVel
     - float[6]
     - -
     - Joint velocity limit for each axis.
   * - fTargetAcc
     - float[6]
     - -
     - Joint acceleration limit for each axis.
   * - fTargetTime
     - float
     - 0.0f
     - Target transition time [sec]. Automatically adjusted if infeasible.

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

       float q[6] = {0.f, -30.f, 90.f, 0.f, 60.f, 0.f};
       float qvel[6] = {10.f, 10.f, 10.f, 10.f, 10.f, 10.f};
       float qacc[6] = {20.f, 20.f, 20.f, 20.f, 20.f, 20.f};

       drfl.servoj_g(q, qvel, qacc, 0.3f);

       return 0;
   }

.. Note::

  - ``servoj_g`` performs **joint interpolation with blending** for smooth transitions.  
  - If ``fTargetTime`` exceeds hardware limits, it is automatically adjusted.  
  - ``servoj_g`` is ideal for **real-time control** and **streaming-based trajectory updates**.  
  - It is **not linked** with ``force/stiffness control`` or ``change_operation_speed()``.  
  - Recommended for use in **dynamic path control**, **adaptive motion**, or **trajectory replay** applications.
