.. _get_tcp:

get_tcp
------------------------------------------
This function retrieves the **currently active TCP (Tool Center Point)** information from the robot controller.  
If no TCP is currently set, the function returns an **empty string**.  
It is useful for verifying which TCP configuration is being used before executing a motion command.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 896)

.. code-block:: cpp

    string get_tcp() {
        return string(_get_tcp(_rbtCtrl));
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - string
     - The name of the currently active TCP.  |br|
       Returns an empty string if no TCP is set.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Retrieve the currently active TCP name
       string strTCP = drfl.get_tcp();

       // If no TCP is active, set one manually
       if (strTCP.empty()) {
           drfl.set_tcp("tcp#1");
           printf("TCP was not active. Set to tcp#1.\n");
       } else {
           printf("Current TCP: %s\n", strTCP.c_str());
       }
   }

This example checks which TCP is currently active in the controller.  
If none is set, it activates `"tcp#1"` and prints the result to the console.
