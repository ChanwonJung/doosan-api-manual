.. _get_robot_link_info:

get_robot_link_info
------------------------------------------
This function queries the controller for the robot’s **link (DH) parameters** and fills the provided
:ref:`ROBOT_LINK_INFO <struct_robot_link_info>` structure. Typical fields contain per-joint Denavit–Hartenberg
parameters (e.g., a, d, α, θ), link lengths, and auxiliary meta data used for kinematic computations.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line TBD)

.. code-block:: cpp

    bool get_robot_link_info(ROBOT_LINK_INFO& out, int timeout_ms = 300) {
        return _get_robot_link_info(_rbtCtrl, &out, timeout_ms);
    };

**Parameter**

.. list-table::
   :widths: 18 18 18 46
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - out
     - :ref:`ROBOT_LINK_INFO <struct_robot_link_info>`
     - -
     - Output structure that will be populated with the robot’s link/DH parameters.
   * - timeout_ms
     - int
     - 300
     - Timeout for the query in milliseconds.

**Return**

.. list-table::
   :widths: 10 20 70
   :header-rows: 1

   * - **Value**
     - **Type**
     - **Description**
   * - 0
     - int
     - Error — failed to retrieve link information (timeout or communication error).
   * - 1
     - int
     - Success — `out` structure was filled with the current link parameters.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect, select robot system, etc... (omitted)

       ROBOT_LINK_INFO link{};
       if (drfl.get_robot_link_info(link, 500)) {
           // Example: iterate joints and print DH-like parameters if provided by your firmware
           for (int j = 0; j < NUMBER_OF_JOINT; ++j) {
               // NOTE: actual field names depend on ROBOT_LINK_INFO definition in your SDK
               // e.g., link._tLink[j]._fA, link._tLink[j]._fD, link._tLink[j]._fAlpha, link._tLink[j]._fTheta
               printf("[J%d] a=%.6f, d=%.6f, alpha=%.6f, theta=%.6f\n",
                      j+1,
                      link._tLink[j]._fA,
                      link._tLink[j]._fD,
                      link._tLink[j]._fAlpha,
                      link._tLink[j]._fTheta);
           }
       } else {
           fprintf(stderr, "get_robot_link_info() failed (timeout or comm error)\n");
       }
       return 0;
   }

This example requests the controller’s **DH/link parameters** and prints them joint-by-joint.
Field names shown (`_fA`, `_fD`, `_fAlpha`, `_fTheta`) reflect common DH notation.
