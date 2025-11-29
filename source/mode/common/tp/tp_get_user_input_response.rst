.. _tp_get_user_input_response:

tp_get_user_input_response
------------------------------------------
This function transfers the user input information to the controller  
when a user input is requested during DRL program operation.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 681)

.. code-block:: cpp

    bool tp_get_user_input_response(string strUserInput)
    {
        return _tp_get_user_input_response(_rbtCtrl, strUserInput.c_str());
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - strUserInput
     - string
     - -
     - 256-byte string containing the user's input message. |br|
       The string is sent as a response to a `tp_get_user_input` request  
       during DRL program execution.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed — unable to send user input response.
   * - 1
     - Success — user input response successfully delivered.

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Simulate: DRL command "tp_get_user_input" is called
        std::cout << "[DRL Popup] Enter your name: ";
        std::string userInput;
        std::getline(std::cin, userInput);

        // Send user response to controller
        Drfl.tp_get_user_input_response(userInput);
        std::cout << "Sent user input \"" << userInput << "\" to controller.\n";

        return 0;
    }

This example simulates a **user input request** triggered by the  
`tp_get_user_input` command in a DRL program.  
The operator enters a string in the console, and the input is sent back  
to the controller via `tp_get_user_input_response()`, allowing the DRL program  
to continue execution using the provided value.
