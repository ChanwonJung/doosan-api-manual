.. _set_accx_rt:

set_accx_rt
------------------------------------------
This function sets the **global task-space acceleration limit** for  
**real-time servo motion control**.  
It defines both **linear** and **rotational** acceleration limits applied to task-level commands  
such as :ref:`servol_rt <servol_rt>` or :ref:`speedl_rt <speedl_rt>`.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 595)

.. code-block:: cpp

   bool set_accx_rt(float fTransAcc, float fRotationAcc = -10000) {
       return _set_accx_rt(_rbtCtrlUDP, fTransAcc, fRotationAcc);
   };

**Parameter**

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fTransAcc
     - float
     - -
     - Task linear acceleration limit [mm/s²].
   * - fRotationAcc
     - float
     - -10000
     - Task rotational acceleration limit [deg/s²].  |br|
       If set to **-10000**, it is automatically calculated  
       based on the task linear acceleration limit.

**Note**

- If the **servo motion acceleration** exceeds the defined global task-space limit,  
  an **Info message** is generated for diagnostic purposes.  
- This does not interrupt motion automatically, but warns the operator  
  to prevent instability during real-time streaming.  
- The rotational acceleration is automatically scaled if not explicitly defined.

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 1
     - Success — acceleration limits successfully applied.
   * - 0
     - Error — invalid input parameter or UDP communication failure.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   #include <iostream>
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;
       drfl.connect_rt_control("192.168.137.100", 12347);

       // Define task-space acceleration limits
       float fTransAcc = 100.0f;      // Linear acceleration [mm/s²]
       float fRotationAcc = 50.0f;    // Rotational acceleration [deg/s²]

       // Apply global acceleration limits for real-time servo control
       if (drfl.set_accx_rt(fTransAcc, fRotationAcc))
           std::cout << "Task-space acceleration limits set successfully." << std::endl;
       else
           std::cout << "Failed to apply task acceleration limits." << std::endl;

       drfl.disconnect_rt_control();
       return 0;
   }

This example sets the **global task acceleration limit**  
to 100 mm/s² for translation and 50 deg/s² for rotation,  
ensuring stable motion under real-time control.

**Tips**

- Use together with :ref:`set_velx_rt <set_velx_rt>` to maintain  
  consistent dynamic behavior in Cartesian control.  
- Recommended to define limits before starting real-time servo commands  
  to avoid excessive acceleration or overshoot during motion blending.
