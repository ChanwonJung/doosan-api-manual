.. _set_on_rt_log_alarm:

set_on_rt_log_alarm
------------------------------------------
This function registers a **callback** that is triggered when a **log or alarm message**  
is received from the robot controller during **real-time external control**.

It allows external systems to monitor warnings, errors, and status logs in real time,  
enabling fast responses to safety or system issues while maintaining real-time control loops.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 663)

.. code-block:: cpp

   void set_on_rt_log_alarm(TOnLogAlarmCB pCallbackFunc) {
       _set_on_rt_log_alarm(_rbtCtrlUDP, pCallbackFunc);
   };

**Parameter**

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Description**
   * - pCallbackFunc
     - :ref:`TOnLogAlarmCB <cb_tonlogalarmcb>` 
     - Function pointer to user-defined callback that handles  |br|
       log or alarm messages sent from the robot controller.

**Note**

- The callback executes automatically when a **log or alarm event** occurs.  
- Use this callback to capture **real-time safety warnings**, **system messages**, or **controller errors**.  
- Avoid performing **slow or blocking operations** (such as file writing or printing at high frequency)  
  inside the callback to maintain communication stability.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — callback successfully registered.
   * - 0
     - Error — invalid callback or UDP communication failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   // Define callback for alarm and log monitoring
   void OnRTLogAlarm(const char* msg) {
       static int count = 0;
       if (++count % 20 == 0)  // Limit printing frequency
           printf("[RT LOG/ALARM] %s\n", msg);
   }

   int main() {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);

       // Register real-time log and alarm callback
       drfl.set_on_rt_log_alarm(OnRTLogAlarm);

       // Configure and start RT control
       string version = "v1.0";
       float period = 0.001f;
       int losscount = 4;

       drfl.set_rt_control_input(version, period, losscount);
       drfl.set_rt_control_output(version, period, losscount);
       drfl.start_rt_control();

       // Continuous loop (keep connection alive)
       while (true) {
           // The callback will automatically trigger when alarm/log events occur
       }

       drfl.disconnect_rt_control();
       return 0;
   }

In this example, ``OnRTLogAlarm()`` prints any alarm or log message  
that the controller sends during real-time control operation.

**Tips**

- Useful for **safety monitoring**, **diagnostics**, and **debug logging** during live control.  
- Integrate with a GUI or network logger to visualize alarm states in real time.  
- Keep the callback **lightweight** to avoid interrupting UDP data flow.
