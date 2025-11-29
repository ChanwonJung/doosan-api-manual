.. _manual_get_analog_input_ex:

get_analog_input_ex (Manual Mode)
----------------------------------------------------------
This section explains how to use :ref:`get_analog_input_ex <get_analog_input>` during **Manual (Teach)** operations  
to **read analog input values** from both the **control box** and **flange** ports  
when using API version **DRCF_VERSION == 3**.

Compared to :ref:`get_analog_input <get_analog_input>`,  
this extended version supports **multiple analog input sources** (Control Box + Flange)  
and provides improved sampling stability for high-resolution sensors.

**Typical usage**

- Measure analog feedback from **end-effector sensors** connected to flange ports.  
- Monitor **control box analog inputs** simultaneously during manual setup.  
- Validate wiring, scaling, and reference voltage before automated operation.

.. Note::

    - Supported input range depends on the robot’s configuration (typically **0–10 V** or **4–20 mA**).  

**Example: Read both control box and flange analog inputs**

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
       // - Control box or flange analog devices connected properly

       // 1) Read analog inputs from control box
       float cb_ch1 = drfl.get_analog_input_ex(ANALOG_IN_CH1);
       float cb_ch2 = drfl.get_analog_input_ex(ANALOG_IN_CH2);
       std::printf("[CtrlBox CH1] = %.3f V\n", cb_ch1);
       std::printf("[CtrlBox CH2] = %.3f V\n", cb_ch2);

       // 2) Read analog inputs from flange (if supported)
       float fl_ch1 = drfl.get_analog_input_ex(FLANGE_ANALOG_IN_CH1);
       float fl_ch2 = drfl.get_analog_input_ex(FLANGE_ANALOG_IN_CH2);
       std::printf("[Flange CH1] = %.3f V\n", fl_ch1);
       std::printf("[Flange CH2] = %.3f V\n", fl_ch2);

       return 0;
   }

**Tips**

- Check the robot model’s documentation to confirm which flange analog channels are available.  
- For precise sensors, enable **hardware filtering or averaging** via the pendant settings.  
- Avoid simultaneous read/write operations on multiple analog ports to prevent data delay.  
