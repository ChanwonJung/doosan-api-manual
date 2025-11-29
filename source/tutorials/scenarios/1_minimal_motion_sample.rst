6.6.1 **minimal_motion_sample.cpp**
------------------------------------

This example (``1_minimal_motion_sample.cpp``) demonstrates the minimal procedure required to ensure **safe robot movement** using the API:

- connect to the controller,
- acquire **control authority** (GRANT),
- wait until the robot state becomes **STANDBY**,
- configure the system/mode,
- and then execute a short joint motion using ``movej``.

This example is located in the following path: |br|
``API-DRFL/example/Linux_64/1_minimal_motion_sample.cpp.``

See the example on the `Doosan Robotics API-DRFL GitHub <https://github.com/DoosanRobotics/API-DRFL/blob/GL013300/example/Linux_64/1_minimal_motion_sample.cpp>`_.

Setup & Connection
~~~~~~~~~~~~~~~~~~~~~~

- ``DRCF_VERSION`` selects the communication protocol version used by the controller.  
- ``IP_ADDRESS`` is set to ``127.0.0.1``, assuming a **local emulator** (DART Platform / virtual controller). 
- For a **real robot controller**, set the actual controller IP. 
- ``get_control_access`` and ``is_standby`` are **global flags** that the callbacks will update.

.. code-block:: cpp

   #define DRCF_VERSION 2 // Set 2 or 3 according to drcf version.

   const std::string IP_ADDRESS = "192.168.137.100"; // real mode
   CDRFLEx robot; // Instance for APIs

   bool get_control_access = false; // Variable to check control authority
   bool is_standby = false;        // Variable to check whether the robot state is standby.

The helper functions ``to_str(MONITORING_ACCESS_CONTROL)`` and ``to_str(ROBOT_STATE)`` convert enum values into human-readable strings for logging:

.. code-block:: cpp

   std::string to_str(const MONITORING_ACCESS_CONTROL x);
   std::string to_str(const ROBOT_STATE x);


Access Control & State monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OnMonitroingAccessControlCallback monitors for **control authority (GRANT/LOSS)**

.. code-block:: cpp

	auto OnMonitroingAccessControlCB = [](const MONITORING_ACCESS_CONTROL access) {
		std::cout << "[OnMonitroingAccessControlCB] Control Access : " << to_str(access) << std::endl;
		if(MONITORING_ACCESS_CONTROL_GRANT == access) {
			get_control_access = true;
			std::cout << "Got Control Access !! " << std::endl;
		}
		if(MONITORING_ACCESS_CONTROL_LOSS == access) {
			get_control_access = false;
		}
	};
	robot.set_on_monitoring_access_control(OnMonitroingAccessControlCB);

The OnMonitoringStateCallback monitors for **robot state**.
This callback is invoked whenever the robot state changes (for example,  
``STATE_SAFE_OFF``, ``STATE_STANDBY``, ``STATE_MOVING``).

.. code-block:: cpp

	auto OnMonitoringStateCB = [] (const ROBOT_STATE state) {
		std::cout << "[OnMonitoringStateCB] Robot State : " << to_str(state) << std::endl;
		if(STATE_STANDBY == state) {
			is_standby = true;
			std::cout << "Successfully Servo on !! " << std::endl;
		}else {
			is_standby = false;
		}
	};
	robot.set_on_monitoring_state(OnMonitoringStateCB);

You can confirm that the callbacks are set correctly by checking the console output when the program runs.

.. code-block:: text

   [OnMonitoringStateCB] Robot State : STATE_SAFE_OFF
   [OnMonitoringStateCB] Robot State : STATE_STANDBY
   Successfully Servo on !!
   [OnMonitoringStateCB] Robot State : STATE_MOVING
   [OnMonitoringStateCB] Robot State : STATE_STANDBY

Connection & Version Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After registering callbacks, the sample opens the connection and prints controller version info.

- ``open_connection`` must succeed before any other API can be used.  
- ``setup_monitoring_version(1)`` selects the newer monitoring context to avoid using deprecated callbacks.  
- ``get_system_version`` confirms which DRCF build you are connected to.

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
   Library version: GL013300

Access control & STANDBY
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This loop attempts up to 10 times (with a 1-second delay between iterations) to.

- Request **control authority** using ``ManageAccessControl(MANAGE_ACCESS_CONTROL_FORCE_REQUEST)`` until ``get_control_access`` becomes ``true``.
- Turn **Servo On** with ``set_robot_control(CONTROL_SERVO_ON)`` until ``is_standby`` becomes ``true``.

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

Robot Mode Confiuguration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the robot has control authority and is in STANDBY, the system and mode are configured:

.. code-block:: cpp

	if(!robot.set_robot_mode(ROBOT_MODE_AUTONOMOUS)) {
		return 1;
	}

``set_robot_mode(ROBOT_MODE_AUTONOMOUS)`` is required before executing motion from an external program. (Configuration is usually done in **MANUAL** mode, while actual motion is run in **AUTONOMOUS** mode.)

Motion Execution
~~~~~~~~~~~~~~~~~~~~~

If everything is ready, the program waits for user input and then performs a simple motion.

.. code-block:: cpp

   std::cout << "Press Enter to continue...";
   std::cin.get();  // Waits for user to press Enter

   float targetPos[6] = {0., 0., 30., 0., 0., 0.};
   float targetVel = 50;
   float targetAcc = 50;

   robot.movej(targetPos, targetVel, targetAcc);  // move +30 deg on joint 3

   targetPos[2] = 0;
   robot.movej(targetPos, targetVel, targetAcc);  // move back to 0 deg

   robot.close_connection();
   return 0;

The motion sequence is: |br|
Wait for the user to press **Enter** -> Execute a **joint move** with +30° on joint 3 -> Move joint 3 back to 0° -> Close the controller connection.

You can confirm the state callback by checking the console output when the program runs.

.. code-block:: text

   [OnMonitoringStateCB] Robot State : STATE_MOVING
   [OnMonitoringStateCB] Robot State : STATE_STANDBY
   Successfully Servo on !!

These logs confirm that motion started correctly (MOVING), and the robot safely returned to STANDBY after motion.