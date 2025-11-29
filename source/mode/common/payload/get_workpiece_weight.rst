.. _get_workpiece_weight:

get_workpiece_weight
------------------------------------------
This function measures and returns the **current workpiece weight** that has been set or detected by the robot controller.  
The returned value represents the workpiece component of the total payload (excluding tool weight).

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 678)

.. code-block:: cpp

    float get_workpiece_weight() {
        return _get_workpiece_weight(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - float
     - Measured workpiece weight in kilograms (kg).

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Retrieve the current workpiece weight
       float weight = drfl.get_workpiece_weight();

       // Print the measured weight value
       printf("Current workpiece weight: %.3f kg\n", weight);
   }

This example retrieves the currently measured or configured workpiece weight  
and prints the value to the console for verification or monitoring.
