.. _addto:

addto
------------------------------------------
This function returns a new joint pose by adding an offset vector (`fOffset`)  
to the given source joint position (`fSourcePos`).  
It is commonly used for small incremental movements or calibration offset computation  
in joint space.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 671)

.. code-block:: cpp

    LPROBOT_POSE addto(
        float fSourcePos[NUM_JOINT],
        float fOffset[NUM_JOINT]
    ) {
        return _addto(_rbtCtrl, fSourcePos, fOffset);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fSourcePos
     - float[6]
     - -
     - Base joint position of the robot (J1–J6).
   * - fOffset
     - float[6]
     - -
     - Offset values (ΔJ1–ΔJ6) to be added to the source position. |br|
       Units are consistent with the joint configuration (degrees or radians).

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_POSE <struct_ROBOT_POSE>`
     - Structure representing the **summed joint pose** (source + offset). 

**Example**

.. code-block:: cpp

   float q_base[6] = { 0.f, 90.f, 0.f, 90.f, 0.f, 0.f };
   float dq[6]     = { 5.f, -5.f, 0.f, 0.f, 0.f, 0.f };

   LPROBOT_POSE q_new = drfl.addto(q_base, dq);

   float q_target[6];
   for (int i = 0; i < 6; ++i)
       q_target[i] = q_new->_fPosition[i];

   drfl.movej(q_target, 50, 20);

This example adds a small offset `dq` to the base joint position `q_base`,  
resulting in a new pose `q_new`.  
The robot then moves to the updated joint configuration using `movej()`.  
This function is useful for incremental calibration, joint tuning, or small adjustment control.
