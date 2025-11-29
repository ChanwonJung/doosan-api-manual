.. _manual_get_digital_input_ex:

get_digital_input_ex (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_digital_input_ex <get_digital_input>` during **Manual (Teach)** operations  
to **read digital input signals** from both the **control box** and **flange connector**  
when using API version **DRCF_VERSION == 3**.

Compared to :ref:`get_digital_input(Manual Mode) <manual_get_digital_input>`,  
this extended version supports **flange-level digital I/O** and **additional high-speed channels**  
for sensors and smart end-effectors.

**Typical usage**

- Monitor **gripper or sensor trigger inputs** from the flange connector.  
- Verify both **control box and flange** digital inputs during integration tests.  
- Debug I/O behavior in manual mode before enabling automatic operation.

.. Note::

    - For earlier firmware, use :ref:`get_digital_input(Manual Mode) <manual_get_digital_input>`.

**Example: Check control box and flange input states**

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
       // - Flange I/O device connected (optional)

       // 1) Read from control box inputs
       bool din1 = drfl.get_digital_input_ex(DIN_1);
       bool din2 = drfl.get_digital_input_ex(DIN_2);

       // 2) Read from flange inputs (if supported)
       bool f_din1 = drfl.get_digital_input_ex(FLANGE_DIN_1);
       bool f_din2 = drfl.get_digital_input_ex(FLANGE_DIN_2);

       std::printf("[CtrlBox DIN_1] = %s\n", din1 ? "ON" : "OFF");
       std::printf("[CtrlBox DIN_2] = %s\n", din2 ? "ON" : "OFF");
       std::printf("[Flange DIN_1]  = %s\n", f_din1 ? "ON" : "OFF");
       std::printf("[Flange DIN_2]  = %s\n", f_din2 ? "ON" : "OFF");

       return 0;
   }

**Tips**

- Use flange inputs for **real-time end-effector feedback** or **gripper-ready signals**.  
- Confirm correct signal polarity and grounding between flange and control box.  
- For debugging, log input states continuously with 100–200 ms intervals.  
