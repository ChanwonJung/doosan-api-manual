.. _manual_set_singularity_handling:

set_singularity_handling (Manual Mode)
------------------------------------------
When teaching or jogging in Cartesian space, wrist singularities can cause **unstable orientation flips**.  
Use :ref:`set_singularity_handling <set_singularity_handling>` to configure how the controller reacts  
when approaching such configurations, ensuring smoother and safer manual teaching.

**Typical usage**

- Prevent wrist or elbow flips near singular configurations.  
- Switch to **STOP** mode for safety or **VEL** mode for continuous smooth operation.  
- Commonly used when the operator observes TCP instability during fine motion near workspace limits.

.. Note::

    - Default mode: ``SINGULARITY_AVOIDANCE_AVOID`` (smooth avoidance).  
    - Affects only **Cartesian (task-space)** moves.  
    - Does not affect direct joint jog commands.

**Example: Avoiding Wrist Flip During Manual Jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Step 1: Set singularity handling to velocity reduction mode
       drfl.set_singularity_handling(SINGULARITY_AVOIDANCE_VEL);

       // Step 2: Jog near singularity region (e.g., wrist fully extended)
       drfl.jog(JOG_AXIS_TASK_Z, MOVE_REFERENCE_BASE, 10.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(800));
       drfl.stop(STOP_TYPE_SLOW);

       printf("Jog completed safely with singularity handling enabled.\n");

       return 0;
   }

**Tips**

- Use **STOP** mode for operator safety in high-risk orientation changes.  
- Use **VEL** mode for maintaining path continuity with reduced speed.  
- Combine with :ref:`get_current_rotm <manual_get_current_rotm>` to visualize TCP orientation near singularity regions.
