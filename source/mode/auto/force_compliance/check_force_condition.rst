.. _auto_check_force_condition:

check_force_condition (Auto Mode)
------------------------------------------
This section explains how to use :ref:`check_force_condition <check_force_condition>`
during Auto (Run) operations to verify whether the measured force or torque
on a selected axis remains within a defined threshold.

It is commonly used for contact detection, assembly checks,
and other safety-related conditions during automated motion.

**Typical usage**

- Monitor **contact forces** during assembly or insertion processes.  
- Detect surface contact or completion of tightening/pressing tasks.  
- Implement **safety thresholds** to stop or adjust operations  
  when excessive force is detected.  
- Combine with :ref:`check_position_condition <check_position_condition>`  
  for hybrid **force–position** validation.  
- Integrate into control loops for dynamic adjustment of robot behavior in real-time.

.. Note::

  - Can be called cyclically (e.g., every 50–100 ms) within process loops for smooth feedback control.

**Example: Force-Based Contact Detection in Auto Mode**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   #include <chrono>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established
       // - Servo ON
       // - Auto (Run) mode active
       // - F/T sensor calibrated or internal force estimation enabled

       // 1) Define downward motion path
       float fPosStart[6] = {400.f, 300.f, 500.f, 180.f, 0.f, 0.f};
       float fPosApproach[6] = {400.f, 300.f, 450.f, 180.f, 0.f, 0.f};

       // 2) Move near the target surface
       drfl.movel(fPosStart, (float[2]){100.f, 50.f}, (float[2]){300.f, 100.f});
       drfl.mwait();

       // 3) Gradually approach the surface
       drfl.movel(fPosApproach, (float[2]){40.f, 15.f}, (float[2]){200.f, 100.f});
       drfl.mwait();

       // 4) Monitor contact condition: Z-axis force between 5 N and 20 N
       bool contactDetected = false;
       while (!contactDetected) {
           contactDetected = drfl.check_force_condition(FORCE_AXIS_Z, 5.f, 20.f, COORDINATE_SYSTEM_TOOL);
           std::this_thread::sleep_for(std::chrono::milliseconds(50));
       }

       printf("Surface contact detected (Z force within 5–20 N).\n");

       // 5) Stop motion or trigger next step
       drfl.stop(STOP_TYPE_QUICK);

       return 0;
   }

In this example, the robot performs a downward motion during Auto mode  
and continuously checks the measured Z-axis force.  
When the detected force enters the defined range (5–20 N),  
the robot recognizes contact and stops motion automatically.  
This ensures reliable and safe contact-based task execution.

**Tips**

- Use ``COORDINATE_SYSTEM_TOOL`` for tool-aligned force checks during insertion or pressing.  
- Set appropriate force thresholds to prevent damage to tools or workpieces.  
- Combine with ``stop()`` or ``move_pause()`` for automatic reaction upon detection.  
- Use short polling intervals (50–100 ms) for responsive control.  
