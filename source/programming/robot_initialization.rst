5.2 Robot Initialization
==============================

As the robot controller receives and processes various information needed for robot operation 
through the initialization of the T/P application, the user application composed by using 
this API must start robot control after checking whether initialization has been completed 
in the information on robot operation state. 

The completion of initialization can be checked 
through TOnMonitoringStateCB, which is a callback function, or get_robot_state, which is a 
user call function, when connecting normally by using robot connection-related functions.