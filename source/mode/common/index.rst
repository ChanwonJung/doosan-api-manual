.. _common:

3.1 Common
===================================
Common Mode provides the fundamental system-level capabilities required regardless of whether the robot is in Manual or Auto mode.
General-purpose functions and shared APIs accessible across all operation modes.  

.. figure:: /tutorials/images/mode/common_overview.png
   :alt: common_overview
   :width: 80%
   :align: center

   *Source by* `DoosanRobotics Training/OnlineCourses <https://robotlab.doosanrobotics.com/en/Training/OnlineCourses/0aaa31ce-6dd0-e911-a812-000d3a07bbcc>`_

.. raw:: html
      
   <br>

These functions include system connection, mode/state monitoring, program 
execution utilities, motion execution interfaces, robot kinematics, I/O control, 
tool/TCP configuration, safety state monitoring, and various controller-level services.

.. toctree::
   :maxdepth: 1

   connection/connection
   mode_state/mode_state
   monitoring_callbacks/monitoring_callbacks
   program_drl_execution/program_drl_execution
   motion_execution/motion_execution
   position/position
   kinematics_math/kinematics_math
   velocity/velocity
   force_compliance/force_compliance
   tool/tool
   tcp/tcp
   payload/payload 
   coordinate/coordinate
   io/io 
   modbus/modbus 
   serial_flange/serial_flange
   tp/tp
   report_alarm/report_alarm 
   led/led
   safety_configuration_param/safety_configuration_param 
   safety_state_mode/safety_state_mode
   servo_power/servo_power
 