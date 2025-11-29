.. _coord_transform:

coord_transform
------------------------------------------
This function transforms a given task-space position (`fTargetPos`)  
from one coordinate system (`eInCoordSystem`) to another (`eOutCoordSystem`).  
It supports all valid transformation pairs among **World, Base, Tool, and User** coordinate systems.

Typical use cases include converting a pose expressed in a user-defined coordinate system  
into base coordinates for motion commands, or transforming tool TCP data into world space.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 975)

.. code-block:: cpp

    LPROBOT_POSE coord_transform(
        float fTargetPos[NUM_TASK],
        COORDINATE_SYSTEM eInCoordSystem,
        COORDINATE_SYSTEM eOutCoordSystem
    ) {
        return _coord_transform(_rbtCtrl, fTargetPos, eInCoordSystem, eOutCoordSystem);
    };

**Supported Transformations**

The following conversions are supported:

- (InCoordSystem) **world**  → (OutCoordSystem) **base**, **tool**, **user**
- (InCoordSystem) **base**   → (OutCoordSystem) **world**, **tool**, **user**
- (InCoordSystem) **tool**   → (OutCoordSystem) **world**, **base**, **user**
- (InCoordSystem) **user**   → (OutCoordSystem) **world**, **base**, **tool**

This allows flexible transformation between all combinations of reference frames.

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
     - Target task-space position to be transformed (x, y, z, Rx, Ry, Rz).
   * - eInCoordSystem
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - -
     - Source coordinate system in which `fTargetPos` is expressed.
   * - eOutCoordSystem
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - -
     - Target coordinate system to which the position will be transformed.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LPROBOT_POSE <struct_ROBOT_POSE>`
     - The transformed pose, expressed in the **output coordinate system**.

**Example**

.. code-block:: cpp

   float tcp_pose[6] = { 300.f, 100.f, 200.f, 0.f, 180.f, 90.f };

   // Transform TCP pose from BASE to USER coordinate system
   LPROBOT_POSE result = drfl.coord_transform(
       tcp_pose,
       COORDINATE_SYSTEM_BASE,
       COORDINATE_SYSTEM_USER
   );

   std::cout << "Transformed X: " << result->_fPosition[0] << std::endl;

This example converts a TCP pose originally expressed in the **base coordinate system**  
into the **user coordinate system**, and prints the transformed X-coordinate.  
This function is especially useful when calibrating user frames or performing  
motion planning relative to non-base reference systems.
