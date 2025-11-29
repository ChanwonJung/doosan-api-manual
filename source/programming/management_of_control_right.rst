5.3 Management of Control Right
=======================================

As the robot controller is configured to be controlled only in one application, the logic related 
to the acquisition and transfer of control right should be realized in the user application using 
the ManageAccessControl(=manage_access_control) function and TOnChangingAccessControlCB callback function, 
which are related to control right, after the completion of robot initialization, and control commands 
should be conveyed only when the control right is possessed. When control commands are conveyed without 
control right, all control commands are ignored and not processed.