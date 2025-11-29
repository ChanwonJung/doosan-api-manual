.. _tutorials_advanced:

6.3 Advanced Tutorials
===============================

The **Advanced Tutorials** section covers practical and safety-critical control patterns  
for real robot operation.  
These examples extend beyond the basic API flow to include **pause/resume logic**,  
**safety stop recovery**, **alarm handling**, and **custom motion planning**.

Each example focuses on safe transition management and recovery from real-world conditions  
such as emergency stops, access loss, or servo-off states.

**Tutorial Flow**

1. **Unified Stop / Pause / Resume** – Safely interrupt and resume robot motions.  
2. **Safety Stop & Recovery** – Handle safety stop states and restore operation.  
3. **Alarm & Access Loss Handling** – Manage alarms and access control interruptions.  
4. **Monitoring & Logging** – Retrieve and interpret detailed monitoring data.  
5. **Custom Trajectory Planning** – Generate and follow a 5th-order polynomial trajectory.  
6. **Servo Off & Reconnection** – Reconnect and restore servo after network loss.

---------------------------------------
Unified Stop / Pause / Resume
---------------------------------------

**Purpose** |br|
Demonstrate a unified pattern for stopping, pausing, and resuming motions,  
covering both API and DRL execution.

.. code-block:: cpp

   // Keyboard-based control thread example
   while (true) {
       char ch = getch();
       switch (ch) {
           case 's':   // stop
               Drfl.MoveStop(STOP_TYPE_SLOW);
               Drfl.PlayDrlStop(STOP_TYPE_SLOW);
               break;
           case 'p':   // pause
               Drfl.MovePause();
               break;
           case 'r':   // resume
               Drfl.MoveResume();
               break;
       }
       std::this_thread::sleep_for(std::chrono::milliseconds(100));
   }

**Check** |br|  
The robot stops or pauses smoothly,  
and resumes motion without triggering safety errors.

---------------------------------------
Safety Stop & Recovery
---------------------------------------

**Purpose** |br| 
Handle transitions from safety stop states and restore normal operation automatically.

.. code-block:: cpp

   void OnMonitoringStateCB(const ROBOT_STATE eState) {
       switch (eState) {
           case STATE_SAFE_STOP:
               Drfl.SetSafeStopResetType(SAFE_STOP_RESET_TYPE_DEFAULT);
               Drfl.SetRobotControl(CONTROL_RESET_SAFET_STOP);
               break;
           case STATE_SAFE_OFF:
               Drfl.SetRobotControl(CONTROL_SERVO_ON);
               break;
           case STATE_SAFE_STOP2:
               Drfl.SetRobotControl(CONTROL_RECOVERY_SAFE_STOP);
               break;
           case STATE_SAFE_OFF2:
               Drfl.SetRobotControl(CONTROL_RECOVERY_SAFE_OFF);
               break;
           default:
               break;
       }
   }

**Check** |br| 
The robot automatically recovers from safety stop or servo-off states  
and returns to STANDBY.

---------------------------------------
Alarm & Access Loss Handling
---------------------------------------

**Purpose** |br| 
Respond to controller alarms and loss of access authority dynamically.

.. code-block:: cpp

   void OnLogAlarm(LPLOG_ALARM tLog) {
       std::cout << "Alarm Group: " << (int)tLog->_iGroup
                 << ", Index: " << (int)tLog->_iIndex << std::endl;
   }

   void OnMonitoringAccessControlCB(const MONITORING_ACCESS_CONTROL eControl) {
       switch (eControl) {
           case MONITORING_ACCESS_CONTROL_REQUEST:
               Drfl.ManageAccessControl(MANAGE_ACCESS_CONTROL_RESPONSE_NO);
               break;
           case MONITORING_ACCESS_CONTROL_GRANT:
               g_bHasControlAuthority = TRUE;
               break;
           case MONITORING_ACCESS_CONTROL_LOSS:
               g_bHasControlAuthority = FALSE;
               Drfl.ManageAccessControl(MANAGE_ACCESS_CONTROL_FORCE_REQUEST);
               break;
           default:
               break;
       }
   }

**Check**  |br|
The system prints alarm information and automatically regains control after access loss.

---------------------------------------
Monitoring & Logging
---------------------------------------

**Purpose** |br| 
Access detailed real-time monitoring data and log robot parameters.

.. code-block:: cpp

   void OnMonitoringDataExCB(const LPMONITORING_DATA_EX pData) {
       std::cout << "TCP Target Position: ["
                 << pData->_tCtrl._tWorld._fTargetPos[0] << ", "
                 << pData->_tCtrl._tWorld._fTargetPos[1] << ", "
                 << pData->_tCtrl._tWorld._fTargetPos[2] << "]"
                 << std::endl;
   }

**Check** |br| 
Real-time position or state values update periodically during motion.

---------------------------------------
Custom Trajectory Planning
---------------------------------------

**Purpose** |br| 
Demonstrate a user-defined trajectory generation using a 5th-order polynomial.  
This technique is useful for smooth joint trajectories or offline simulation.

.. code-block:: cpp

   struct PlanParam {
       float time;
       float ps[6], vs[6], as[6];
       float pf[6], vf[6], af[6];
       float A0[6], A1[6], A2[6], A3[6], A4[6], A5[6];
   };

   void TrajectoryPlan(PlanParam* plan) {
       float tf = plan->time;
       for (int i = 0; i < 6; i++) {
           plan->A0[i] = plan->ps[i];
           plan->A1[i] = plan->vs[i];
           plan->A2[i] = plan->as[i] / 2;
           plan->A3[i] = (20*plan->pf[i] - 20*plan->ps[i]
                        - (8*plan->vf[i] + 12*plan->vs[i]) * tf
                        - (3*plan->as[i] - plan->af[i]) * tf * tf) / (2 * tf * tf * tf);
       }
   }

**Check** |br| 
Generated coefficients produce continuous position, velocity, and acceleration profiles.

---------------------------------------
Servo Off & Reconnection
---------------------------------------

**Purpose**  |br|
Automatically reconnect to the controller after network loss or servo-off conditions.

.. code-block:: cpp

   void OnDisconnected() {
       while (!Drfl.open_connection("192.168.137.100")) {
           std::this_thread::sleep_for(std::chrono::seconds(1));
       }
   }

**Check** |br| 
Connection is re-established automatically after disconnection,  
and control can resume without rebooting the robot.

.. note::
   Advanced control techniques require that the basic API flow from :ref:`6.2 Basic Tutorials <tutorials_basic>`  
   is already configured and tested successfully.
