.. _enum_safety_state:

SAFETY_STATE
------------------------------------------
It is an enumerated constant for setting the subsequent operation at the time of a protective stop, and is defined as follows.

.. list-table::
   :header-rows: 1
   :widths: 5 30 65

   * - Rank
     - Constant Name
     - Description

   * - 0
     - SAFETY_STATE_BP_START
     - boot-up start

   * - 1
     - SAFETY_STATE_BP_INIT
     - boot-up init(config)

   * - 2
     - SAFETY_STATE_VD_STO
     - motor stop

   * - 3
     - SAFETY_STATE_VD_SOS
     - standby

   * - 4
     - SAFETY_STATE_JH_SOS
     - jog & homing stop

   * - 5
     - SAFETY_STATE_JH_MOVE
     - jog & homing move

   * - 6
     - SAFETY_STATE_HG_MOVE
     - hand guiding move

   * - 7
     - SAFETY_STATE_RV_SOS
     - recovery standby

   * - 8
     - SAFETY_STATE_RV_MOVE
     - recovery move

   * - 9
     - SAFETY_STATE_RV_BACK
     - backdrive mode

   * - 10
     - SAFETY_STATE_RV_HG_MOVE
     - recovery mode hand guiding

   * - 11
     - SAFETY_STATE_SW_SOS
     - standalone workspace standby

   * - 12
     - SAFETY_STATE_SW_RUN
     - standalone workspace move

   * - 13
     - SAFETY_STATE_CW_SOS
     - collaborative workspace standby

   * - 14
     - SAFETY_STATE_CW_RUN
     - collaborative workspace run

   * - 15
     - SAFETY_STATE_CM_RUN
     - collision mute run

   * - 16
     - SAFETY_STATE_AM_RUN
     - auto-measure run

   * - 17
     - SAFETY_STATE_DRL_JH_SOS
     - DRL jog & homing standby

   * - 18
     - SAFETY_STATE_DRL_HG_MOVE
     - hand guiding move

   * - 19
     - SAFETY_STATE_LAST
     - Reserved for the last safety state index

**Defined in:** ``DRFC.h``  

.. code-block:: cpp

   typedef enum {
       SAFETY_STATE_BP_START,        /* boot-up start */
       SAFETY_STATE_BP_INIT,         /* boot-up init(config) */
       SAFETY_STATE_VD_STO,          /* violation detected STO */
       SAFETY_STATE_VD_SOS,          /* violation detected SOS */
       SAFETY_STATE_JH_SOS,          /* jog & homing SOS */
       SAFETY_STATE_JH_MOVE,         /* jog & homing MOVE */
       SAFETY_STATE_HG_MOVE,         /* hand guiding MOVE */
       SAFETY_STATE_RV_SOS,          /* recovery SOS */
       SAFETY_STATE_RV_MOVE,         /* recovery MOVE */
       SAFETY_STATE_RV_BACK,         /* recovery BackDrive */
       SAFETY_STATE_RV_HG_MOVE,      /* recovery hand guiding move */
       SAFETY_STATE_SW_SOS,          /* standalone workspace SOS */
       SAFETY_STATE_SW_RUN,          /* standalone workspace RUN */
       SAFETY_STATE_CW_SOS,          /* collaborative workspace SOS */
       SAFETY_STATE_CW_RUN,          /* collaborative workspace RUN */
       SAFETY_STATE_CM_RUN,          /* collision mute RUN */
       SAFETY_STATE_AM_RUN,          /* auto-measure RUN */
       SAFETY_STATE_DRL_JH_SOS,      /* DRL jog & homing SOS */
       SAFETY_STATE_DRL_HG_MOVE,     /* hand guiding MOVE */
       SAFETY_STATE_LAST
   } SAFETY_STATE;
