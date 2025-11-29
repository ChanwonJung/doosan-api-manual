.. _trans:

trans
------------------------------------------
Input parameter (`fSourcePos`) based on the ref coordinate is translated/rotated as `fOffset`  
based on the same coordinate and this function returns the result that is converted to the value  
based on the `eTargetRef`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 665)

.. code-block:: cpp

    LPROBOT_POSE trans(
        float fSourcePos[NUM_TASK],
        float fOffset[NUM_TASK],
        COORDINATE_SYSTEM eSourceRef = COORDINATE_SYSTEM_BASE,
        COORDINATE_SYSTEM eTargetRef = COORDINATE_SYSTEM_BASE
    ) {
        return _trans(_rbtCtrl, fSourcePos, fOffset, eSourceRef, eTargetRef);
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
     - Target joint or task position for six axes (x, y, z, Rx, Ry, Rz)
   * - fOffset
     - float[6]
     - -
     - Offset information for six axes (translation/rotation delta)
   * - eSourceRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Source coordinate system reference. 
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - COORDINATE_SYSTEM_BASE
     - Target coordinate system reference.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`ROBOT_POSE <struct_robot_pose>`
     - Returns the transformed position and orientation result (pose) |br|
       calculated by applying `fOffset` to `fSourcePos` and converting  |br|
       the result into the `eTargetRef` coordinate system.

**Example**

.. code-block:: cpp

   float point[6]  = { 30, 30, 30, 30, 30, 30 };
   float offset[6] = { 100, 100, 100, 100, 100, 100 };
   LPROBOT_POSE res = drfl.trans(point, offset);
   for (int i = 0; i < 6; i++)
       cout << res->_fPosition[i] << endl;

In this example, the function calculates the **translated pose** of the tool  
by applying a 100 mm translation and 100° rotation offset to the original pose.  
This function is useful for computing **relative motion targets**, such as  
incremental path planning, tool offset compensation, or dynamic coordinate conversion.
