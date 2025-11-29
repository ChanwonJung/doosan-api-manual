5.5 Robot Operation State
==============================

The operation state information of the robot has a total of 15 states as follows, and all states 
excluding reservation use (Nos. 11 ~ 14) can be checked through the OnMonitoringState 
callback function or get_robot_state, which is a user call function.