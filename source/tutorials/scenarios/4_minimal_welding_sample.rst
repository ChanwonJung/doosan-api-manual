6.6.4 **minimal_welding_sample.cpp**
-------------------------------------------
This example (``4_minimal_welding_sample.cpp``) demonstrates how to configure and execute a
digital welding process over EtherNet/IP using the Doosan Robotics API:

- register monitoring / alarm / access control callbacks
- open a TCP/IP connection and request control authority
- turn Servo On and verify system/library versions
- switch to AUTONOMOUS + REAL mode
- execute a full DRL-based welding sequence
- configure the welding interface and motion purely via C++ API and run a weave weld

.. note::

  This sample is implemented for DRCF_VERSION 2.
  Welding-related APIs are not available yet when building with DRCF_VERSION 3.
  Support for welding under DRCF v3 will be provided in a future update.

This example is located in the following path: |br|
``API-DRFL/example/Linux_64/4_minimal_welding_sample.cpp``

See the example on the `Doosan Robotics API-DRFL GitHub <https://github.com/DoosanRobotics/API-DRFL/blob/GL013300/example/Linux_64/4_minimal_welding_sample.cpp>`_.

Setup & Global Variables
~~~~~~~~~~~~~~~~~~~~~~~~

The sample defines a global controller object, several state flags,  
and a helper function that returns a DRL welding script as a string.

.. code-block:: cpp

   #define DRCF_VERSION 2

   #include <iostream>
   #include <cstring>
   #include <thread>
   #include <chrono>
   #include <termios.h>
   #include <unistd.h>

   #include "../../include/DRFLEx.h"
   using namespace DRAFramework;
   using namespace std::chrono_literals;

   #undef NDEBUG
   #include <assert.h>
 
   CDRFLEx Drfl;
   bool g_bHasControlAuthority = FALSE;
   bool g_TpInitailizingComplted = FALSE;
   bool moving = FALSE;
   bool bAlterFlag = FALSE;
   bool is_standby = FALSE;

   std::string IP_ADDR = "192.168.137.100";
   std::string getWeldingSampleDrl();

A set of callback handlers is declared to react to TP initialization,  
homing completion, alarms, popups, TP logs, user input, real-time monitoring data,  
and disconnection events.

.. code-block:: cpp

   void OnTpInitializingCompleted();
   void OnHommingCompleted();
   void OnProgramStopped(const PROGRAM_STOP_CAUSE v);
   void OnMonitoringDataCB(const LPMONITORING_DATA pData);
   void OnMonitoringDataExCB(const LPMONITORING_DATA_EX pData);
   void OnMonitoringCtrlIOCB(const LPMONITORING_CTRLIO pData);
   void OnMonitoringCtrlIOExCB(const LPMONITORING_CTRLIO_EX2 pData);
   void OnMonitoringStateCB(const ROBOT_STATE eState);
   void OnMonitroingAccessControlCB(const MONITORING_ACCESS_CONTROL transit);
   void OnLogAlarm(LPLOG_ALARM tLog);
   void OnTpPopup(LPMESSAGE_POPUP tPopup);
   void OnTpLog(const char* strLog);
   void OnTpProgress(LPMESSAGE_PROGRESS tProgress);
   void OnTpGetuserInput(LPMESSAGE_INPUT tInput);
   void OnRTMonitoringData(LPRT_OUTPUT_DATA_LIST tData);
   void OnDisConnected();

These globals and callbacks are used to maintain **control authority** and **Servo On** state, automatically reconnect on network loss, log alarm and popup messages from the controller, and feed welding status back to the user during execution.

Main Loop
~~~~~~~~~~~~~

The main loop runs after initialization and waits for a single-character command.

.. code-block:: cpp

   while (true) {
     std::cout << "\ninput key : ";
     char ch;
     std::cin >> ch;

     if (ch == 'q') {
       std::cout << "Exit program..." << std::endl;
       break;   // exit while loop
     }

     switch (ch) {
       case '0':
       {
         // DRL welding sample
         Drfl.drl_start(ROBOT_SYSTEM_REAL, getWeldingSampleDrl());
       }
       break;

       case '1':
       {
         // C++ welding interface + motion sample
         // (configure EtherNet/IP mapping and execute welding motion)
         // ...
       }
       break;

       case '2':
       {
         // Reserved for additional welding tests
       }
       break;

       default:
         break;
     }
   }

   Drfl.CloseConnection();
   return 0;

