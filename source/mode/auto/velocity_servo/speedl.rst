.. _speedl:

speedl (Auto Mode)
------------------------------------------
It is an **asynchronous type motion command** and executes the next command at the same time as the motion starts.  
This function performs **Cartesian velocity control**, following the most recent target TCP (Tool Center Point) velocity  
within the maximum speed and acceleration constraints of consecutive commands.

Also, this API operates only in **Auto (Run) mode**. It is **not available in Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 816)

.. code-block:: cpp

   bool speedl(float fTargetVel[NUM_TASK],
               float fTargetAcc[2],
               float fTargetTime)
   {
       return _speedl(_rbtCtrl, fTargetVel, fTargetAcc, fTargetTime);
   }

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTargetVel
     - float[6]
     - -
     - Target TCP velocity for six Cartesian axes [X, Y, Z, Rx, Ry, Rz].
   * - fTargetAcc
     - float[2]
     - -
     - Translational and rotational acceleration [mm/s², deg/s²].
   * - fTargetTime
     - float
     - 0.0f
     - Command duration [sec]. Automatically adjusted if infeasible.

**Return**

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed
   * - 1
     - Success

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       // Preconditions: Connected, servo ON, Auto mode active

       // Define linear velocity and acceleration in Cartesian space
       float jvel[6] = {10.f, 10.f, 10.f, 10.f, 10.f, 10.f};
       float jacc[2] = {20.f, 20.f};

       // Execute TCP velocity control
       drfl.speedl(jvel, jacc, -10000.f);

       return 0;
   }

.. Note::

  - If ``fTargetTime`` is entered but cannot be maintained due to the maximum speed or acceleration condition,  
    it automatically adjusts and displays a notification message.  
  - For safety, if no new ``speedl`` command is transmitted within **0.1 seconds** during motion,  
    the controller raises an **error** and stops motion.  
  - ``speedl`` is **not linked** with the ``change_operation_speed()`` function.  
  - It is also **not linked** with ``force/stiffness control`` commands.  
  - Recommended for **smooth Cartesian velocity control**, **real-time motion streaming**, or **external controller synchronization**.
