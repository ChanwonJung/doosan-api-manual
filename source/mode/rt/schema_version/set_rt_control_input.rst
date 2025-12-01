.. _set_rt_control_input:

set_rt_control_input
------------------------------------------
This function sets the **input data communication configuration**  
for Real-time External Control (from external controller → robot controller).  
It defines the version, update period, and loss tolerance used for UDP-based input streaming.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 586)

.. code-block:: cpp

   bool set_rt_control_input(string strVersion, float fPeriod, int nLossCnt) {
       return _set_rt_control_input(_rbtCtrlUDP, strVersion.c_str(), fPeriod, nLossCnt);
   };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strVersion
     - string
     - -
     - Input data version to be used for RT streaming (e.g., `"v1.0"`)
   * - fPeriod
     - float
     - -
     - Communication period in seconds. |br|
       Valid range: **0.001 ~ 1.0 [s]** (1 kHz ~ 1 Hz update rate)
   * - nLossCnt
     - int
     - -
     - Maximum allowed consecutive packet loss count.  
       If the number of lost packets exceeds this value, the RT connection is automatically terminated. |br|
       When set to **-1**, loss count is not checked.

**Note**

- ``fPeriod`` currently supports **0.001 s ~ 1.0 s** only.  
- This function must be called **after** :ref:`connect_rt_control <connect_rt_control>`  
  and **before** :ref:`start_rt_control <start_rt_control>`.  
- Input schema must match one of the versions from :ref:`get_rt_control_input_version_list <get_rt_control_input_version_list>`.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Successfully configured RT input communication.
   * - 0
     - Failed to configure (e.g., invalid version, out-of-range period, or disconnected state).

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect and configure RT input data
       drfl.connect_rt_control("192.168.137.100", 12347);

       std::string version = "v1.0";
       float period = 0.001f;   // 1 msec = 1 kHz
       int lossCount = 4;

       if (drfl.set_rt_control_input(version, period, lossCount))
           std::cout << "RT input configuration set successfully." << std::endl;
       else
           std::cout << "Failed to set RT input configuration." << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function sets the RT input configuration for version `"v1.0"`  
with a 1 ms update rate and a loss tolerance of 4 consecutive packets.

**Tips**

- For stable performance, use a **period between 0.002 s and 0.01 s** depending on network conditions.  
- Matching input/output periods ensures smoother real-time synchronization.  
- If connection drops frequently, try increasing the ``nLossCnt`` value.
