.. _mwait:

mwait
------------------------------------------
This is a function for waiting for the termination of the motion of the preceding motion command in the robot controller. If an asynchronous motion command is combined with this function, it can execute the same motion as a synchronous command.

**Definition** |br|  
``DRFLEx.h`` within class `CDRFLEx`, public section (line 768)

.. code-block:: cpp

    bool mwait() { return _mwait(_rbtCtrl); };

**Parameter** |br|  
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error occurred while waiting for motion completion.
   * - 1
     - Successfully waited until the preceding motion command finished.

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Define target joint position
        float point[NUM_JOINT] = {30, 30, 30, 30, 30, 30};

        // Execute asynchronous motion command
        Drfl.movej(point, 60, 120);

        // Wait for the motion to complete before proceeding
        Drfl.mwait();

        return 0;
    }

This example demonstrates how to **synchronize** an asynchronous motion command using ``mwait()``.  
The function pauses program execution until the robot finishes the current motion.
