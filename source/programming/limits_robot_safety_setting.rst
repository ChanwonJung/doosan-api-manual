5.8 Limits on Robot Safety Setting Function
============================================

Setting functions related to robot motion (TOOL, TCP, etc.) and safety (safety area, safety stop, 
safety I/O, etc.) are not provided by this API. They should be set directly in the T/P application. 
As the initialization process is limited to being executed only in the T/P application during the 
booting of the robot controller, the robot safety setting must be made in the T/P application.

As an exception, the setting of TOOL or TCP, which are used in motion control commands, is 
provided as an API function, but this is not interworked with the T/P application. This requires 
reregistration for use during the rebooting of the robot controller or reoperation of the program. 
Therefore, using it after setting in the T/P application is recommended.

With respect to this, robot setting is possible only in the following robot pause states: 
STATE_INITIALIZING, STATE_STANDBY, STATE_SAFE_OFF, and STATE_EMERGENCY. 
If setting is tried in a state other than these, errors occur and robot motion stops. 
And a subsequent log and alarm message are generated in the callback function (TOnLogAlarmCB).