6.6.5 **minimal_instruction_sample.cpp**
---------------------------------------------
This example (``5_minimal_instruction_sample.cpp``) demonstrates a **step-by-step instruction flow**
for controlling the robot using the API: 

- register monitoring callbacks,
- open/close the controller connection,
- request **control authority**,
- turn **Servo On** and check system/version,
- switch **robot mode/system**,
- execute a simple **joint motion** (``movej``),
- test **inverse kinematics** (``ikin``),
- and send/stop a **DRL script**.

Each function is mapped to a numeric key (1~8), so users can trigger individual operations  
one by one and observe how the API behaves in real time.

This example is located in the following path: |br|
``API-DRFL/example/Linux_64/5_minimal_instruction_sample.cpp``

**See the example on the** `Doosan Robotics API-DRFL GitHub <https://github.com/DoosanRobotics/API-DRFL/blob/GL013300/example/Linux_64/5_minimal_instruction_sample.cpp>`_.

**Watch the full walk-through on the** `Doosan Robotics Official Youtube <https://www.youtube.com/watch?v=tADMjcAb92A>`_.

.. raw:: html

   <div style="text-align:center; margin: 1em 0;">
     <iframe width="640" height="360"
             src="https://www.youtube.com/embed/tADMjcAb92A"
             title="Tutorial Video"
             frameborder="0"
             allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
             allowfullscreen>
     </iframe>
   </div>


Setup & Global Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example uses a global controller object and several flags to track control status.

.. code-block:: cpp

   #include "../../include/DRFLEx.h"
   using namespace DRAFramework;

   CDRFLEx Drfl;

   bool g_bHasControlAuthority = FALSE;
   bool g_TpInitailizingComplted = FALSE;
   bool g_mStat = FALSE;
   bool g_Stop = FALSE;
   bool moving = FALSE;

A DRL script string and helper flags are also defined.

.. code-block:: cpp

   std::string strDrl =
       "\r\n\
   loop = 0\r\n\
   while loop < 1003:\r\n\
    movej(posj(10,10.10,10,10.10), vel=60, acc=60)\r\n\
    movej(posj(00,00.00,00,00.00), vel=60, acc=60)\r\n\
    loop+=1\r\n";

   bool bAlterFlag = FALSE;

These globals are used throughout the example to store the DRFLEx instance, track whether control authority has been granted, 
control motion stop/pause/resume, and prepare DRL motion tests.

Keyboard Menu & Main loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main loop reads a key from the console and executes a corresponding instruction block.

.. code-block:: cpp

   bool bLoop = TRUE;
   while (bLoop) {
     g_mStat = false;
     g_Stop = false;

     std::cout << "\ninput key : ";
     char ch;
     std::cin >> ch;

     switch (ch) {
       case 'q':
         bLoop = FALSE;
         Drfl.close_connection();
         std::cout << "Close Connection !! " << std::endl;
         break;
       case '1':
         // Register callbacks
         break;
       case '2':
         // Open connection
         break;
       case '3':
         // Request control authority
         break;
       case '4':
         // Servo On & monitoring version
         break;
       case '5':
         // Robot mode/system
         break;
       case '6':
         // Joint motion
         break;
       case '7':
         // Kinematics test
         break;
       case '8':
         // DRL script
         break;
       case '9':
         // Reserved
         break;
       default:
         break;
     }

     std::this_thread::sleep_for(std::chrono::milliseconds(100));
   }

This structure makes the example a **minimal instruction console**:  
you can manually trigger each step of the control pipeline and see the result immediately.

Callback Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the user presses ``1``, the example registers several monitoring and event callbacks.

.. code-block:: cpp

   case '1':
   {
     Drfl.set_on_monitoring_data_ex(OnMonitoringDataExCB);
     Drfl.set_on_monitoring_ctrl_io_ex(OnMonitoringCtrlIOExCB);
     Drfl.set_on_log_alarm(OnLogAlarm);
     Drfl.set_on_disconnected(OnDisConnected);
     // Optional callbacks (commented):
     // Drfl.set_on_monitoring_state(OnMonitoringStateCB);
     // Drfl.set_on_tp_initializing_completed(OnTpInitializingCompleted);
     // Drfl.set_on_tp_popup(OnTpPopup);
     // Drfl.set_on_tp_log(OnTpLog);
     // Drfl.set_on_tp_progress(OnTpProgress);
     // Drfl.set_on_tp_get_user_input(OnTpGetuserInput);
     // Drfl.set_on_rt_monitoring_data(OnRTMonitoringData);
     std::cout << "Register Callbacks !! " << std::endl;
   }
   break;

