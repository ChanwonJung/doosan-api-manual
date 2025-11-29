.. _set_user_home:

set_user_home
------------------------------------------
This function sets the **user-defined home position** of the robot in the controller.  
Once set, this position can be used as a target for homing operations through  
:ref:`move_home <move_home>` using the parameter ``MOVE_HOME_USER``.

It is useful when defining a **custom initial pose** for safe startup, calibration,  
or workspace entry sequences distinct from the factory home position.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 907)

.. code-block:: cpp

    bool set_user_home() {
        return _set_user_home(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to set user home position
   * - 1
     - Success — user home position successfully stored in controller

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // (1) Define current position as the user home
       drfl.set_user_home();

       // (2) Move robot to the user-defined home position
       drfl.move_home(MOVE_HOME_USER, (unsigned char)1);
   }

In this example, the current robot pose is saved as the user home position.  
The robot then executes a motion command to return to that stored pose  
using the `MOVE_HOME_USER` flag during the homing sequence.
