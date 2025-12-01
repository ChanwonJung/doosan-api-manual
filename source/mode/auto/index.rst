.. _auto:

3.3 Auto Mode
===================================

.. figure:: /tutorials/images/mode/auto_overview.gif
   :alt: auto_overview
   :width: 80%
   :align: center

.. raw:: html
      
   <br>

Auto Mode enables fully automated robot operation in which predefined tasks, DRL programs, and motion sequences 
run without direct user control. Programs created in Task Builder or Task Writer can be verified in 
Virtual Mode and executed on the real robot, and this mode supports preparation features such as tool-weight and weight-center measurement. |br|
If required by a risk assessment, a 3-position Enable Switch must be configured through WCM > Robot > Safety I/O and kept in the center-enable position to permit Play, Start, Resume, or Servo On actions. |br|
When the robot is in Auto Mode, the LED indicator displays a white color.

.. figure:: /tutorials/images/mode/auto_application.png
   :alt: auto_application
   :width: 65%
   :align: center

   *Source by* `DoosanRobotics Product-solutions/palletizing <https://www.doosanrobotics.com/en/product-solutions/solution/process/palletizing/>`_

.. raw:: html
      
   <br>

Auto Mode is intended for executing complete program flows, while Manual Mode is limited to single-action operations such as 
jogging and restricts TCP speed to 250 mm/s for safety. Because high-speed commands like movej may trigger overspeed 
faults in Manual Mode, full-speed or continuous-trajectory motions must be executed in Auto Mode.

.. toctree::
   :maxdepth: 1

   drl_program_control/drl_program_control
   motion_primitives_basic/motion_primitives_basic
   motion_primitives_advanced/motion_primitives_advanced
   motion_control_utilities/motion_control_utilities
   home_recovery_operations/home_recovery_operations
   force_compliance/force_compliance
   velocity_servo/velocity_servo
   tool_tcp_payload/tool_tcp_payload
   gpio_modbus_flange/gpio_modbus_flange