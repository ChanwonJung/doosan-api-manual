.. _manual:

3.2 Manual Mode
===================================

.. figure:: /tutorials/images/mode/manual_direct_teaching.gif
   :alt: direct_teaching
   :width: 80%
   :align: center

.. raw:: html
      
   <br>

Manual Mode includes API functions that allow users to directly manipulate the robot  
or interact with it through physical input devices. |br|
When the robot is in Manual (Teach) Mode, the LED at the robot's end displays a blue color. |br|
These functions are typically used together with the following interaction methods.

**Teach Pendant-Based Operation**

.. figure:: /tutorials/images/mode/manual_tp.png
   :alt: manual_tp
   :width: 80%
   :align: center

   *Source by* `DoosanRobotics Training/OnlineCourses/TP <https://robotlab.doosanrobotics.com/en/Training/OnlineCourses/eb8ee59b-6fd0-e911-a812-000d3a07bbcc>`_

.. raw:: html
      
   <br>

The Teach Pendant enables various forms of direct robot manipulation, including:

- Jogging: Joint or Task-based incremental motion  
- Move: Direct movement to a target joint position or Cartesian pose  
- Coordinate Selection: Choosing the reference frame (TCP, Base, etc.)  
- Alignment & Homing: Axis alignment or moving the robot to its home position

.. figure:: /tutorials/images/mode/manual_jog.png
   :alt: jogging
   :width: 80%
   :align: center

   Jogging

.. raw:: html
      
   <br>

The following coordinate-frame-based motion example illustrates how  
precise manual adjustments can be performed in Manual Mode.

**Hand Guiding & Cockpit Control**

When the Hand Guiding button on the back of the Teach Pendant is pressed,  
the robot switches to a compliant mode, allowing the operator to physically guide  
the robot by holding the flange and moving it to the desired pose.  
This provides a highly intuitive method for adjusting the robot's position.

.. figure:: /tutorials/images/mode/cockpit.png
   :alt: manual_cockpit
   :width: 75%
   :align: center

   *Source by* `DoosanRobotics Training/OnlineCourses/Cockpit <https://robotlab.doosanrobotics.com/en/Training/OnlineCourses/eb8ee59b-6fd0-e911-a812-000d3a07bbcc>`_

.. raw:: html
      
   <br>

The Cockpit interface on top of the robot flange also allows manual control, including  
jogging, position adjustments, and orientation commands directly from the robot arm.

For a detailed guide on Manual Mode, refer to the link below: |br|
`Manual Mode Training Course <https://robotlab.doosanrobotics.com/en/Training/OnlineCourses/eb8ee59b-6fd0-e911-a812-000d3a07bbcc>`_

.. toctree::
   :maxdepth: 1

   jogging_motion_control/jogging_motion_control
   coordinate_teaching/coordinate_teaching
   io_communication_feedback/io_communication_feedback
   safety_servo_operations/safety_servo_operations
   force_control_compliance_tuning/force_control_compliance_tuning
   tp_interaction/tp_interaction
   tp_logging_lifecycle/tp_logging_lifecycle
   watch_variables/watch_variables