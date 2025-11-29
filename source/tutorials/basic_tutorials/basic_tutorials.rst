.. _tutorials_basic:

6.2 Basic Tutorials
===================

The **Basic Tutorials** section provides simple, self-contained examples  
to help users understand and verify the **fundamental operations** of the Doosan Robotics API.  
Each topic focuses on one essential function — such as establishing connection,  
enabling servos, performing basic motions, or running a short DRL script —  
allowing users to confirm correct API behavior step by step before moving on to advanced control.

These examples are intentionally minimal and demonstrate the **core command flow**  
without additional logic or threading.  
For complete scenario-based examples, refer to :ref:`6.6 Scenario-based Examples <tutorials_scenarios>`.

**Tutorial Flow**

1. **Connection & Callback Registration** – Connect to the robot controller and set up monitoring callbacks.  
2. **Access Control & ServoOn** – Obtain control authority and enable servo motors.  
3. **Jog & Home** – Verify joint-level and homing motions.  
4. **MoveJ / MoveL (Sync & Async)** – Execute basic motion primitives.  
5. **DRL Mini Loop** – Run and stop a simple DRL script safely.  
6. **I/O Basics** – Test digital output toggling on the control box.

Each subsection below contains a concise code snippet and key verification point.

---------------------------------------
Connection & Callback Registration
---------------------------------------

**Purpose**  |br|
Connect to the controller and register monitoring callbacks to receive robot state updates and alarms.

.. code-block:: cpp

   Drfl.set_on_monitoring_state(OnMonitoringStateCB);
   Drfl.set_on_monitoring_access_control(OnMonitroingAccessControlCB);
   Drfl.set_on_log_alarm(OnLogAlarm);
   Drfl.set_on_monitoring_data(OnMonitoringDataCB);
   Drfl.set_on_monitoring_data_ex(OnMonitoringDataExCB);

   assert(Drfl.open_connection("192.168.137.100"));

   SYSTEM_VERSION ver{};
   Drfl.get_system_version(&ver);
   std::cout << "System: "  << ver._szController << "\\n";
   std::cout << "Library: " << Drfl.get_library_version() << "\\n";

**Check** |br| 
Connection succeeds and callbacks respond to robot events such as state or alarm updates.

---------------------------------------
Access Control & ServoOn
---------------------------------------

**Purpose**  |br|
Acquire control authority and activate the robot’s servo motors.

.. code-block:: cpp

   void OnTpInitializingCompleted() {
       Drfl.ManageAccessControl(MANAGE_ACCESS_CONTROL_FORCE_REQUEST);
   }

   // After GRANT:
   assert(Drfl.set_robot_mode(ROBOT_MODE_AUTONOMOUS));
   assert(Drfl.set_robot_system(ROBOT_SYSTEM_REAL));
   Drfl.set_robot_control(CONTROL_SERVO_ON);

**Check** |br| 
Control authority is granted, the robot state transitions to **STANDBY**,  
and ServoOn completes without alarms.

---------------------------------------
Jog & Home
---------------------------------------

**Purpose** |br| 
Verify motion control by performing a short jog and homing sequence.

.. code-block:: cpp

   // Jog example
   Drfl.Jog(JOG_AXIS_JOINT_1, MOVE_REFERENCE_BASE, 0.0f); // stop jog
   // Home example
   Drfl.Home((unsigned char)0);

**Check** |br|
Jog and Home operations execute normally without triggering safety stops.

---------------------------------------
MoveJ / MoveL (Sync / Async)
---------------------------------------

**Purpose** |br| 
Test basic motion primitives in joint and Cartesian space,  
and verify the stop function under asynchronous control.

.. code-block:: cpp

   // Example: small incremental motion
   // Drfl.MoveJ(targetJ, vel, acc);      // Sync
   // Drfl.MoveL(targetX, vel, acc);      // Sync

   // Async execution and stop
   // Drfl.MoveJAsync(targetJ, vel, acc);
   Drfl.MoveStop(STOP_TYPE_SLOW);

**Check** |br| 
Motions execute successfully and stop safely when commanded.

---------------------------------------
DRL Mini Loop (Start / Stop)
---------------------------------------

**Purpose** |br| 
Run a simple DRL script and confirm that it executes and stops safely.

.. code-block:: cpp

   const std::string drl =
       "loop = 0\\n"
       "while loop < 3:\\n"
       "  movej(posj(10,10,10,10,10,10), vel=30, acc=30)\\n"
       "  movej(posj(0,0,0,0,0,0),       vel=30, acc=30)\\n"
       "  loop += 1\\n";

   // Start DRL
   // Drfl.PlayDrlStart(drl.c_str());

   // Safe stop
   Drfl.PlayDrlStop(STOP_TYPE_SLOW);
   Drfl.mwait();   // wait for controller acknowledgment

**Check** |br| 
The DRL loop runs for the specified iterations or stops safely upon command.

---------------------------------------
I/O Basics (Control Box DO)
---------------------------------------

**Purpose** |br|
Toggle a digital output on the control box to verify basic I/O operation.

.. code-block:: cpp

   Drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_10, TRUE);
   std::this_thread::sleep_for(std::chrono::seconds(1));
   Drfl.set_digital_output(GPIO_CTRLBOX_DIGITAL_INDEX_10, FALSE);

**Check** |br|
The digital output toggles correctly (verified via indicator lamp, relay, or tester).

.. note::
   The examples in this section are simplified demonstrations of each core API.  
   For complete scenario-based examples integrating multiple features,  
   refer to :ref:`6.6 Scenario-based Examples <tutorials_scenarios>`.
