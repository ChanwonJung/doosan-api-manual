.. _config_program_watch_variable:

config_program_watch_variable
------------------------------------------
This function is used to set the variable name to be monitored in order to monitor  
the internal variables of the program when it is executed in the robot controller.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 984) 

.. code-block:: cpp

    bool config_program_watch_variable(VARIABLE_TYPE eDivision, DATA_TYPE eType, 
                                       string strName, string strData) { 
        return _config_program_watch_variable(_rbtCtrl, eDivision, eType, 
                                               strName.c_str(), strData.c_str()); 
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eDivision
     - :ref:`VARIABLE_TYPE <enum_variable_type>`
     - -
     - Refer to the Definition of Enumeration Type
   * - eType
     - :ref:`DATA_TYPE <enum_data_type>`
     - -
     - Refer to the Definition of Enumeration Type
   * - strName
     - string
     - -
     - 128-byte variable name string.
   * - strData
     - string
     - -
     - 128-byte data string.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed
   * - 1
     - Success

**Example**

.. code-block:: cpp

   #include <iostream>
   #include <string>
   using namespace std;

   int main()
   {
       // Register a float-type variable "var1" to monitor in TP
       bool result = drfl.config_program_watch_variable(VARIABLE_TYPE_GLOBAL,
                                                        DATA_TYPE_FLOAT,
                                                        "var1",
                                                        "1.22");

       if (result)
       {
           cout << "[SUCCESS] Variable 'var1' registered for watch." << endl;
           cout << "You can now monitor it from the Teach Pendant Watch tab." << endl;
       }
       else
       {
           cerr << "[ERROR] Failed to configure TP watch variable." << endl;
       }

       // Example: add another variable to observe
       drfl.config_program_watch_variable(VARIABLE_TYPE_PROGRAM,
                                          DATA_TYPE_INT,
                                          "cycle_count",
                                          "10");

       return 0;
   }

When called, this function registers the specified variable to the **Teach Pendant (TP) Watch panel**,  
allowing the user to **monitor or debug variable values in real time** during DRL program execution.  
Multiple variables can be configured to track program parameters such as speed, torque, or cycle counters.
