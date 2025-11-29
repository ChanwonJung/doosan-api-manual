.. _del_tcp:

del_tcp
------------------------------------------
This function deletes a **previously registered TCP (Tool Center Point)** entry from the robot controller.  
Only TCPs that were manually added (via :ref:`add_tcp <add_tcp>`) can be deleted.  
Once removed, the TCP will no longer be available for selection until it is re-registered.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 900)

.. code-block:: cpp

    bool del_tcp(string strSymbol) {
        return _del_tcp(_rbtCtrl, strSymbol.c_str());
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
     - The name of the TCP to delete.  |br|
       Must correspond to an existing TCP previously registered in the controller.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error — failed to delete TCP
   * - 1
     - Success — TCP deletion completed successfully

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float fTCP[6] = {10.f, 10.f, 10.f, 0.f, 0.f, 0.f};

       // (1) Register a new TCP
       drfl.add_tcp("tcp#1", fTCP);

       // (2) Set it as the active TCP
       drfl.set_tcp("tcp#1");

       // (3) Delete the registered TCP
       drfl.del_tcp("tcp#1");
   }

This example demonstrates how to register a new TCP, activate it,  
and then remove it from the controller’s registry when it is no longer needed.
