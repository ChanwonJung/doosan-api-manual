.. _speedj:

speedj (Auto Mode)
------------------------------------------
It is an **asynchronous type motion** command and executes the next command at the same time as the motion starts. 
It is a motion that follows within the maximum speed and acceleration set for the most recent target joint speed among commands transmitted continuously.

Also, this API is valid only in **Auto (Run) mode**. It is **not available in Manual (Teach) mode**.

**Definition** |br|
``DRFLEx.h`` within class ``CDRFLEx``, public section (line 815)

.. code-block:: cpp

   bool speedj(float fTargetVel[NUM_JOINT],
               float fTargetAcc[NUM_JOINT],
               float fTargetTime)
   {
       return _speedj(_rbtCtrl, fTargetVel, fTargetAcc, fTargetTime);
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
     - Target joint velocity for six axes [deg/s or rad/s per system setting].
   * - fTargetAcc
     - float[6]
     - -
     - Joint acceleration [deg/s² or rad/s²].
   * - fTargetTime
     - float
     - -
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

       // Define joint velocity and acceleration
       float jvel[6] = {10.f, 10.f, 10.f, 10.f, 10.f, 10.f};
       float jacc[6] = {20.f, 20.f, 20.f, 20.f, 20.f, 20.f};

       // Execute velocity control in joint space
       drfl.speedj(jvel, jacc, -10000.f);

       return 0;
   }

.. Note::

  - If ``fTargetTime`` is entered but cannot be maintained due to the maximum speed or acceleration condition,  
    it automatically adjusts and displays a notification message.  
  - If you want to **stop gradually**, set ``fTargetVel = {0,0,0,0,0,0}`` or call ``stop()``.  
  - For safety, if no new ``speedj`` command is received for **0.1 sec** during motion,  
    an **error message is displayed and motion stops automatically**.  
  - ``speedj`` is **not linked** with the operation speed adjustment function ``change_operation_speed()``.  
  - Recommended for **continuous joint velocity control**, **trajectory following**, or **real-time motion update loops**.
