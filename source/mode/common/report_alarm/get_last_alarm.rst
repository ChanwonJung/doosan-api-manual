.. _get_last_alarm:

get_last_alarm
------------------------------------------
This function checks the latest log and alarm code that occurred in the robot controller.

It returns a pointer to a structure containing detailed alarm information,  
such as the group, level, index, and message parameters.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 744)

.. code-block:: cpp

    LPLOG_ALARM get_last_alarm()
    {
        return _get_last_alarm(_rbtCtrl);
    };

**Parameter** |br|
None

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - :ref:`LOG_ALARM <struct_log_alarm>` *
     - 	Refer to definition of structure

**Example**

.. code-block:: cpp

    LPLOG_ALARM pLogAlarm = Drfl.get_last_alarm();
    switch(pLogAlarm->_iGroup)
    {
        case LOG_GROUP_SYSTEMFK:
            switch(pLogAlarm->_iLevel)
            {
                case LOG_LEVEL_SYSINFO:
                    cout << "index(" << pLogAlarm->_iIndex << "), ";
                    cout << "param(" << pLogAlarm->_szParam[0] << "), ";
                    cout << "param(" << pLogAlarm->_szParam[1] << "), ";
                    cout << "param(" << pLogAlarm->_szParam[2] << ")" << endl;
                    break;

                default:
                    break;
            }
            break;

        default:
            break;
    }

This example retrieves the most recent alarm from the controller and  
prints its group, level, index, and parameter values to the console.  
You can use this function to monitor error states or diagnose robot system issues.
