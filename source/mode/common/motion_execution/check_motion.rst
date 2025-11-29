.. _check_motion:

check_motion
------------------------------------------
This function checks the current motion status of the robot controller.  
It is used to determine whether a motion is in progress, being calculated, or completely stopped.  
Typically, this function is called in polling loops to synchronize sequential robot commands.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 827)

.. code-block:: cpp

    int check_motion() { return _check_motion(_rbtCtrl); };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - No motion in action (idle state)
   * - 1
     - Motion being calculated (path planning or preparation stage)
   * - 2
     - Motion in operation (currently executing trajectory)

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Define two joint targets
       float q0[6]  = {0, 0, 90, 0, 90, 0};
       float q99[6] = {0, 0, 0, 0, 0, 0};

       // 1) Start first joint motion
       drfl.movej(q0, 60, 30);

       // 2) Poll motion state until completed
       while (true) {
           int state = drfl.check_motion();
           if (state == 0) {   // motion complete
               std::cout << "[check_motion] Motion finished, starting next move..." << std::endl;
               break;
           }
           else if (state == 1)
               std::cout << "[check_motion] Motion being calculated..." << std::endl;
           else if (state == 2)
               std::cout << "[check_motion] Motion in progress..." << std::endl;

           std::this_thread::sleep_for(std::chrono::milliseconds(200));
       }

       // 3) Execute next motion only after previous move completed
       drfl.movej(q99, 60, 30);

       return 0;
   }

This example demonstrates a **polling-based motion synchronization** approach using `check_motion()`. |br|
The function allows the user to verify whether a previous motion has finished before executing the next move. |br|  
A return value of **0** indicates that the motion is complete and the robot is ready for the next command.
