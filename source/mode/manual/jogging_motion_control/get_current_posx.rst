.. _manual_get_current_posx:

get_current_posx (Manual Mode)
------------------------------------------
This section describes how to use :ref:`get_current_posx <get_current_posx>` during **Manual (Teach)** operations.  
While the function is defined in **3.1 Common**, it is essential in teaching mode for **monitoring the robot’s real-time TCP position**  
in Cartesian coordinates.

**Typical usage**

- Display or log the current **tool center point (TCP)** pose while jogging or moving manually.  
- Verify alignment during teaching by reading the robot position in the selected reference frame.  
- Compare current TCP coordinates with a target or saved user frame.

.. Note::

    - The coordinate reference (e.g., **BASE**, **TOOL**, **WORLD**) depends on the parameter used when retrieving the data.  
    - Useful for on-screen feedback in pendant or custom GUI applications.

**Example: Display TCP pose during Manual Jogging**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <thread>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Assume connection, Manual mode, and servo ON are set.

       // Jog +X direction for a short duration
       drfl.jog(JOG_AXIS_TASK_X, MOVE_REFERENCE_BASE, 10.0f);
       std::this_thread::sleep_for(std::chrono::milliseconds(500));
       drfl.stop(STOP_TYPE_SLOW);
       drfl.mwait();

       // Retrieve current TCP pose in BASE coordinate system
       LPROBOT_POSX pCur = drfl.get_current_posx(COORDINATE_SYSTEM_BASE);

       printf("[Current TCP Position - BASE]\n");
       printf("X: %.2f, Y: %.2f, Z: %.2f | Rx: %.2f, Ry: %.2f, Rz: %.2f\n",
              pCur->_fX, pCur->_fY, pCur->_fZ,
              pCur->_fRx, pCur->_fRy, pCur->_fRz);

       return 0;
   }

**Tips**

- Use this function after jog or manual moves to confirm precise positioning.  
- For comparing positions between coordinate systems, combine with :ref:`coord_transform <coord_transform>`.  
- In teaching interfaces, call ``get_current_posx()`` periodically (e.g., 10–20 Hz) for smooth position feedback.
