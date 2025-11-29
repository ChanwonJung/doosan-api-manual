.. _manual_get_orientation_error:

get_orientation_error (Manual Mode)
------------------------------------------
This section explains how to use :ref:`get_orientation_error <get_orientation_error>` during **Manual (Teach)** operations.  
This function calculates the **orientation difference (error)** between two poses in task space.  
It is mainly used to evaluate angular deviation between taught poses — for instance,  
to check how much the tool orientation has rotated relative to a reference direction  
during manual alignment, calibration, or frame teaching.

**Typical usage**

- Measure angular deviation between two tool orientations (e.g., before/after teaching).  
- Verify if a new taught pose maintains the desired rotation tolerance.  
- Compare TCP orientation consistency during frame or tool calibration.  
- Monitor orientation drift during hand-guided motion or force teaching.

.. Note::

    - The function only performs numerical comparison — it does **not** affect robot motion.

**Example: Compare tool orientation difference between two poses**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <cstdio>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       // Preconditions:
       // - Connection established (open_connection)
       // - Manual (Teach) mode active

       // Step 1. Define two poses in TASK coordinates
       float poseA[NUM_TASK] = {400.0f, 0.0f, 300.0f, 180.0f, 0.0f, 180.0f};
       float poseB[NUM_TASK] = {400.0f, 50.0f, 300.0f, 175.0f, 0.0f, 182.0f};

       // Step 2. Compute orientation difference about Z-axis
       float errZ = drfl.get_orientation_error(poseA, poseB, TASK_AXIS_Z);

       // Step 3. Display result
       printf("[Orientation Error] ΔRz = %.3f degrees\n", errZ);

       return 0;
   }

In this example, two TCP poses are compared using :ref:`get_orientation_error <get_orientation_error>`,  
and the angular deviation around the **Z-axis** is computed.  
This allows users to check if the taught point maintains orientation accuracy  
within a specified rotational tolerance before saving or proceeding with calibration.

**Tips**

- Use for **tolerance validation** in frame or tool calibration workflows.  
- Combine with :ref:`coord_transform <manual_coord_transform>` to compare orientations across frames.  
- When the error exceeds a threshold (e.g., ±2°), consider re-teaching or refining approach paths.  
- Compare multiple axes (X, Y, Z) sequentially to analyze full 3D rotational deviation.
