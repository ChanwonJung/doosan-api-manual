5.4 Robot Operation Mode
==============================

The robot controller operation mode supports automatic mode and manual mode, 
and the Set/Getrobotmode function allows you to check the settings and modes.. 
Automatic mode is used for automatically executing the program composed in DRL, 
a robot programming language our company provides, and manual mode is for executing 
a single action (e.g., jog action) for which the TCP velocity of the edge of the 
robot is restricted to 250 mm/sec for safety. 

Regarding this, when the movej command, 
which is a robot motion control function for joint space, needs to be set by manual mode 
and controlled at maximum speed, overspeed can occur and robot operation can stop. 
Therefore, caution should be paid when setting the operation mode.