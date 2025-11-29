.. _enum_monitoring_access_control:

MONITORING_ACCESS_CONTROL
------------------------------------------
This is an enumeration type constant that can check the change of control right in the robot controller, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 25 70

   * - Rank
     - Constant Name
     - Description

   * - 0
     - MONITORING_ACCESS_CONTROL_REQUEST
     - Reception of message for request of transfer of control right

   * - 1
     - MONITORING_ACCESS_CONTROL_DENY
     - Reception of message for rejection of transfer of control right

   * - 2
     - MONITORING_ACCESS_CONTROL_GRANT
     - Reception of message for acquisition of control right

   * - 3
     - MONITORING_ACCESS_CONTROL_LOSS
     - Reception of message for loss of control right

   * - 4
     - MONITORING_ACCESS_CONTROL_LAST
     - Internal end marker of the MONITORING_ACCESS_CONTROL enumeration. |br|  
       It does **not represent an actual state**, but defines the total number |br| 
       of valid monitoring control states for internal use.

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       MONITORING_ACCESS_CONTROL_REQUEST,
       MONITORING_ACCESS_CONTROL_DENY,                
       MONITORING_ACCESS_CONTROL_GRANT,
       MONITORING_ACCESS_CONTROL_LOSS,
       MONITORING_ACCESS_CONTROL_LAST
   } MONITORING_ACCESS_CONTROL;
