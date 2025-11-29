.. _enum_safety_func:

SAFETY_FUNC
------------------------------------------
It is an enumerated constant that defines the safety functions of the robot controller, such as stop modes, error detections, and safety signals, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SAFETY_FUNC_FIRST
     - Start index of safety function enumeration

   * - 1
     - SAFETY_FUNC_STOP_STO_NOT_USE
     - STO (Safe Torque Off) not used

   * - 2
     - SAFETY_FUNC_STOP_SBC_NOT_USE
     - SBC (Safe Brake Control) not used

   * - 3
     - SAFETY_FUNC_STOP_SS1_NOT_USE
     - SS1 (Safe Stop 1) not used

   * - 4
     - SAFETY_FUNC_STOP_SS2_NOT_USE
     - SS2 (Safe Stop 2) not used

   * - 5
     - SAFETY_FUNC_SIGNAL_EMG
     - Emergency stop signal

   * - 6
     - SAFETY_FUNC_SIGNAL_PRS
     - Protective stop signal

   * - 7
     - SAFETY_FUNC_ERROR_SOS
     - SOS (Safe Operating Stop) error

   * - 8
     - SAFETY_FUNC_ERROR_JOINT_SLP
     - Joint position limit error

   * - 9
     - SAFETY_FUNC_ERROR_JOINT_SLS
     - Joint speed limit error

   * - 10
     - SAFETY_FUNC_ERROR_JOINT_SLT
     - Joint torque limit error

   * - 11
     - SAFETY_FUNC_ERROR_COLLISION
     - Collision detection error

   * - 12
     - SAFETY_FUNC_ERROR_TCP_SLP
     - TCP position limit error

   * - 13
     - SAFETY_FUNC_ERROR_TCP_SLO
     - TCP orientation limit error

   * - 14
     - SAFETY_FUNC_ERROR_TCP_SLS
     - TCP speed limit error

   * - 15
     - SAFETY_FUNC_ERROR_TCP_SLF
     - TCP force limit error

   * - 16
     - SAFETY_FUNC_ERROR_MOMENTUM
     - TCP momentum limit error

   * - 17
     - SAFETY_FUNC_ERROR_POWER
     - Power limit error

   * - 18
     - SAFETY_FUNC_LAST
     - Reserved for the last safety function index

   * - 19
     - SAFETY_FUNC_ENABLE_SWITCH_RELEASE
     - Enable switch release function (same as SAFETY_FUNC_LAST)

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       SAFETY_FUNC_FIRST,
       SAFETY_FUNC_STOP_STO_NOT_USE = SAFETY_FUNC_FIRST,
       SAFETY_FUNC_STOP_SBC_NOT_USE,
       SAFETY_FUNC_STOP_SS1_NOT_USE,
       SAFETY_FUNC_STOP_SS2_NOT_USE,
       SAFETY_FUNC_SIGNAL_EMG,
       SAFETY_FUNC_SIGNAL_PRS,
       SAFETY_FUNC_ERROR_SOS,
       SAFETY_FUNC_ERROR_JOINT_SLP, /* joint position */
       SAFETY_FUNC_ERROR_JOINT_SLS, /* joint speed */
       SAFETY_FUNC_ERROR_JOINT_SLT, /* joint torque */
       SAFETY_FUNC_ERROR_COLLISION,
       SAFETY_FUNC_ERROR_TCP_SLP,  /* tcp position */
       SAFETY_FUNC_ERROR_TCP_SLO,  /* tcp orientation */
       SAFETY_FUNC_ERROR_TCP_SLS,  /* tcp speed */
       SAFETY_FUNC_ERROR_TCP_SLF,  /* tcp force */
       SAFETY_FUNC_ERROR_MOMENTUM,
       SAFETY_FUNC_ERROR_POWER,
       SAFETY_FUNC_LAST,
       SAFETY_FUNC_ENABLE_SWITCH_RELEASE = SAFETY_FUNC_LAST
   } SAFETY_FUNC;
