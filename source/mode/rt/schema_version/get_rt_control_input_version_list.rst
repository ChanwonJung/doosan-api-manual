.. _get_rt_control_input_version_list:

get_rt_control_input_version_list
------------------------------------------
This function retrieves the list of supported **Real-time (RT) input data versions**  
available on the robot controller.  
Each version corresponds to a predefined input data schema that determines  
which external data fields (e.g., F/T sensor, DI, DO, AI, AO) can be transmitted to the controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 583)

.. code-block:: cpp

   string get_rt_control_input_version_list() { 
       return _get_rt_control_input_version_list(_rbtCtrlUDP); 
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
     - Comma-separated list of available RT **Input Data Versions**.

**Version List**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - **Input Data Version**
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

       // Connect and query RT input version list
       drfl.connect_rt_control("192.168.137.100", 12347);
       std::string version_list = drfl.get_rt_control_input_version_list();
       std::cout << "Available RT input versions: " << version_list << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function queries the controller for all supported  
RT input data versions, such as `"v1.0"`, which can then be used when calling  
:ref:`set_rt_control_input <set_rt_control_input>` to configure the streaming schema.

**Tips**

- Use this function **before** starting RT control to check version compatibility.  
- Returned list may vary depending on controller firmware version.  
- Always ensure both input/output versions match when configuring RT streaming.
