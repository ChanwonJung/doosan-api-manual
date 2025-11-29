.. _stop:

stop
------------------------------------------
This function stops the active motion in the robot controller.  
The stopping behavior depends on the ``eStopType`` parameter (e.g., quick, slow).  
All stop types except **E-Stop** are applied only to the currently active motion segment.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 762)

.. code-block:: cpp

    bool stop(STOP_TYPE eStopType = STOP_TYPE_QUICK) { return _stop(_rbtCtrl, eStopType); };

**Parameter** |br|

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eStopType
     - :ref:`STOP_TYPE <enum_STOP_TYPE>`
     - STOP_TYPE_QUICK
     - Type of stop to perform. |br|
       Options include quick, soft, or hold stop. 

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error occurred while attempting to stop motion.
   * - 1
     - Successfully stopped the current motion.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx Drfl;

       // Define a Cartesian target position
       float x1[NUM_TASK] = {784, 543, 970, 0, 180, 0};

       // Move the robot to the target position
       Drfl.movej(x1, 200, 200);

       // Wait for 2 seconds while the robot is moving
       std::this_thread::sleep_for(std::chrono::seconds(2));

       // Perform a soft stop on the current motion
       Drfl.stop(STOP_TYPE_SLOW);

       return 0;
   }

This example demonstrates how to **stop an ongoing motion smoothly**.  
The robot starts moving to a defined position and, after 2 seconds,  
the motion is halted using a **soft stop (STOP_TYPE_SLOW)** for gradual deceleration.