- ``q`` : gracefully stop the sample and close the connection.
- ``0`` : run the **DRL-based welding script** returned by ``getWeldingSampleDrl()``.
- ``1`` : configure the welding interface directly via **C++ structures**  
  and execute a **weaving welding motion** using ``amovel`` with a welding app type.
- ``2`` : reserved for future extensions.

Callback Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike the minimal instruction example (where callbacks are registered on a key press),  
this welding sample registers all callbacks **at startup** before opening the connection.

.. code-block:: cpp

   int main(int argc, char** argv) {

     Drfl.set_on_homming_completed(OnHommingCompleted);
     Drfl.set_on_monitoring_data(OnMonitoringDataCB);
     Drfl.set_on_monitoring_data_ex(OnMonitoringDataExCB);
     Drfl.set_on_monitoring_ctrl_io(OnMonitoringCtrlIOCB);
     // Drfl.set_on_monitoring_ctrl_io_ex(OnMonitoringCtrlIOExCB);
     Drfl.set_on_monitoring_state(OnMonitoringStateCB);
     Drfl.set_on_monitoring_access_control(OnMonitroingAccessControlCB);
     Drfl.set_on_tp_initializing_completed(OnTpInitializingCompleted);
     Drfl.set_on_log_alarm(OnLogAlarm);
     Drfl.set_on_tp_popup(OnTpPopup);
     Drfl.set_on_tp_log(OnTpLog);
     Drfl.set_on_tp_progress(OnTpProgress);
     Drfl.set_on_tp_get_user_input(OnTpGetuserInput);
     Drfl.set_on_rt_monitoring_data(OnRTMonitoringData);
     Drfl.set_on_program_stopped(OnProgramStopped);
     Drfl.set_on_disconnected(OnDisConnected);

     assert(Drfl.open_connection(IP_ADDR));
     // ...
   }

- ``OnMonitoringStateCB`` sets ``is_standby`` when the robot reaches **STATE_STANDBY**,  
  which indicates that **Servo On** is complete.
- ``OnMonitroingAccessControlCB`` tracks whether control authority is **GRANT / LOSS / DENY**.
- ``OnTpInitializingCompleted`` immediately issues a **force request** for control authority.
- ``OnLogAlarm``, ``OnTpPopup``, ``OnTpLog`` print diagnostic information to the console.
- ``OnDisConnected`` retries ``open_connection()`` in a loop to restore connectivity.

The access control callback is used to update ``g_bHasControlAuthority`` whenever the
controller changes the access state.

.. code-block:: cpp

   void OnMonitroingAccessControlCB(const MONITORING_ACCESS_CONTROL transit) {
     std::cout << "[AccessControl] state = " << int(transit) << std::endl;

     switch (transit) {
       case MONITORING_ACCESS_CONTROL_GRANT:
         // State where control authority is granted
         g_bHasControlAuthority = true;
         break;
       case MONITORING_ACCESS_CONTROL_LOSS:
       case MONITORING_ACCESS_CONTROL_DENY:
         // State where control authority is lost or denied
         g_bHasControlAuthority = false;
         break;
       default:
         break;
     }
   }

When the access-control state changes, the callback prints the numeric value of
``MONITORING_ACCESS_CONTROL``.

.. code-block:: text

   [AccessControl] state = 0

Different integer values correspond to the enum constants defined in
``MONITORING_ACCESS_CONTROL`` (REQUEST, GRANT, DENY, LOSS, ...).  

The robot-state callback is responsible for detecting when the robot reaches
the **standby** state after Servo On.

.. code-block:: cpp

  void OnMonitoringStateCB(const ROBOT_STATE eState) 
  {
    if (eState == STATE_STANDBY) {
      is_standby = true;
      std::cout << "Successfully Servo On !!" << std::endl;} 
    else 
    {
      is_standby = false;
    }
  }

