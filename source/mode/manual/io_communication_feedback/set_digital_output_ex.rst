.. _manual_set_digital_output_ex:

set_digital_output_ex (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`set_digital_output_ex <set_digital_output>` during **Manual (Teach)** operations  
to **control both control box and flange digital outputs**  
when using API version **DRCF_VERSION == 3**.

Compared to :ref:`set_digital_output(Manual mode) <manual_set_digital_output>`,  
this extended version supports **flange-level output control**, allowing direct operation of  
grippers, sensors, and other end-effector devices without external wiring.

**Typical usage**

- Directly control **tool I/O outputs** from the robot flange during manual tests.  
- Operate **grippers, vacuum valves, or solenoids** for end-effector actuation.  
- Test both **control box outputs** and **flange outputs** in one API version.

**Example: Control control box and flange outputs**

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
       // - DRCF_VERSION == 3
       // - Flange and control box outputs available

       // 1) Turn ON control box output DOUT_1
       drfl.set_digital_output_ex(DOUT_1, true);
       std::printf("[CtrlBox DOUT_1] = ON\n");

       // 2) Turn ON flange output FLANGE_DOUT_1
       drfl.set_digital_output_ex(FLANGE_DOUT_1, true);
       std::printf("[Flange DOUT_1] = ON\n");

       std::this_thread::sleep_for(std::chrono::seconds(1));

       // 3) Turn OFF both outputs
       drfl.set_digital_output_ex(DOUT_1, false);
       drfl.set_digital_output_ex(FLANGE_DOUT_1, false);
       std::printf("[Outputs] = OFF\n");

       return 0;
   }

**Tips**

- Flange outputs are ideal for **end-effector power or control lines**.  
- Verify flange output wiring and tool connector pin assignments before testing.  
- If the output signal does not toggle, ensure **tool power supply** is active.  