These callbacks allow the application to monitor task/world poses and IO status, receive alarm information (``OnLogAlarm``), automatically reconnect when disconnected (``OnDisConnected``), 
and optionally integrate with TP events and real-time monitoring.

Example console output:

.. code-block:: text

   input key : 1
   Register Callbacks !!


Connection to Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~

Pressing ``2`` opens a TCP/IP connection to the controller.

.. code-block:: cpp

   case '2':
   {
     assert(Drfl.open_connection("192.168.137.100"));
     std::cout << "Open Connection !! " << std::endl;
   }
   break;

- The example uses ``192.168.137.100`` assuming a **real controller**.  
- For a virtual mode, replace this with the ``127.0.0.1``.

Example console output:

.. code-block:: text

   input key : 2
   Open Connection !!


Control Authority Handling 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Key ``3`` requests control authority and sets a simple access-control callback.

.. code-block:: cpp

   case '3':
   {
     // Request control authority
     Drfl.ManageAccessControl(MANAGE_ACCESS_CONTROL_FORCE_REQUEST);

     Drfl.set_on_monitoring_access_control(
       [](const MONITORING_ACCESS_CONTROL eTrasnsitControl)
       {
         if (MONITORING_ACCESS_CONTROL_GRANT == eTrasnsitControl) {
           g_bHasControlAuthority = TRUE;
           std::cout << "Successfully got Control Authority !! " << std::endl;
         } else {
           std::cout << "Unintended autority.. " << std::endl;
         }
       }
     );

     std::cout << "Try to get Control Authority !!" << std::endl;
   }
   break;

- ``MANAGE_ACCESS_CONTROL_FORCE_REQUEST`` forces an access request to the controller.
- When granted, ``g_bHasControlAuthority`` is set to ``TRUE`` and a message is printed.

Example console output:

.. code-block:: text

   input key : 3
   Try to get Control Authority !!
   Successfully got Control Authority !!

Servo On & Monitoring Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Key ``4`` enables Servo, configures monitoring version, and prints system information.

.. code-block:: cpp

   case '4':
   {
     Drfl.setup_monitoring_version(1);
     Drfl.set_robot_control(CONTROL_SERVO_ON);
     Drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_10, TRUE);

     SYSTEM_VERSION tSysVerion = { '\0', };
     Drfl.get_system_version(&tSysVerion);
     std::cout << "System version: " << tSysVerion._szController << std::endl;
     std::cout << "Library version: " << Drfl.get_library_version() << std::endl;

     while ((Drfl.get_robot_state() != STATE_STANDBY) || !g_bHasControlAuthority)
       std::this_thread::sleep_for(std::chrono::milliseconds(1000));

     std::cout << "Servo On !! " << std::endl;
   }
   break;

- ``setup_monitoring_version(1)`` selects the newer monitoring context.
- ``set_robot_control(CONTROL_SERVO_ON)`` turns Servo On.
- The loop waits until both **robot state = STANDBY** and **control authority** are satisfied.

Example console output:

.. code-block:: text

   input key : 4
   System version: GF03020000
   Library version: GL013300
   Servo On !!


Robot Mode & System Configuration 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Key ``5`` switches to **AUTONOMOUS** mode and **REAL** system.

.. code-block:: cpp

   case '5':
   {
     assert(Drfl.set_robot_mode(ROBOT_MODE_AUTONOMOUS));
     assert(Drfl.set_robot_system(ROBOT_SYSTEM_REAL));
     std::cout << "Set Auto Mode !!" << std::endl;
   }
   break;

- ``ROBOT_MODE_AUTONOMOUS`` enables programmatic motion execution.
- ``ROBOT_SYSTEM_REAL`` indicates that the motion is executed on a real robot. Also you can change ``ROBOT_SYSTEM_VIRTUAL`` if you want to execute in virtual mode.  

Example console output:

.. code-block:: text

   input key : 5
   Set Auto Mode !!


Joint Motion Execution 
~~~~~~~~~~~~~~~~~~~~~~~~~~

Key ``6`` executes a simple **joint-space motion** using ``movej``.

.. code-block:: cpp

   case '6':
   {
     std::cout << "Move Start !!  " << std::endl;

     float p1[6] = {0, 0, 10, 0, 10, 0};
     Drfl.movej(p1, 60, 30);

     float p2[6] = {0, 0, 0, 0, 0, 0};
     Drfl.movej(p2, 30, 30);

     std::cout << "Move End !!  " << std::endl;
   }
   break;

- First move: joint 3 and 5 move to 10 deg at velocity 60, acceleration 30.
- Second move: all joints return to 0 deg at velocity 30, acceleration 30.

