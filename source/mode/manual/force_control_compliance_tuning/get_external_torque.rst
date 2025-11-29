.. _manual_get_external_torque:

get_external_torque (Manual Mode)
------------------------------------------

This section explains how to use :ref:`get_external_torque <get_external_torque>` during **Manual (Teach)** operations  
to **measure the external torques** applied to each joint of the robot arm.  
This value represents the **reaction torque caused by external contact, payload change, or manual force interaction**.

**Typical usage**

- Detect unexpected contact or collision by observing torque variations.  
- Validate payload estimation or balance adjustments.  
- Analyze force distribution during compliance or hand-guided teaching.  

.. Note::

    - The measured values are computed internally from joint torque sensors and dynamic model compensation.  
    - Use this function **only for monitoring**; it does not modify robot control.  
    - Available in all modes, but commonly used in **Manual (Teach)** for real-time feedback.

**Example: Monitor external torque during compliance test**

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
       // - Robot equipped with torque sensors

       // 1) Read external torque repeatedly
       for (int i = 0; i < 10; ++i) {
           LPROBOT_FORCE pExt = drfl.get_external_torque();
           if (pExt) {
               std::printf("[External Torque] Fx=%.2f Fy=%.2f Fz=%.2f | Tx=%.2f Ty=%.2f Tz=%.2f\n",
                   pExt->_fFx, pExt->_fFy, pExt->_fFz,
                   pExt->_fTx, pExt->_fTy, pExt->_fTz);
           }
           std::this_thread::sleep_for(std::chrono::milliseconds(200));
       }

       return 0;
   }

In this example, the program continuously reads **external torque and force values** to monitor  
physical interaction between the robot and its environment.  
When the robot is manually guided or comes into contact with an object,  
the changes in force and torque output indicate the direction and magnitude of applied external influence.

**Tips**

- Use for **contact detection** or verifying **compliance behavior** in real-time.  
- Large unexpected torque spikes may indicate collisions or improper payload settings.  
- Combine with :ref:`change_collision_sensitivity <manual_change_collision_sensitivity>` to fine-tune safety response.  
- When comparing with :ref:`get_tool_force <manual_get_tool_force>`, remember this function reports joint-based torque estimation, not tool-end measurement.
