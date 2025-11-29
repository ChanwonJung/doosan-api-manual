.. _enable_alter_motion:

enable_alter_motion
------------------------------------------
``enable_alter_motion()`` and :ref:`alter_motion <alter_motion>` functions enable to alter motion trajectory.

This function sets the configurations for altering function and allows the input quantity of alter_motion() to be applied to motion trajectory. The unit cycle time of generating alter motion is 100msec. Cycle time(iCycleTime*100msec) can be changed through input parameter n. This function provide 2 modes(Accumulation mode, Increment mode). Input quantity of alter_motion() can be applied to motion trajectory in two ways as accumulated value or increment value. In accumulation mode, the input quantity means absolute altering amount(dX,dY,dZ,dRX,dRY,dRZ) from current motion trajectory.

On the contrary in increment mode, the quantity means increment value from the previous absolute altering amount. The reference coordinate can be changed through input parameter ref. Limitations of accumulation amout and increment amount can be set through input paramet fLimitDpos (accumulated limit) and fLimitDposPer(increment input limit during 1 cycle). The actual alter amount is limited to these limits.

This function is only available in M2.4 version or higher.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 980)

.. code-block:: cpp

    bool enable_alter_motion(int iCycleTime,
                             PATH_MODE ePathMode,
                             COORDINATE_SYSTEM eTargetRef,
                             float fLimitDpos[2],
                             float fLimitDposPer[2]) {
        return _enable_alter_motion(_rbtCtrl, iCycleTime, ePathMode, eTargetRef, fLimitDpos, fLimitDposPer);
    };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - iCycleTime
     - int
     - -
     - Update period for alter motion (in milliseconds). |br|
       Defines how frequently position deltas are applied.
   * - ePathMode
     - :ref:`PATH_MODE <enum_path_mode>`
     - -
     - Path interpolation mode.
   * - eTargetRef
     - :ref:`COORDINATE_SYSTEM <enum_coordinate_system>`
     - -
     - Coordinate frame in which alter motion commands are applied. |br|
       Typical values: ``COORDINATE_SYSTEM_BASE``, ``COORDINATE_SYSTEM_TOOL``.
   * - fLimitDpos
     - float[2]
     - -
     - Maximum translation limits. |br|
       [0]: Linear displacement limit (mm) |br|
       [1]: Orientation change limit (deg)
   * - fLimitDposPer
     - float[2]
     - -
     - Incremental velocity or acceleration limits per cycle. |br|
       [0]: Linear speed limit (mm/s) |br|
       [1]: Angular speed limit (deg/s)

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Error
   * - 1
     - Success

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // 1) Enable alter motion mode (20 ms cycle)
       float limitDpos[2] = {5.0f, 3.0f};       // max linear/orient displacement
       float limitDposPer[2] = {0.5f, 0.3f};    // per-cycle delta limits
       drfl.enable_alter_motion(20, PATH_MODE_JOINT, COORDINATE_SYSTEM_TOOL,
                                limitDpos, limitDposPer);

       // 2) Apply small delta adjustments while motion is running
       for (int i = 0; i < 50; ++i) {
           float delta[6] = {0.1f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f};
           drfl.alter_motion(delta);
           std::this_thread::sleep_for(std::chrono::milliseconds(20));
       }

       // 3) Disable alter motion mode after fine-tuning
       drfl.disable_alter_motion();

       return 0;
   }

This example demonstrates how to **activate alter motion**, apply small position corrections at each control cycle,  
and safely disable it after the fine-tuning process.  
Note that `alter_motion()` can be used only after `enable_alter_motion()` is called successfully,  
and must be executed within the configured limits for displacement and orientation.