If the controller reports ``STATE_STANDBY``, the sample sets ``is_standby = true`` and
prints a confirmation message.

.. code-block:: text

  Successfully Servo On !!

The main loop later checks ``is_standby`` together with
``g_bHasControlAuthority`` to confirm that the system is ready for welding.

Alarm information from the controller is reported through the log-alarm callback.

.. code-block:: cpp

  void OnLogAlarm(LPLOG_ALARM tLog) {
  cout << "Alarm Info: "
       << "group(" << (unsigned int)tLog->_iGroup << "), index("
       << tLog->_iIndex << "), param(" << tLog->_szParam[0] << "), param("
       << tLog->_szParam[1] << "), param(" << tLog->_szParam[2] << ")" << endl;
  }

Example output:

.. code-block:: text

  Alarm Info: group(1), index(1037), param(), param(), param()

Each alarm is logged with a **group** and **index** code plus up to three
string parameters. These values can be cross-referenced with the alarm table
in the controller manual to identify the exact cause (e.g., Servo On failure,
limit violation, welding interface error, etc.).  

Connection to Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After registering callbacks, the controller connection is opened via TCP/IP.

.. code-block:: cpp

   assert(Drfl.open_connection(IP_ADDR));

   Drfl.setup_monitoring_version(1); // (0 -> older version, 1 -> latest)

   SYSTEM_VERSION tSysVerion = {'\0',};
   Drfl.get_system_version(&tSysVerion);


Control Authority & Servo On Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample implements a robust loop to obtain control authority and turn Servo On.

.. code-block:: cpp

   // 1) Retry requesting access + Servo ON up to 10 times
   for (size_t retry = 0; retry < 10;
        ++retry, std::this_thread::sleep_for(std::chrono::milliseconds(1000))) {

     if (!g_bHasControlAuthority) {
       // Force request for control authority
       Drfl.ManageAccessControl(MANAGE_ACCESS_CONTROL_FORCE_REQUEST);
       continue;
     }

     if (!is_standby) {
       // Try Servo ON
       Drfl.set_robot_control(CONTROL_SERVO_ON);
       continue;
     }

     if (g_bHasControlAuthority && is_standby)
       break;
   }

   // 2) State Check
   if (!(g_bHasControlAuthority && is_standby)) {
     std::cout << "Failed to reach GRANT + STANDBY state" << std::endl;
     Drfl.CloseConnection();
     return 1;
   }

   std::cout << "System version: " << tSysVerion._szController << std::endl;
   std::cout << "Library version: " << Drfl.get_library_version() << std::endl;


.. code-block:: text

   System version: GF03050000
   Library version: GL013300

Together with ``OnMonitoringStateCB``, this guarantees that **Servo On** only proceeds  
once the controller has granted access and the robot state reaches **STANDBY**.


Robot Mode & System Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After Servo On, the robot mode and system are configured for welding.

.. code-block:: cpp

   std::cout << "set robot mode ret : "
             << Drfl.set_robot_mode(ROBOT_MODE_AUTONOMOUS) << std::endl;

   Drfl.set_robot_system(ROBOT_SYSTEM_REAL);

.. code-block:: text

   set robot mode ret : 1

DRL-based Welding Script
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Key ``0`` executes a self-contained DRL script returned by ``getWeldingSampleDrl()``.

.. code-block:: cpp

   case '0':
   {
     // DRL welding sample
     Drfl.drl_start(ROBOT_SYSTEM_REAL, getWeldingSampleDrl());
   }
   break;

The DRL string configures welding parameters and motions:

