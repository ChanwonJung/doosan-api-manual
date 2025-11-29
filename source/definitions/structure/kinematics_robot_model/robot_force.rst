.. _struct_ROBOT_FORCE:

ROBOT_FORCE
============

This structure represents the **force and torque data** measured or estimated by the robot controller.  
It provides six-axis wrench information, including three linear forces (Fx, Fy, Fz) and three torques (Tx, Ty, Tz).

.. list-table::
   :widths: 15 28 18 8 31
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_fForce``
     - ``float[NUM_JOINT]``
     - (Fx, Fy, Fz, Tx, Ty, Tz)
     - Six-axis force and torque values in the selected reference frame.

Total size: 24 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _ROBOT_FORCE
   {
       float _fForce[NUM_JOINT];  /* current force and torque (Fx, Fy, Fz, Tx, Ty, Tz) */
   } ROBOT_FORCE, *LPROBOT_FORCE;