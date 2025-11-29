.. _reset_workpiece_weight:

reset_workpiece_weight
------------------------------------------
This function resets the **workpiece weight data** stored in the controller, initializing the internal algorithm used to estimate or manage payload information.  
It should be called before performing a new workpiece weight measurement to ensure accurate results.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 679)

.. code-block:: cpp

    bool reset_workpiece_weight() {
        return _reset_workpiece_weight(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed: weight reset not applied due to communication or mode restriction
   * - 1
     - Success: workpiece weight data successfully reset and ready for new measurement

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Initialize the weight measurement algorithm
       bool success = drfl.reset_workpiece_weight();

       if (success)
           printf("Workpiece weight reset successfully.\n");
       else
           printf("Failed to reset workpiece weight.\n");
   }

This example resets the current workpiece weight data before performing a new measurement,  
ensuring that the internal payload estimation algorithm starts from a clean state.
