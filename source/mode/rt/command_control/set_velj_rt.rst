.. _set_velj_rt:

set_velj_rt
------------------------------------------
This function sets the **global joint speed limit** used during **real-time servo motion control**.  
It defines the maximum allowable joint velocity for all servo motion commands executed via the real-time control interface.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 592)

.. code-block:: cpp

   bool set_velj_rt(float vel[NUM_JOINT]) {
       return _set_velj_rt(_rbtCtrlUDP, vel);
   };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - vel
     - float[6]
     - -
     - Global joint velocity limit [deg/s] applied during real-time control.

**Note**

- If the joint velocity commanded by a servo motion function  |br|
  (e.g., :ref:`servoj_rt <servoj_rt>` or :ref:`speedj_rt <speedj_rt>`) |br|  
  exceeds the defined global limit, an **Info message** is generated.  
- This function does **not stop** motion automatically; it only logs or warns about the exceedance.  
- The limit is maintained until explicitly changed or the real-time control session is terminated.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — velocity limit successfully applied.
   * - 0
     - Error — invalid parameter or communication failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);

       // Define global joint velocity limits [deg/s]
       float vel[6] = {100.f, 100.f, 100.f, 100.f, 100.f, 100.f};

       // Apply velocity limits for real-time servo motion
       if (drfl.set_velj_rt(vel))
           std::cout << "Global joint velocity limit set successfully." << std::endl;
       else
           std::cout << "Failed to set velocity limit." << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

This example sets a uniform joint velocity limit of 100 deg/s  
to restrict motion speed during real-time servo operations.

**Tips**

- Use this function **before starting RT motion** (e.g., before calling ``servoj_rt``).  
- It helps prevent excessive joint velocity in unstable communication or high-frequency control.  
- The same configuration can be re-applied dynamically without restarting RT mode.
