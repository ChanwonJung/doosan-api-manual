.. _manual_get_digital_output:

get_digital_output (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_digital_output <get_digital_output>` during **Manual (Teach)** operations  
to **check the current ON/OFF status** of digital output channels on the **control box**  
when using API version **DRCF_VERSION == 2**.

**Typical usage**

- Verify whether a digital output (e.g., gripper open/close signal) is currently active.  
- Check if manual output toggling or DRL command has taken effect.  
- Debug wiring and output polarity during manual I/O testing.

.. Note::

    - For newer systems, use :ref:`get_digital_output_ex(Manual Mode) <manual_get_digital_output_ex>`.

**Example: Read digital output state**

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
       // - Digital outputs manually set or controlled by prior test

       // 1) Check DOUT_1 and DOUT_2 states
       bool dout1 = drfl.get_digital_output(DOUT_1);
       bool dout2 = drfl.get_digital_output(DOUT_2);

       std::printf("[DOUT_1] = %s\n", dout1 ? "ON" : "OFF");
       std::printf("[DOUT_2] = %s\n", dout2 ? "ON" : "OFF");

       return 0;
   }

**Tips**

- Use this function to confirm if **previous set_digital_output()** commands succeeded.  
- If outputs do not change, check **I/O permissions** and **external power supply**.  
