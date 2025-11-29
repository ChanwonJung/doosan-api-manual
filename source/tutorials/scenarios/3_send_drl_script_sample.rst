6.6.3 **send_drl_script_sample.cpp**
----------------------------------------------
This example (``3_send_drl_script_sample.cpp``) demonstrates how to send and execute a **DRL script defined as a C++ string** and control its execution (start, pause, resume, stop) through the DRFLEx API:
Instead of loading a separate ``.drl`` file, the script is defined as a **string within the code** and transmitted to the controller using ``drl_start()``. |br|
In addition, this example shows how to control the execution flow of a DRL program using:

- ``drl_start()``
- ``drl_pause()``
- ``drl_resume()``
- ``drl_stop()``

This example is located in the following path: |br|
``API-DRFL/example/Linux_64/3_minimal_motion_sample.cpp.``

See the example on the `Doosan Robotics API-DRFL GitHub <https://github.com/DoosanRobotics/API-DRFL/blob/GL013300/example/Linux_64/3_send_drl_script_sample.cpp>`_.


Setup & Connection
~~~~~~~~~~~~~~~~~~~~~~

Before executing any DRL script, the program must connect to the controller, acquire **control authority (GRANT)** and verify that the robot state is **STANDBY**.

- ``DRCF_VERSION`` selects the communication protocol version used.  
- ``IP_ADDRESS`` is set to ``127.0.0.1``, assuming a **local emulator** (DART Platform / virtual controller). 
- For a **real robot controller**, provide the actual controller IP.  
- ``get_control_access`` and ``is_standby`` are updated using the callbacks below.


.. code-block:: cpp

   #define DRCF_VERSION 2 // Set 2 or 3 according to drcf version.

   const std::string IP_ADDRESS = "192.168.137.100"; // real mode
   CDRFLEx robot; // Instance for APIs

   bool get_control_access = false; // Variable to check control authority
   bool is_standby = false;        // Variable to check whether the robot state is standby.

Helper functions for converting enums to readable strings:

.. code-block:: cpp

   std::string to_str(const MONITORING_ACCESS_CONTROL x);
   std::string to_str(const ROBOT_STATE x);


Access Control & State Monitoring Callback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OnMonitroingAccessControlCallback monitors for **control authority (GRANT/LOSS)**

.. code-block:: cpp

   auto OnMonitroingAccessControlCB = [](const MONITORING_ACCESS_CONTROL access) {
     if (MONITORING_ACCESS_CONTROL_GRANT == access) {
       get_control_access = true;
       std::cout << "Got Control Access !! " << std::endl;
     }
     if (MONITORING_ACCESS_CONTROL_LOSS == access) {
       get_control_access = false;
     }
   };
   robot.set_on_monitoring_access_control(OnMonitroingAccessControlCB);

The OnMonitoringStateCallback monitors for **robot state**.
This callback is invoked whenever the robot state changes (for example,  
``STATE_SAFE_OFF``, ``STATE_STANDBY``, ``STATE_MOVING``).

.. code-block:: cpp

   auto OnMonitoringStateCB = [] (const ROBOT_STATE state) {
     if (STATE_STANDBY == state) {
       is_standby = true;
       std::cout << "Successfully Servo on !! " << std::endl;
     } else {
       is_standby = false;
     }
   };
   robot.set_on_monitoring_state(OnMonitoringStateCB);

You can confirm that the callbacks are set correctly by checking the console output when the program runs.
These output indicates that access was granted, and the robot reached **STANDBY** at least once.

.. code-block:: text

   Successfully Servo on !!
   Got Control Access !!
   Successfully Servo on !!


Connection & Version Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After registering callbacks, the sample opens the connection and prints controller version info.

