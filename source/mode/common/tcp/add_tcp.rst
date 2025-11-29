.. _add_tcp:

add_tcp
------------------------------------------
This function registers a new **TCP (Tool Center Point)** configuration in the robot controller memory.  
Each TCP defines a specific position and orientation of the tool’s reference point relative to the flange.  
Registered TCPs can later be activated with :ref:`set_tcp <set_tcp>`.  

Note that the TCP registration is stored in **volatile memory**,  
meaning it is cleared upon reboot unless registered via the Teach Pendant initialization process.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 898)

.. code-block:: cpp

    bool add_tcp(string strSymbol, float fPosition[NUM_TASK]) {
        return _add_tcp(_rbtCtrl, strSymbol.c_str(), fPosition);
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
     - Name of the TCP to register. |br| 
       Must be unique and stored in the controller’s TCP list.
   * - fPosition
     - float[6]
     - -
     - TCP pose data (X, Y, Z, Rx, Ry, Rz) defining the TCP position and orientation  |br|
       relative to the robot flange coordinate frame.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to register the TCP 
   * - 1
     - Success — TCP registration completed successfully


**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float fTCP[6] = {10.f, 10.f, 10.f, 0.f, 0.f, 0.f};

       // (1) Register a new TCP named "tcp#1"
       drfl.add_tcp("tcp#1", fTCP);

       // (2) Set it as the currently active TCP
       drfl.set_tcp("tcp#1");

       // (3) Delete the registered TCP
       drfl.del_tcp("tcp#1");
   }

This example demonstrates how to register a new TCP position,  
activate it for motion commands, and then remove it from the controller’s TCP registry.
