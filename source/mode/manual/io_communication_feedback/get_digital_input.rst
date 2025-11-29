.. _manual_get_digital_input:

get_digital_input (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_digital_input <get_digital_input>` during **Manual (Teach)** operations  
to **read the ON/OFF state** of digital input signals from the robot’s **control box I/O ports**  
when using API version **DRCF_VERSION == 2**.

**Typical usage**

- Check the current **sensor or switch state** wired to the control box.  
- Verify **safety interlocks, photo sensors, or external start signals** during manual setup.  
- Confirm correct wiring polarity and I/O assignment before automation.

.. Note::

    - For DRCF v3 and later, use :ref:`get_digital_input_ex(Manual Mode) <manual_get_digital_input_ex>`.

**Example: Read multiple digital inputs**

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
       // - Digital sensors connected to control box input pins

       // 1) Read digital input #1 and #2
       bool din1 = drfl.get_digital_input(DIN_1);
       bool din2 = drfl.get_digital_input(DIN_2);

       std::printf("[DIN_1] = %s\n", din1 ? "ON" : "OFF");
       std::printf("[DIN_2] = %s\n", din2 ? "ON" : "OFF");

       return 0;
   }

**Tips**

- Ensure the control box digital inputs are **properly powered** and configured as inputs.  
- For NPN/PNP type mismatches, verify the wiring reference (GND or +24V).  
- If values do not change, check I/O mapping or safety interlock configuration.  
