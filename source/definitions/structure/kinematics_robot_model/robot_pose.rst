.. _struct_ROBOT_POSE:

ROBOT_POSE
==========

This is a structure for expressing the **current location information** of the robot,  
mainly used in the get_current_pose() command of the robot controller.  
It contains six elements that describe the robot’s task-space pose.

.. list-table::
   :widths: 15 28 18 8 31
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fPosition``
     - ``float[NUM_JOINT]``
     - Six float values
     - Location information: |br|
       six task-space coordinates (X, Y, Z, Rx, Ry, Rz)

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_POSE
   {
       float _fPosition[NUM_JOINT];  /* current pose: six location components (X, Y, Z, Rx, Ry, Rz) */
   } ROBOT_POSE, *LPROBOT_POSE;