.. code-block:: cpp

   std::string getWeldingSampleDrl() {
     return R"(
   set_singular_handling(DR_AVOID)
   set_velj(60.0)
   set_accj(100.0)
   set_velx(250.0, 80.625)
   set_accx(1000.0, 322.5)

   dry_run = 1 
   weld_con_adj = 1 
   arc_sensing_test = False 

   app_weld_set_interface_eip_r2m_process(welding_start=[1,0,0,0,4,0,1,0,0],
                                          robot_ready=[1,0,0,0,5,0,1,0,0],
                                          error_reset=[1,0,0,1,4,0,1,0,0])
   app_weld_set_interface_eip_r2m_mode(...)
   app_weld_set_interface_eip_r2m_test(...)
   app_weld_set_interface_eip_r2m_condition(...)
   app_weld_set_interface_eip_r2m_option(...)
   app_weld_set_interface_eip_m2r_process(...)
   app_weld_set_interface_eip_m2r_monitoring(...)
   app_weld_set_interface_eip_m2r_other(...)

   wait(0.5)

   app_weld_enable_digital()
   wait(1)

   app_weld_set_weld_cond_digital(flag_dry_run=dry_run, vel_target=3.0000,
                                  vel_min=0.1000, vel_max=100.0000,
                                  welding_mode=1, s_2t=0, pulse_mode=0,
                                  wm_opt1=0, simulation=0,
                                  ts_opt1=0, ts_opt2=0,
                                  job_num=4, synergic_id=1, ...)

   app_weld_weave_cond_trapezoidal(wv_offset=[0.000,0.000], wv_ang=0.00,
                                   wv_param=[0.000,3.0,0.000,-3.0,
                                             0.30,0.10,0.20,0.30,0.10,0.20])

   ready_weld_pos = posx(-77.41, -640.26, 119.09, 54.84, 166.79, -48.59 )
   movel(ready_weld_pos, radius=0.00, ref=0, mod=DR_MV_MOD_ABS,
         ra=DR_MV_RA_DUPLICATE, app_type=DR_MV_APP_NONE)
   wait(1)

   end_weld_pos = posx(306.16,-617.1,173.77,54.18,166.75,-49.15)
   amovel(end_weld_pos, v=3.0000, a=70.0000, ref=0, mod=DR_MV_MOD_ABS,
          ra=DR_MV_RA_DUPLICATE, app_type=DR_MV_APP_WELD)
   tp_log("Start welding motion")
   mwait(1)
   app_weld_disable_digital()

   wait(1))";
   }

- Configure **EtherNet/IP mapping** (R2M / M2R) for welding control and monitoring.
- Enable the **digital welding interface** (``app_weld_enable_digital()``).
- Set welding conditions (speed, mode, job number, synergic ID, etc.).
- Configure **trapezoidal weaving** for the torch path.
- Move to a ready pose via ``movel``, then weld from **start** to **end** pose  
  using ``amovel(..., app_type=DR_MV_APP_WELD)``.
- Disable welding at the end of the motion.

By default, ``dry_run = 1`` performs a **simulation weld** (no real arc).  
To perform real welding, users must set ``dry_run = 0`` and ensure  
that the welding machine and EtherNet/IP mapping are configured correctly.

C++-based Welding Interface Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Key ``1`` demonstrates how to set up the same welding interface **purely via C++**  
and execute a welding motion without using DRL welding commands directly.

