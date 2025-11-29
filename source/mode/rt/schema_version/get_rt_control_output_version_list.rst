.. _get_rt_control_output_version_list:

get_rt_control_output_version_list
------------------------------------------
This function retrieves the list of supported **Real-time (RT) output data versions**  
available on the robot controller.  
Each version represents a predefined output data schema determining  
which robot states (e.g., joint position, torque, I/O signals) are streamed from the controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 582)

.. code-block:: cpp

   string get_rt_control_output_version_list() { 
       return _get_rt_control_output_version_list(_rbtCtrlUDP); 
   };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - String
     - Comma-separated list of available RT **Output Data Versions** supported by the controller.

**Version List**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - **Output Data Version**
     - **First Supported Controller Version**
   * - v1.0
     - V2.9 and above

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect and query RT output version list
       drfl.connect_rt_control("192.168.137.100", 12347);
       std::string version_list = drfl.get_rt_control_output_version_list();
       std::cout << "Available RT output versions: " << version_list << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function retrieves all supported RT output data versions  
(e.g., `"v1.0"`) that define the available output schema of the controller.

**Tips**

- Use this before calling :ref:`set_rt_control_output <set_rt_control_output>` to select a valid version.  
- The available versions depend on the **controller firmware version**.  
- Input/output versions must match when using synchronized RT communication.