.. code-block:: cpp

   // Connect to the drcf controller.
   bool ret = robot.open_connection(IP_ADDRESS);
   std::cout << "open connection return value " << ret << std::endl;
   if (true != ret) {
     std::cout << "Cannot open connection to robot @ " << IP_ADDRESS << std::endl;
     return 1;
   }
   
   // Monitoring compatibility
   robot.setup_monitoring_version(1);

   SYSTEM_VERSION tSysVerion = { '\0', };
   robot.get_system_version(&tSysVerion);
   std::cout << "Controller (DRCF) version: " << tSysVerion._szController << std::endl;
   std::cout << "Library version: " << robot.get_library_version() << std::endl;

You can confirm the connection and version information by checking the console output when the program runs.

.. code-block:: text

   open connection return value 1
   Controller (DRCF) version: GF03020000
   
Access Control & StandBy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following loop ensures that both control access is **GRANT**, 
and robot state is **STANDBY**, before starting the DRL program.

.. code-block:: cpp

   for (size_t retry = 0; retry < 10;
        ++retry, std::this_thread::sleep_for(std::chrono::milliseconds(1000))) {

     if (!get_control_access) {
       robot.ManageAccessControl(MANAGE_ACCESS_CONTROL_FORCE_REQUEST);
       continue;
     }

     if (!is_standby) {
       robot.set_robot_control(CONTROL_SERVO_ON);
       continue;
     }

     if (get_control_access && is_standby)
       break;
   }

   if (!(get_control_access && is_standby)) {
     std::cout << "Failed Setting intended states" << std::endl;
     return 1;
   }

If the robot fails to reach both states within 10 retries,  
the program exits with an error message.   


Robot Mode Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before executing DRL scripts, the robot must be in **AUTONOMOUS** mode:

.. code-block:: cpp

   if (!robot.set_robot_mode(ROBOT_MODE_AUTONOMOUS)) {
     return 1;
   }

``AUTONOMOUS`` mode is required for programmatic motion and DRL execution.  
(Teaching/configuration is typically done in ``MANUAL`` mode.)

DRL Script Definition & Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The example embeds a DRL script directly as a string literal:

.. code-block:: cpp

   std::cout << "Press Enter to continue ..." ;
   std::cin.get(); // Waits for user to press Enter

   std::string strDrl =
     "\r\n\
   loop = 0\r\n\
   while loop < 5:\r\n\
     movej(posj(0,0,90,0,90,0), vel=60, acc=60)\r\n\
     movej(posj(0,0,80,0,90,0), vel=60, acc=60)\r\n\
     loop+=1\r\n";

   robot.drl_start(ROBOT_SYSTEM_REAL, strDrl);

- The DRL syntax is identical to writing a ``.drl`` program.
- ``drl_start()`` transmits the script and begins its execution.  
- ``ROBOT_SYSTEM_VIRTUAL`` is used because this sample targets a virtual controller.
- In real mode, use ``ROBOT_SYSTEM_REAL`` instead.

Program Control (Pause / Resume / Stop)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After starting the DRL program, the example waits for user input before each control action:

.. code-block:: cpp

   std::cout << "Press Enter to pause ..." ;
   std::cin.get(); // Waits for user to press Enter
   robot.drl_pause();

   std::cout << "Press Enter to resume ..." ;
   std::cin.get(); // Waits for user to press Enter
   robot.drl_resume();

   std::cout << "Press Enter to stop ..." ;
   std::cin.get(); // Waits for user to press Enter
   robot.drl_stop();

   robot.close_connection();
   return 0;

- ``drl_pause()`` temporarily halts program execution.
- ``drl_resume()`` continues the program from where it paused.
- ``drl_stop()`` terminates the DRL program entirely.

You can confirm the state callback by checking the console output when the program runs.

.. code-block:: text

   Successfully Servo on !!
   open connection return value 1
   Controller (DRCF) version: GF03020000
   Library version: GL013300
   Got Control Access !!
   Successfully Servo on !!
   Press Enter to continue ...
   Press Enter to pause ...
   Press Enter to resume ...
   Press Enter to stop ...

These logs confirm that the DRL script started correctly, the user-controlled pause/resume worked, and the DRL program stopped safely.