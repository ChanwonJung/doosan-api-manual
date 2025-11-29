5.1 Robot Connection/Release
==============================

As the robot controller and this API are connected through TCP/IP communication, 
a connection establishment process is necessary. As normal connection is not possible 
when connection is tried with other APIs or socket-related functions because the certification process 
is included in the internal connection process, the connection-related functions of this API must be used.

Also, when two or more robot controllers are used for one network, the IP address of each robot controller 
shall be changed so that it does not overlap at the T/P application and the connection process shall be executed 
in each robot controller for normal control.

And as this API uses TCP/IIP communication, performance decline or functional error of the user application 
can occur depending on the computer performance or the network load.