.. _set_singularity_handling:

set_singularity_handling
------------------------------------------
This function configures the robot's **response policy for handling singularities** during task motion.  
A singularity occurs when the robot's Jacobian matrix becomes ill-conditioned,  
causing instability or loss of path accuracy.  

Users can choose among different avoidance strategies to define how the controller reacts  
when encountering a singular configuration.  
By default, the robot operates in **automatic avoidance mode**, which reduces instability  
but may slightly affect path precision near singular points.

**Available modes:** |br|
- **SINGULARITY_AVOIDANCE_AVOID**: Automatic avoidance (default). |br|
- **SINGULARITY_AVOIDANCE_STOP**: Path-first stop mode. |br|
- **SINGULARITY_AVOIDANCE_VEL**: Variable velocity mode.

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 983)

.. code-block:: cpp

    bool set_singularity_handling(SINGULARITY_AVOIDANCE eMode) {
        return _set_singularity_handling(_rbtCtrl, eMode);
    };

**Parameter**

.. list-table::
   :widths: 22 20 18 40
   :header-rows: 1

   * - **Parameter Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - eMode
     - :ref:`SINGULARITY_AVOIDANCE <enum_singularity_avoidance>`  
     - SINGULARITY_AVOIDANCE_AVOID
     - Sets the singularity handling mode. 
     
**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - 0
     - Failed to update singularity handling mode.
   * - 1
     - Successfully applied the new singularity handling policy.

**Example**

.. code-block:: cpp

   #include "DRFLEx.h"
   using namespace DRAFramework;

   int main() {
       CDRFLEx drfl;

       float p1[6] = {400.0f, 500.0f, 600.0f, 0.0f, 180.0f, 0.0f};
       float p2[6] = {400.0f, 500.0f, 200.0f, 0.0f, 180.0f, 0.0f};

       // 1) Default automatic avoidance mode
       drfl.set_singularity_handling(SINGULARITY_AVOIDANCE_AVOID);
       drfl.movel(p1, 50, 50);

       // 2) Path-first stop mode for safety near singular points
       drfl.set_singularity_handling(SINGULARITY_AVOIDANCE_STOP);
       drfl.movel(p2, 30, 30);

       // 3) Variable velocity mode for smooth operation around singularities
       drfl.set_singularity_handling(SINGULARITY_AVOIDANCE_VEL);
       drfl.movel(p1, 40, 40);

       return 0;
   }

This example demonstrates how to configure the singularity handling strategy  
to balance **stability and path accuracy** during task-space motions.  
When operating near singular regions, select the appropriate mode based on  
motion priority and application safety requirements.