Example console output:

.. code-block:: text

   input key : 6
   Move Start !!  
   Move End !!  


Kinematics Test 
~~~~~~~~~~~~~~~~~~~

Key ``7`` demonstrates how to use the **inverse kinematics** function ``ikin``.

.. code-block:: cpp

   case '7':
   {
     // Motion execution using kinematics functions
     float x1[6] = {370.9, 719.7, 651.5, 90, -180, 0}; // task-space pose for IK conversion
     LPROBOT_POSE res = Drfl.ikin(x1, 2); // ROBOT_POSE structure contains 6 float elements
     
     // Store the IK result using a shallow copy
     float q1[6] = {0,};
     for (int i = 0; i < 6; i++) {
       q1[i] = res->_fPosition[i]; // Copy elements from the returned LPROBOT_POSE
     }
     std::cout << " Get ikin Success (Task Space -> Joint Space) !! " << std::endl;
     // Optionally: Drfl.movej(q1, 60, 30);
   }
   break;

- ``ikin`` computes a joint-space solution from a given task-space pose.
- The result can be used directly in a subsequent ``movej`` command.

Example console output:

.. code-block:: text

   input key : 7
    Get ikin Success (Task Space -> Joint Space) !!


DRL Script Execution 
~~~~~~~~~~~~~~~~~~~~~~~

Key ``8`` sends and executes a **DRL script** that performs two ``movej`` motions.

.. code-block:: cpp

   case '8':
   {
     // DRL script example
     std::string strDrl =
       "movej([0, 0, 10, 0, 10, 0], 60, 30)\n"
       "movej([0, 0, 0, 0, 0, 0], 60, 30)\n";
     
     // Implements a simple DRL script that moves the robot between two positions using movej commands
     Drfl.drl_start(ROBOT_SYSTEM_REAL, strDrl); // Use ROBOT_SYSTEM_REAL for actual hardware execution
     Drfl.set_on_program_stopped(OnProgramStopped);

     std::cout << "Sent DRL Script !!" << std::endl;
   }
   break;

The registered ``OnProgramStopped`` callback handles program termination.

.. code-block:: cpp

   void OnProgramStopped(const PROGRAM_STOP_CAUSE) {
     Drfl.drl_stop();
     std::cout << "program stopped" << std::endl;
   }

During execution, alarm logs may appear when the DRL program stops.

.. code-block:: text

   input key : 8
   Sent DRL Script !!
   input key : Alarm Info: group(1), index(2007), param(), param(), param()
   program stopped

This confirms that the DRL script was sent the program executed and the stop event and alarm were handled correctly.

.. note::
  
  A DRL script string and helper flags are also defined. |br|
  In this minimal sample, a shorter inline DRL script is used in key ``8`` for clarity,
  while the global ``strDrl`` shows an example of a more complex looped motion that can
  be reused or extended in user applications.

  .. code-block:: cpp

    string strDrl =
    "\r\n\
    loop = 0\r\n\
    while loop < 1003:\r\n\
    movej(posj(10,10.10,10,10.10), vel=60, acc=60)\r\n\
    movej(posj(00,00.00,00,00.00), vel=60, acc=60)\r\n\
    loop+=1\r\n";



Xenomai / Real-time Environment Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This sample also supports building in a **Xenomai-based real-time environment**.  
When compiled with the ``__XENO__`` macro, the following code paths are enabled.

.. code-block:: cpp

   #ifdef __XENO__
   #include <rtdk.h>
   #include <native/task.h>
   #include <native/timer.h>
   #else
   // Standard Linux / non-RT environment
   #endif // __XENO__

In the main loop, the real-time task is scheduled with a fixed period.

.. code-block:: cpp

   #ifdef __XENO__
       unsigned long overrun = 0;
       const double tick = 1000000;  // 1 ms
       rt_task_set_periodic(nullptr, TM_NOW, tick);
       if (rt_task_wait_period(&overrun) == -ETIMEDOUT) {
         std::cout << __func__ << ": over-runs: " << overrun << std::endl;
       }
   #else
       std::this_thread::sleep_for(std::chrono::microseconds(1000));
   #endif  // __XENO__

- In **non-RT environments**, the loop simply sleeps using
  ``std::this_thread::sleep_for``.
- In **Xenomai RT environments**, the loop is driven by
  ``rt_task_set_periodic`` and ``rt_task_wait_period`` to achieve
  deterministic timing and to detect possible **overruns**.

These blocks are independent from the DRFLEx API logic itself and are only
required when deploying the sample in a strict real-time control environment.
