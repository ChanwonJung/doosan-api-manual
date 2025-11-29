.. _tutorials_operation_modes:

6.1 Operation Modes
===================================


This section explains the **operational modes** of the Doosan Robot Controller,  
which determine how the robot interacts with users and executes commands.

**Virtual Mode** |br|
Simulates robot behavior without hardware movement.  
Ideal for API testing, motion verification, and software development.

**Real Mode** |br|
Executes actual robot motion with servo control enabled.  
Requires physical connection, safety checks, and access authority.

Before running any example, ensure that the correct mode is selected  
and that the controller has successfully completed initialization.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   virtual_mode
   real_mode
