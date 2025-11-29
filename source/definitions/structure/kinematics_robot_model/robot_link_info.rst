.. _struct_ROBOT_LINK_INFO:

ROBOT_LINK_INFO
================

This structure defines the **Denavit–Hartenberg (DH) parameters** and installation properties  
for each of the six robot links. It describes both the geometric and orientation configuration  
of the robot, which are essential for forward/inverse kinematics and mechanical calibration.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``d[6]``
     - ``float[6]``
     - -
     - Link offset distance along Z-axis (m)
   * - 24
     - ``a[6]``
     - ``float[6]``
     - -
     - Link length along X-axis (m)
   * - 48
     - ``alpha[6]``
     - ``float[6]``
     - -
     - Twist angle between consecutive Z-axes (rad)
   * - 72
     - ``theta[6]``
     - ``float[6]``
     - -
     - Joint reference angle (mechanical reference) (rad)
   * - 96
     - ``offset[6]``
     - ``float[6]``
     - -
     - Homing offset per joint (rad)
   * - 120
     - ``gradient``
     - ``float``
     - -
     - Base installation gradient angle (deg)
   * - 124
     - ``rotation``
     - ``float``
     - -
     - Base installation rotation angle (deg)

Total size: 128 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_LINK_INFO 
   {
       float d[6];       // meter
       float a[6];       // meter
       float alpha[6];   // rad
       float theta[6];   // rad (mechanical reference)
       float offset[6];  // rad (homingOffset)
       float gradient;   // base install gradient
       float rotation;   // base install rotation    
   } ROBOT_LINK_INFO, *LPROBOT_LINK_INFO;
