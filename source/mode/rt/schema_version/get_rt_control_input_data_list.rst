.. _get_rt_control_input_data_list:

get_rt_control_input_data_list
------------------------------------------
This function returns a list of **input data fields** supported by a specific  
Real-time (RT) input data version. |br|
Each version defines which external signals can be transmitted to the robot controller  
during real-time operation.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 584)

.. code-block:: cpp

   string get_rt_control_input_data_list(string strVersion) { 
       return _get_rt_control_input_data_list(_rbtCtrlUDP, strVersion.c_str()); 
   };

**Parameter**

.. list-table::
   :widths: 25 25 20 30
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strVersion
     - string
     - -
     - Target **input data version** (e.g., `"v1.0"`).

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - string
     - Comma-separated list of available input data fields for the specified version.

**Input Data List**

.. list-table::
   :widths: 25 20 35 20
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Description**
     - **First Supported Controller Version**
   * - external_force_torque
     - float[6]
     - External force/torque sensor input.
     - v1.0
   * - external_digital_input
     - uint16
     - External digital input (16 channels).
     - v1.0
   * - external_digital_output
     - uint16
     - External digital output (16 channels).
     - v1.0
   * - external_analog_input
     - float[6]
     - External analog input (6 channels).
     - v1.0
   * - external_analog_output
     - float[6]
     - External analog output (6 channels).
     - v1.0

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       drfl.connect_rt_control("192.168.137.100", 12347);

       // Retrieve input data fields for version v1.0
       std::string data_list = drfl.get_rt_control_input_data_list("v1.0");
       std::cout << "Input data fields: " << data_list << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function queries all available **input data fields**  
for the specified version (`"v1.0"`), allowing the user to configure compatible RT input schema.

**Tips**

- Use this after calling :ref:`get_rt_control_input_version_list <get_rt_control_input_version_list>`  
  to confirm the supported input version.  
- The list may vary depending on firmware updates or controller model.  
- Each listed field corresponds to a structure element used in :ref:`write_data_rt <write_data_rt>`.
