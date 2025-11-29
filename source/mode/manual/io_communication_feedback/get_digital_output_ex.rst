.. _manual_get_digital_output_ex:

get_digital_output_ex (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_digital_output_ex <get_digital_output>` during **Manual (Teach)** operations  
to **read the current digital output states** from both **control box** and **flange I/O**  
when using API version **DRCF_VERSION == 3**.

Compared to :ref:`get_digital_output(Manual Mode) <manual_get_digital_output>`,  
this extended version supports **flange-level digital outputs** and improved I/O synchronization  
for advanced tooling and sensor control.

**Typical usage**

- Monitor output signals to both control box and flange ports.  
- Verify gripper, solenoid, or light activation states during manual testing.  
- Confirm output transitions in real-time before executing Auto sequences.

.. Note::

    - For legacy systems, use :ref:`get_digital_output(Manual Mode) <manual_get_digital_output>`.

**Example: Check control box and flange output states**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active
       // - DRCF_VERSION == 3
       // - Digital outputs configured or toggled previously

       // 1) Check control box outputs
       bool dout1 = drfl.get_digital_output_ex(DOUT_1);
       bool dout2 = drfl.get_digital_output_ex(DOUT_2);

       // 2) Check flange outputs (if supported)
       bool f_dout1 = drfl.get_digital_output_ex(FLANGE_DOUT_1);
       bool f_dout2 = drfl.get_digital_output_ex(FLANGE_DOUT_2);

       std::printf("[CtrlBox DOUT_1] = %s\n", dout1 ? "ON" : "OFF");
       std::printf("[CtrlBox DOUT_2] = %s\n", dout2 ? "ON" : "OFF");
       std::printf("[Flange DOUT_1]  = %s\n", f_dout1 ? "ON" : "OFF");
       std::printf("[Flange DOUT_2]  = %s\n", f_dout2 ? "ON" : "OFF");

       return 0;
   }

**Tips**

- Use flange outputs for **tool control** or **signal forwarding to attached devices**.  
- If readings differ from expected state, check whether **outputs are interlocked** by safety settings.  
- Combine with :ref:`set_digital_output <set_digital_output>` for real-time verification.  
