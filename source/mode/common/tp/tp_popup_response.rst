.. _tp_popup_response:

tp_popup_response
------------------------------------------
This function controls the next operation (**stop** or **resume** of a paused program)  
based on the user's response to a popup message that appeared during DRL program execution.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 680)

.. code-block:: cpp

    bool tp_popup_response(POPUP_RESPONSE eRes)
    {
        return _tp_popup_response(_rbtCtrl, eRes);
    };

**Parameter**

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eRes
     - :ref:`POPUP_RESPONSE <enum_popup_response>`
     - -
     - Response value from the popup window.

**Return**

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed — unable to process the popup response.
   * - 1
     - Success — popup response successfully processed.

**Example**

.. code-block:: cpp

    #include "DRFLEx.h"
    #include <iostream>
    using namespace DRAFramework;

    int main() {
        CDRFLEx Drfl;

        // Simulate: DRL program triggers a popup (e.g., "Continue operation?")
        std::cout << "[DRL Popup] Continue operation? (1 = Resume, 0 = Cancel): ";
        int userInput;
        std::cin >> userInput;

        // Send response to DRL popup based on user input
        if (userInput == 1) {
            Drfl.tp_popup_response(POPUP_RESPONSE_RESUME);
            std::cout << "User selected RESUME — continuing program execution.\n";
        } else {
            Drfl.tp_popup_response(POPUP_RESPONSE_STOP);
            std::cout << "User selected STOP — halting DRL execution.\n";
        }

        return 0;
    }

This example simulates handling a **DRL popup event** that requires user confirmation.  
The program prompts for input and sends a corresponding response  
(`RESUME` or `STOP`) using `tp_popup_response()`, allowing the DRL program  
to either **continue or terminate** based on the user’s decision.
