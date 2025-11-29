.. _enum_popup_response:

POPUP_RESPONSE
------------------------------------------
This is an enumeration constant that means user interaction with pop-up message.  
It is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - POPUP_RESPONSE_STOP
     - Stop Task

   * - 1
     - POPUP_RESPONSE_RESUME
     - Resume Task

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       POPUP_RESPONSE_STOP,
       POPUP_RESPONSE_RESUME
   } POPUP_RESPONSE;
