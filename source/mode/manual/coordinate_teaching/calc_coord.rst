.. _manual_calc_coord:

calc_coord (Manual Mode)
------------------------------------------
This section explains how to use :ref:`calc_coord <calc_coord>` during **Manual (Teach)** operations.  
It computes a **user frame (pose)** from a small set of measured poses (points / vectors), so you can validate or refine a workpiece frame **without** permanently writing it.  

Typical use is to probe 2–4 points on a surface, compute an orthonormal frame, then verify by transforming and comparing positions.

**Typical usage**

- Quickly derive a **temporary work frame** from 3 points (origin, X-direction point, XY-plane point).  
- Use the **2-vector method** (X-vector + Y-vector + origin) to align the TCP with known fixture directions.  
- Validate an existing frame by recomputing and comparing with :ref:`coord_transform <coord_transform>` before saving.

.. Note::

    - All input poses are arrays in the order ``[X, Y, Z, Rx, Ry, Rz]`` and are interpreted in ``eTargetRef`` (e.g., **BASE**).

**Example: 3-point plane probing → compute frame → verify with a test point**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   #include <cstdio>
   using namespace DRAFramework;

   // Helper: copy ROBOT_TASK_POSE into a float[6] buffer
   static void copy_pos6(float out[6], const LPROBOT_TASK_POSE p) {
       out[0] = p->_fX;  out[1] = p->_fY;  out[2] = p->_fZ;
       out[3] = p->_fRx; out[4] = p->_fRy; out[5] = p->_fRz;
   }

   int main() {
       CDRFLEx drfl;
       // Assume: connected, Manual mode, servo ON, safe workspace.

       // --- Step 1. Touch three points on a flat workpiece (BASE frame) ---
       // O: intended frame origin (corner), Xp: point along +X, Yp: point within XY plane
       float O[6], Xp[6], Yp[6], Zz[6] = {0};  // Zz unused for 3-point
       {
           // Operator jogs to the corner (origin) and records
           // (In your GUI: bind a button to snapshot current pos)
           auto pO  = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
           copy_pos6(O, pO);
           printf("Captured Origin O: (%.3f, %.3f, %.3f)\n", O[0], O[1], O[2]);

           // Jog along the edge that defines +X
           // (small jog here is illustrative; real flow uses pendant jogging)
           drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 5.0f);
           std::this_thread::sleep_for(std::chrono::milliseconds(600));
           drfl.stop(STOP_TYPE_SLOW); drfl.mwait();
           auto pXp = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
           copy_pos6(Xp, pXp);
           printf("Captured X-edge Xp: (%.3f, %.3f, %.3f)\n", Xp[0], Xp[1], Xp[2]);

           // Move within the surface to define XY plane (+Y direction)
           drfl.jog(JOG_AXIS_TASK_Y, MOVE_REFERENCE_BASE, 5.0f);
           std::this_thread::sleep_for(std::chrono::milliseconds(600));
           drfl.stop(STOP_TYPE_SLOW); drfl.mwait();
           auto pYp = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
           copy_pos6(Yp, pYp);
           printf("Captured Y-plane Yp: (%.3f, %.3f, %.3f)\n", Yp[0], Yp[1], Yp[2]);
       }

       // --- Step 2. Compute a frame from the three captured points ---
       // nCnt = 3, nInputMode = (3-point method; see your enum), eTargetRef = BASE
       unsigned short nCnt = 3;
       unsigned short nInputMode = /* INPUT_MODE_3POINT */ 0; // Refer to constants
       LPROBOT_POSE pFrame = drfl.calc_coord(
           nCnt, nInputMode, COORDINATE_SYSTEM_BASE,
           O, Xp, Yp, Zz /* unused in 3-point */
       );

       printf("\nComputed Frame (pose in BASE):\n");
       printf("X: %.3f  Y: %.3f  Z: %.3f  Rx: %.3f  Ry: %.3f  Rz: %.3f\n",
              pFrame->_fPosition[0], pFrame->_fPosition[1], pFrame->_fPosition[2],
              pFrame->_fPosition[3], pFrame->_fPosition[4], pFrame->_fPosition[5]);

       // --- Step 3. Verify: transform a nearby measured point into the new frame ---
       float testP[6];
       {
           // Take a fresh measurement (e.g., another corner/feature near the origin)
           auto pTest = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);
           copy_pos6(testP, pTest);
       }
       // Transform BASE->UserFrame (preview). For a permanent save, use set_user_cart_coord2/3.
       // Here we only sanity-check by seeing if coordinates look local to the new frame.
       auto pLocal = drfl.coord_transform(testP, COORDINATE_SYSTEM_BASE, COORDINATE_SYSTEM_USER);
       // (Note: The active "USER" frame depends on controller state; for preview,
       //  compare relative deltas against O/Xp/Yp manually or apply your own math.)

       printf("\nTest point in target frame (preview):\n");
       printf("x: %.3f  y: %.3f  z: %.3f  rx: %.3f  ry: %.3f  rz: %.3f\n",
              pLocal->_fX, pLocal->_fY, pLocal->_fZ,
              pLocal->_fRx, pLocal->_fRy, pLocal->_fRz);

       // --- Step 4. (Optional) If satisfied, persist via set_user_cart_coord2/3 ---
       // e.g., set_user_cart_coord2({O, Xp, Yp}, O, COORDINATE_SYSTEM_BASE);

       return 0;
   }

**Tips**

- For **3-point**: pick points with good spacing; avoid nearly collinear samples to reduce numerical noise.  
- For **2-vector**: normalize source vectors and verify they are not nearly parallel.  
- Use :ref:`get_current_rotm <manual_get_current_rotm>` and :ref:`get_orientation_error <get_orientation_error>` to check orthogonality and alignment drift before saving.  
- If you intend to **save** this frame, compute/verify with ``calc_coord`` first, then persist with :ref:`set_user_cart_coord2 <set_user_cart_coord2>` / :ref:`set_user_cart_coord3 <set_user_cart_coord3>`.
