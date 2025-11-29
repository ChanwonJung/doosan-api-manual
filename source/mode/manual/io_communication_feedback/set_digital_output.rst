.. _manual_set_digital_output:

set_digital_output (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`set_digital_output <set_digital_output>` during **Manual (Teach)** operations  
to **manually turn ON or OFF digital output channels** on the **control box**  
when using API version **DRCF_VERSION == 2**.

**Typical usage**

- Control external devices such as **grippers**, **relays**, **valves**, or **indicators**.  
- Verify output signal wiring and polarity during installation.  
- Perform manual I/O testing before enabling Auto (Program) mode.

.. Note::

    - For newer systems, use :ref:`set_digital_output_ex(Manual Mode) <manual_set_digital_output_ex>`.

**Example: Control digital outputs on control box**

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
       // - External devices connected to control box output terminals

       // 1) Turn ON DOUT_1 for 1 second
       drfl.set_digital_output(DOUT_1, true);
       std::printf("[DOUT_1] = ON\n");
       std::this_thread::sleep_for(std::chrono::seconds(1));

       // 2) Turn OFF DOUT_1
       drfl.set_digital_output(DOUT_1, false);
       std::printf("[DOUT_1] = OFF\n");

       return 0;
   }

**Tips**

- Verify **output mode (Sink/Source)** matches the external device type (NPN/PNP).  
- If output doesn’t change, check the **external 24V supply** and **safety interlock state**.  
- Combine with :ref:`get_digital_output <manual_get_digital_output>` to confirm output states.  
