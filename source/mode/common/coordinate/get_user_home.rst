.. _get_user_home:

get_user_home
------------------------------------------
This function retrieves the **user-defined home position** stored in the robot controller.  
The returned structure contains the Cartesian pose information (position and orientation)  
of the home position previously set using :ref:`set_user_home <set_user_home>`.

This function is often used to **verify or log** the stored home pose before executing  
a homing motion or during system initialization.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 760)

.. code-block:: cpp

    LPROBOT_POSE get_user_home() {
        return _get_user_home(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_POSE <struct_ROBOT_POSE>`
     - Returns a pointer to the user-defined home position data structure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // (1) Retrieve the stored user home pose
       LPROBOT_POSE pHome = drfl.get_user_home();

       // (2) Print the position and orientation of the user home
       printf("User Home Position [mm]: X=%.2f, Y=%.2f, Z=%.2f\n", pHome->_fX, pHome->_fY, pHome->_fZ);
       printf("User Home Orientation [deg]: Rx=%.2f, Ry=%.2f, Rz=%.2f\n", pHome->_fA, pHome->_fB, pHome->_fC);
   }

This example retrieves the robot’s user-defined home pose and  
prints its Cartesian position and orientation values for verification or debugging.
