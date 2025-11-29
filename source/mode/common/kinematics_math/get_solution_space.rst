.. _get_solution_space:

get_solution_space
------------------------------------------
This function calculates the **solution space index (0–7)** for a given joint position.  
Each solution space represents one of the eight possible robot configurations  
(elbow-up/down, wrist-flip, shoulder combinations, etc.).  
The result is primarily used when performing **inverse kinematics** via :ref:`ikin <ikin>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 673)

.. code-block:: cpp

    unsigned char get_solution_space(
        float fTargetPos[NUM_JOINT]
    ) {
        return _get_solution_space(_rbtCtrl, fTargetPos);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetPos
     - float[6]
     - -
     - Target joint positions (J1–J6). |br|
       The function evaluates these angles to determine the corresponding IK configuration space.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - unsigned char (0–7)
     - Identifier of the **solution space** that the current pose belongs to. |br| 
       Used as input to :ref:`ikin <ikin>` or :ref:`ikin_extension <ikin_extension>`.

**Example**

.. code-block:: cpp

   float q1[6] = { 0.f, 0.f, 0.f, 0.f, 0.f, 0.f };
   unsigned char sol = drfl.get_solution_space(q1);

   std::cout << "Current solution space: " << static_cast<int>(sol) << std::endl;

This example computes the solution space index for a given joint configuration `q1`.  
The returned value (`sol`) indicates one of the eight possible robot postures  
and can be used when performing inverse-kinematic operations such as `ikin()` or `ikin_ex()`.
