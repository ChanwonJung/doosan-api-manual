.. _constants_robot_configuration:

2.1.2 Robot Configuration Constants
----------------------------------------

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - **Name**
     - **Value**
     - **Description**
   * - NUM_JOINT
     - 6
     - Number of joints of the robot. Used for joint-space arrays.
   * - NUMBER_OF_JOINT
     - 6
     - Alias of ``NUM_JOINT``. Provided for backward compatibility.
   * - NUM_TASK
     - 6
     - Number of task-space components (X, Y, Z, Rx, Ry, Rz).
   * - NUMBER_OF_TASK
     - 6
     - Alias of ``NUM_TASK``. Provided for backward compatibility.
   * - NUMBER_OF_TASK_EX
     - NUMBER_OF_TASK + 1
     - Extended task size including additional orientation type support.
   * - NUMBER_OF_ITER_THRESHOULD
     - 2
     - Number of iteration-threshold parameters used in extended inverse kinematics.
   * - NUM_AXIS
     - NUMBER_OF_JOINT
     - Alias for the number of axes, equal to the number of joints.
   * - NUM_FLANGE_IO
     - 6
     - Number of I/O channels available on the flange.
   * - NUM_BUTTON
     - 5
     - Number of standard buttons defined on the device.
   * - NUM_BUTTON_EX
     - 6
     - Extended number of buttons for newer hardware.
   * - NUMBER_OF_BUTTON
     - 6
     - Alias representing the total number of buttons.