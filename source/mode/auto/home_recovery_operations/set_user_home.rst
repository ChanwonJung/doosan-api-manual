.. _auto_set_user_home:

set_user_home (Auto Mode)
------------------------------------------
This section explains how to use :ref:`set_user_home <set_user_home>`  
during **Auto (Run)** operations to store the robot’s **current pose**  
as the **user-defined home position**.

Once saved, this custom home can be recalled later using  
:ref:`move_home <auto_move_home>` with the ``MOVE_HOME_USER`` mode,  
making it useful for user-specific startup poses, calibration points,  
or safe retreat locations.

**Typical usage**

- Define a custom home position for automated tasks or workstation setups.  
- Set a repeatable reference pose after manual teaching or calibration.  
- Establish a safe “return to base” location for task completion.  
- Reconfigure the user home dynamically depending on product type or jig position.  

.. Note::

   - The stored home position persists in controller memory  
     until overwritten or reset.  
   - No parameters are required; the function stores the **current robot TCP pose**.  

**Example: Saving the Current Pose as the User Home and Returning to It**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Save the robot's current TCP pose as the user home
       if (!drfl.set_user_home()) {
           printf("Failed to set user home.\n");
           return -1;
       }

       printf("User home position saved.\n");

       // 2) Move to the newly saved user home position
       if (!drfl.move_home(MOVE_HOME_USER, 1)) {
           printf("Failed to move to user home position.\n");
           return -1;
       }

       printf("Robot is moving to user home.\n");
       return 0;
   }

In this example, the robot stores its current pose as the **user-defined home**,  
then immediately executes a motion to return to that pose using ``MOVE_HOME_USER``.

**Tips**

- Useful for creating custom approach or retreat positions tailored to each task.  
- Ideal when multiple operators or workflows require different home poses.  
- Combine with :ref:`get_user_home <auto_get_user_home>` to verify the stored pose.  
- Save the user home after calibration or jig alignment to maintain consistency across runs.  
