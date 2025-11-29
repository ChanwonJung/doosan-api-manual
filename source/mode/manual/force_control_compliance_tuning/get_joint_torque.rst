.. _manual_get_joint_torque:

get_joint_torque (Manual Mode)
------------------------------------------

This section explains how to use :ref:`get_joint_torque <get_joint_torque>` during **Manual (Teach)** operations  
to **read the torque values** measured by each **joint’s built-in torque sensor**.  
These values reflect both **gravity-compensated joint load** and any **external force influence**.

**Typical usage**

- Monitor individual joint torques to detect overload or imbalance.  
- Analyze torque trends during hand-guided motion or gravity compensation tuning.  
- Verify joint torque readings after collision or compliance operations.  

.. Note::

    - The values represent **total joint torque**, including dynamic and external effects.  
    - For detecting **only external reaction torque**, use :ref:`get_external_torque <manual_get_external_torque>`.  
    - This function is read-only and available in all operation modes.

**Example: Display joint torque values for monitoring**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - Servo enabled or robot stationary for accurate measurement

       for (int i = 0; i < 10; ++i) {
           LPROBOT_FORCE pJointTor = drfl.get_joint_torque();
           if (pJointTor) {
               std::printf("[Joint Torque] J1=%.2f J2=%.2f J3=%.2f J4=%.2f J5=%.2f J6=%.2f\n",
                   pJointTor->_fFx, pJointTor->_fFy, pJointTor->_fFz,
                   pJointTor->_fTx, pJointTor->_fTy, pJointTor->_fTz);
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(200));
       }

       return 0;
   }

In this example, the host PC periodically queries the robot controller for **joint torque values**.  
The printed output displays real-time torque feedback for all six joints,  
which can be used to detect unbalanced loads or verify torque behavior during manual movement.  
This approach helps confirm that the robot’s torque sensors and payload parameters are functioning correctly.

**Tips**

- Ideal for **teaching mode diagnostics** and **gravity compensation verification**.  
- If torque readings drift when stationary, check payload settings or calibration.  
- Compare with :ref:`get_external_torque <manual_get_external_torque>` to distinguish joint vs. external torque effects.  
- Avoid sampling during high-speed motion to prevent transient spikes from inertia.
