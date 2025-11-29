.. _move_home:

move_home
------------------------------------------
This function aligns each axis of the robot to its home position when the robot’s axes have been twisted or offset  
due to internal or external errors in the robot controller. It restores the **mechanical home state**  
and ensures all axes are synchronized for subsequent motion commands.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 759)

.. code-block:: cpp

    bool move_home(MOVE_HOME eMode = MOVE_HOME_MECHANIC, unsigned char bRun = (unsigned)1) {
        return _move_home(_rbtCtrl, eMode, bRun);
    };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eMode
     - :ref:`MOVE_HOME <enum_move_home>`
     - MOVE_HOME_MECHANIC
     - Specifies the homing mode |br|
       Refer to the Definition of Enumeration Type
   * - bRun
     - unsigned char
     - 1
     - Motion execution flag. |br|
       0: Stop, 1:Motion (Execute homing)

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

   #include "DRFLEx.h"
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Execute homing motion to realign all axes mechanically
       drfl.move_home(MOVE_HOME_MECHANIC, (unsigned char)1);
       std::this_thread::sleep_for(std::chrono::seconds(8)); // wait during motion

       // 2) Stop homing motion prematurely if needed
       drfl.move_home(MOVE_HOME_MECHANIC, (unsigned char)0);

       // 3) Resume operation only after homing is completed and stabilized
       drfl.mwait();  // wait until homing is complete
       drfl.movej({0, -30, 90, 0, 90, 0}, 50, 50);  // start a new move

       return 0;
   }

This example demonstrates a **typical homing workflow**:  |br|
the robot performs a full mechanical alignment using `MOVE_HOME_MECHANIC`,  
optionally stops mid-process if needed, and then resumes normal motion once homing is complete. |br|  
It is recommended to call :ref:`mwait() <mwait>` or :ref:`get_robot_state() <get_robot_state>`  
after homing to confirm the motion completion and state stability.
