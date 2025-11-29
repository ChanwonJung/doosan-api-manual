5.7 Program Execution and Shutdown
===================================

When the program is shut out due to inside/outside errors, or normally, the program stop 
(drl_stop) command must be executed, and as some time is required for complete internal 
shutdown of the program, shutdown of the program must be checked in the callback function 
for program shutdown (TOnProgramStoppedCB), and then program is restarted if needed.

Also, if the program is set as virtual robot system and program execution is shut down, the 
program is converted into the actual robot system. Therefore, caution should be paid.