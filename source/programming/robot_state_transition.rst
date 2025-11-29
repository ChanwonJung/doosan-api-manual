5.6 Robot state transition
==============================

The command standby state (STATE_STANDBY) is a basic robot control preparation state, and 
it carries out motions by automatically converting into STATE_HOMING, STATE_MOVING, or 
STATE_TEACHING when a control command is received from the user, and if the motion is 
done without error, it converts again into STATE_STANDBY and waits for user commands.

The EMERGENCY_STOP state is converted by the E/M button in whatever states excluding the 
initialization state (STATE_INITIALIZING) and robot stops. When an internal function or motion 
error of the robot controller occurs, it is converted into the SAFE_OFF state (motor and brake 
power cut-off) or SAFE_STOP state (control stop) and the robot stops.

Also, the functions for which state should be converted directly by the user for safety are as 
follows, and these functions can be executed by the set_robot_control function.