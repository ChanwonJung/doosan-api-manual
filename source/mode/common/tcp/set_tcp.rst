.. _set_tcp:

set_tcp
------------------------------------------
This function sets the **currently active TCP (Tool Center Point)** among the TCP configurations  
that have been pre-registered in the robot controller.  
If an empty string is passed, the TCP information is cleared and reset to default.  
This ensures that motion and coordinate calculations use the correct reference point  
for the attached end-effector or tool.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 894)

.. code-block:: cpp

    bool set_tcp(string strSymbol) {
        return _set_tcp(_rbtCtrl, strSymbol.c_str());
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strSymbol
     - string
     - -
     - Name of the TCP to activate.  |br|
       Must correspond to a TCP entry previously registered in the controller. |br| 
       If an empty string `""` is passed, the active TCP is cleared.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to activate the TCP 
   * - 1
     - Success — the TCP was successfully set as active

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // (1) Set the TCP named "tcp#1"
       drfl.set_tcp("tcp#1");

       // (2) Move using the selected TCP reference
       float point[6] = {756.6f, 511.6f, 876.6f, 44.5f, 86.7f, 55.7f};
       float vel[2]   = {30.f, 0.f};
       float acc[2]   = {30.f, 0.f};

       drfl.movej(point, vel, acc);
   }

This example selects the TCP named `"tcp#1"` and performs a joint-space motion  
using that TCP as the reference frame for all position and orientation calculations.