.. code-block:: cpp

   case '1':
   {
     // 1) Move to ready joint position and get current task pose
     float ready_weld_posj[6] = {85.8353, -53.5421, -61.888, 6.7839, -76.0373, -19.6588};
     Drfl.movej(ready_weld_posj, 50, 50);

     LPROBOT_TASK_POSE posx = Drfl.get_current_posx();
     float target_wel_posx[6];
     for (int i = 0; i < NUM_JOINT; i++) {
       target_wel_posx[i] = posx->_fTargetPos[i];
     }
     target_wel_posx[0] += 200;  // shift X by +200 mm

     // 2) Basic welding options
     Drfl.set_singularity_handling(SINGULARITY_AVOIDANCE_AVOID);
     unsigned char dry_run = 1;       // 0: real weld, 1: dry-run
     unsigned char weld_con_adj = 1;  // use preset welding condition

     Drfl.set_robot_mode(ROBOT_MODE_AUTONOMOUS);

     // 3) Ensure the welding TCP is selected
     if (Drfl.get_tcp() != "Welding Torch")
       Drfl.set_tcp("Welding Torch");
     std::this_thread::sleep_for(200ms);

     // 4) Configure EtherNet/IP R2M & M2R interface structures
     CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS    r2m_process_data    = { /* ... */ };
     CONFIG_DIGITAL_WELDING_INTERFACE_MODE       r2m_mode_data       = { /* ... */ };
     CONFIG_DIGITAL_WELDING_INTERFACE_TEST       r2m_test_data       = { /* ... */ };
     CONFIG_DIGITAL_WELDING_INTERFACE_CONDITION  r2m_condition_data  = { /* ... */ };
     CONFIG_DIGITAL_WELDING_INTERFACE_OPTION     r2m_option_data     = { /* ... */ };
     CONFIG_DIGITAL_WELDING_INTERFACE_PROCESS2   m2r_process2_data   = { /* ... */ };
     CONFIG_DIGITAL_WELDING_INTERFACE_MONITORING m2r_monitoring_data = { /* ... */ };
     CONFIG_DIGITAL_WELDING_INTERFACE_OTHER      m2r_other_data      = { /* ... */ };

     Drfl.app_weld_set_interface_eip_r2m_process    (r2m_process_data);
     Drfl.app_weld_set_interface_eip_r2m_mode       (r2m_mode_data);
     Drfl.app_weld_set_interface_eip_r2m_test       (r2m_test_data);
     Drfl.app_weld_set_interface_eip_r2m_condition  (r2m_condition_data);
     Drfl.app_weld_set_interface_eip_r2m_option     (r2m_option_data);
     Drfl.app_weld_set_interface_eip_m2r_process2   (m2r_process2_data);
     Drfl.app_weld_set_interface_eip_m2r_monitoring (m2r_monitoring_data);
     Drfl.app_weld_set_interface_eip_m2r_other      (m2r_other_data);

     // 5) Enable digital welding & set welding condition
     std::this_thread::sleep_for(500ms);
     Drfl.app_weld_enable_digital(1);
     std::this_thread::sleep_for(500ms);

     CONFIG_DIGITAL_WELDING_CONDITION weld_condition = { 0, };
     weld_condition._cVirtualWelding = dry_run;
     weld_condition._fTargetVel      = 3.f;
     weld_condition._fMaxVelLimit    = 100.f;
     weld_condition._nWeldingMode    = 1;
     weld_condition._nPulseMode      = 0;
     weld_condition._nJobNumber      = 4;
     weld_condition._nSynergicID     = 1;
     Drfl.app_weld_set_weld_cond_digital(weld_condition);

     std::this_thread::sleep_for(1000ms);

     // 6) Configure trapezoidal weaving
     CONFIG_TRAPEZOID_WEAVING_SETTING weaving_trap = {
       0.f, 0.f, 0.f,
       {0.f, 3.f}, {0.f, -3.f},
       0.3f, 0.1f, 0.2f,
       0.3f, 0.1f, 0.2f
     };
     Drfl.app_weld_weave_cond_trapezoidal(weaving_trap);

     // 7) Execute welding motion with welding application type
     float welding_velx[2] = { 3, 3 };
     float welding_accx[2] = { 70, 70 };
     Drfl.amovel(
       target_wel_posx,
       welding_velx, welding_accx,
       0,
       MOVE_MODE_ABSOLUTE,
       MOVE_REFERENCE_BASE,
       BLENDING_SPEED_TYPE_DUPLICATE,
       DR_MV_APP_WELD);

     Drfl.mwait();
   }
   break;

- **Task pose offset**: the welding target is defined as the current pose plus an X-offset,  
  making it easy to shift the weld line relative to the current TCP position.
- **Digital welding interface mapping** is done with a series of  
  ``CONFIG_DIGITAL_WELDING_INTERFACE_*`` structures, matching the DRL sample configuration.
- **Weaving parameters** (offsets, amplitude, timing) are configured through  
  ``CONFIG_TRAPEZOID_WEAVING_SETTING`` and applied via  
  ``app_weld_weave_cond_trapezoidal``.
- The final motion uses ``amovel(..., DR_MV_APP_WELD)``, which executes  
  a **linear weld with weaving** along the specified target pose.