.. _set_rt_control_output:

set_rt_control_output
------------------------------------------
This function sets the **output data communication configuration**  
for Real-time External Control (from robot controller → external controller).  
It defines the version, transmission period, and optional loss count for UDP-based output streaming.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line XXX)

.. code-block:: cpp

   bool set_rt_control_output(string strVersion, float fPeriod, int nLossCnt) {
       return _set_rt_control_output(_rbtCtrlUDP, strVersion.c_str(), fPeriod, nLossCnt);
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
     - Output data version to be used for RT streaming (e.g., `"v1.0"`).
   * - fPeriod
     - float
     - -
     - Communication period in seconds. |br|
       Valid range: 0.001 ~ 1.0 [s] (1 kHz ~ 1 Hz transmission rate).
   * - nLossCnt
     - int
     - -
     - Reserved. Currently not used in this function.

**Note**

- ``fPeriod`` currently supports **0.001 s ~ 1.0 s**.  
- ``nLossCnt`` parameter is reserved and **not used** in the current controller version.  
- This function should be called after :ref:`connect_rt_control <connect_rt_control>`  
  and before :ref:`start_rt_control <start_rt_control>`.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Successfully configured RT output communication.
   * - 0
     - Failed to configure (e.g., invalid version or out-of-range period).

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Connect and configure RT output data
       drfl.connect_rt_control("192.168.137.100", 12347);

       std::string version = "v1.0";
       float period = 0.001f;   // 1 msec = 1 kHz
       int lossCount = 4;       // Reserved, not used

       if (drfl.set_rt_control_output(version, period, lossCount))
           std::cout << "RT output configuration set successfully." << std::endl;
       else
           std::cout << "Failed to set RT output configuration." << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

In this example, the function sets the RT output configuration for version `"v1.0"`  
with a 1 ms transmission period. The ``nLossCnt`` parameter is currently unused.

**Tips**

- Use the same period for both input and output to maintain real-time synchronization.  
- Smaller periods (e.g., 0.001–0.005 s) provide higher update rates but increase network load.  
- Adjust the period according to network latency and controller performance.
