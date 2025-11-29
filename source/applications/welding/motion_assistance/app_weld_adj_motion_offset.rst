.. _app_weld_adj_motion_offset:

app_weld_adj_motion_offset
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1051)

.. code-block:: cpp

    bool app_weld_adj_motion_offset(float fOffsetY, float fOffsetZ)
    {
        return _app_weld_adj_motion_offset(_rbtCtrl, fOffsetY, fOffsetZ);
    };

**Features**

This function applies **Y-axis** and **Z-axis offsets** to the robot’s current motion path.  
It is used to dynamically adjust the welding trajectory in real time to account for alignment errors,  
fixture tolerances, or surface variations during the welding process.

These offsets can be applied while the robot is executing a welding path, allowing for smooth and  
adaptive motion correction without stopping the ongoing operation.

**Arguments**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Field**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fOffsetY
     - float
     - -
     - Y-axis offset (mm). |br|
       Positive values shift the welding torch along the positive Y-direction.
   * - fOffsetZ
     - float
     - -
     - Z-axis offset (mm). |br|
       Positive values raise the torch vertically upward relative to the workpiece.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failure (offset adjustment could not be applied.)
   * - 1
     - Success (motion offset successfully updated.)

**Example**

.. code-block:: cpp

    // Example: Apply motion offset to correct welding torch position
    float fOffsetY = 2.0f;  // Y Offset in mm
    float fOffsetZ = 3.0f;  // Z Offset in mm

    // Apply Y and Z motion offsets during welding
    bool result = Drfl.app_weld_adj_motion_offset(fOffsetY, fOffsetZ);

    if (result)
        std::cout << "Motion offset applied successfully: Y=" << fOffsetY << " mm, Z=" << fOffsetZ << " mm." << std::endl;
    else
        std::cout << "Failed to apply motion offset." << std::endl;

In this example, the welding path is dynamically adjusted by **+2 mm in Y** and **+3 mm in Z**,  
allowing the robot to compensate for minor misalignments or part height variations in real-time.
