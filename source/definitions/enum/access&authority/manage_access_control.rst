.. _enum_manage_access_control:

MANAGE_ACCESS_CONTROL
------------------------------------------
This is an enumeration type constant that can obtain and change control right of the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MANAGE_ACCESS_CONTROL_FORCE_REQUEST
     - Transmission of message for forced collection of control right

   * - 1
     - MANAGE_ACCESS_CONTROL_REQUEST
     - Transmission of message for request of transfer of control right

   * - 2
     - MANAGE_ACCESS_CONTROL_RESPONSE_YES
     - Transmission of message for permission of transfer of control right

   * - 3
     - MANAGE_ACCESS_CONTROL_RESPONSE_NO
     - Transmission of message for rejection of transfer of control right

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MANAGE_ACCESS_CONTROL_FORCE_REQUEST,
       MANAGE_ACCESS_CONTROL_REQUEST,
       MANAGE_ACCESS_CONTROL_RESPONSE_YES,
       MANAGE_ACCESS_CONTROL_RESPONSE_NO,
   } MANAGE_ACCESS_CONTROL;
