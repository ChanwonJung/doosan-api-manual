.. _get_current_solution_space:

get_current_solution_space
------------------------------------------
This is a function for checking information on the pose of the robot in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 713)

.. code-block:: cpp

    unsigned char get_current_solution_space() { 
        return _get_current_solution_space(_rbtCtrl); 
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - unsigned char (0~7)
     - Index value indicating the current **solution space** of the robot. |br|
       This represents which joint configuration (among multiple valid inverse kinematics solutions) |br|
       the robot is currently maintaining for its end-effector position.

**Example**

.. code-block:: cpp

   unsigned char iSolutionSpace = drfl.get_current_solution_space();
   // Moves (MoveJ) if the robot maintains the current pose
   float point[6] = { 10, 10, 10, 10, 10, 10 };
   drfl.movejx(point, iSolutionSpace, 30, 30);

In this example, the function retrieves the robot’s **current solution space ID**  
and uses it as an argument for `movejx()`.  
This ensures that the robot maintains the same inverse-kinematic posture (elbow up/down, wrist flip, etc.)  
during subsequent motions.  
Solution spaces typically range from **0 to 7**, corresponding to unique robot joint configurations.
