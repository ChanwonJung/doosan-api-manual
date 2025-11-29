.. _get_current_rotm:

get_current_rotm
------------------------------------------
This is a function to check the rotation matrix of the current tool corresponding to the input reference coordinate system (`eTargetRef`).

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 712)

.. code-block:: cpp

    float (*get_current_rotm(COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE))[3] { 
        return _get_current_rotm(_rbtCtrl, eTargetRef); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Reference coordinate system for which the rotation matrix is calculated.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - float[3][3]
     - 3×3 Rotation matrix representing the tool’s current orientation relative to the specified coordinate frame.

**Example**

.. code-block:: cpp

   float (*result)[3] = drfl.get_current_rotm();
   for (int i = 0; i < 3; i++) {
       for (int j = 0; j < 3; j++) {
           cout << result[i][j] << " ";
       }
       cout << endl;
   }

In this example, the **rotation matrix** of the tool is printed.  
Each element `result[i][j]` represents the orientation component of the tool flange  
with respect to the selected reference frame (e.g., base or tool coordinate system).  
This is especially useful for applications requiring **orientation control**,  
such as force alignment, compliance, or visual servoing.
