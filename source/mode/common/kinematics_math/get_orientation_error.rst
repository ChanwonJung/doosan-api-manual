.. _get_orientation_error:

get_orientation_error
------------------------------------------
This function calculates the **orientation error value** between two arbitrary task-space poses  
(`fPosition1` and `fPosition2`) around the specified task axis (`eTaskAxis`).  
It is useful for verifying angular deviation or alignment errors between tool orientations.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 676)

.. code-block:: cpp

    float get_orientation_error(
        float fPosition1[NUM_TASK],
        float fPosition2[NUM_TASK],
        TASK_AXIS eTaskAxis
    ) {
        return _get_orientation_error(_rbtCtrl, fPosition1, fPosition2, eTaskAxis);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fPosition1
     - float[6]
     - -
     - First task-space position (x, y, z, Rx, Ry, Rz) used as reference orientation.
   * - fPosition2
     - float[6]
     - -
     - Second task-space position to compare against the reference.
   * - eTaskAxis
     - :ref:`TASK_AXIS <enum_task_axis>` 
     - -
     - Axis about which the orientation error is calculated.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - float
     - Orientation error value (in degrees or radians depending on system configuration).

**Example**

.. code-block:: cpp

   float x1[6] = { 0.f, 0.f, 0.f, 0.f, 0.f, 0.f };
   float x2[6] = { 10.f, 20.f, 30.f, 40.f, 50.f, 60.f };

   float diff = drfl.get_orientation_error(x1, x2, TASK_AXIS_X);
   std::cout << "Orientation error around X-axis: " << diff << std::endl;

This example computes the **rotation error** between two tool poses `x1` and `x2`  
around the **X-axis**, returning the angular difference.  
Such calculation is often used in calibration, pose correction, or alignment inspection.
