.. _app_weld_weave_cond_circular:

app_weld_weave_cond_circular
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1006)

.. code-block:: cpp

    bool app_weld_weave_cond_circular(float fOffsetY, float fOffsetZ, float fGradient, float fwWdt[2], float fwT[2])
    {
        return _app_weld_weave_cond_circular(_rbtCtrl, fOffsetY, fOffsetZ, fGradient, fwWdt, fwT);
    };

**Features**

This function sets the circular weaving conditions.  
These conditions are only valid within the welding section defined from weld activation  
(:ref:`app_weld_enable_analog <app_weld_enable_analog>` / :ref:`app_weld_enable_digital <app_weld_enable_digital>`)  
to deactivation ( :ref:`app_weld_disable_digital <app_weld_disable_digital>`),  
and executing it outside this section will result in an error.

Weaving conditions are defined in the weave coordinate system, where:

- The direction of the weld path is the **weave x-axis**.  
- The direction of the vector product (cross-product) of the weave x-axis and the TCP-z direction is the **weave y-axis**.  

Only one weaving condition is allowed within a single welding section.  
You can adjust the **offset or weaving width** during welding using  
:ref:`app_weld_adj_welding_cond_analog <app_weld_adj_welding_cond_analog>` /
:ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>` commands,  
or modify voltage/current/speed and offset from the teaching pendant’s condition popup.  

However, adjusting weaving conditions from the pendant is possible only when  
the adjustment state is **RESET**, i.e., when the condition was last set by  
:ref:`app_weld_set_weld_cond_analog <app_weld_set_weld_cond_analog>` /
:ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>`.

**Arguments**

.. list-table::
   :widths: 22 18 15 45
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fOffsetY
     - float
     - 0.0
     - Offset in the Y direction of the weave coordinate system (mm)
   * - fOffsetZ
     - float
     - 0.0
     - Offset in the Z direction of the weave coordinate system (mm)
   * - fGradient
     - float
     - 0.0
     - Rotation angle of the weaving plane with respect to the X-axis of the weave coordinate system (deg)
   * - fwWdt
     - float[2]
     - {3.0, 3.0}
     - [0] Weaving width 1 (mm) |br| [1] Weaving width 2 (mm)
   * - fwT
     - float[2]
     - {0.3, 0.3}
     - [0] Weaving cycle 1 (sec) |br| [1] Weaving cycle 2 (sec)

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

    float fOffsetY   = 0.0;
    float fOffsetZ   = 0.0;
    float fGradient  = 0.0;
    float fwWdt[2]   = {3.0, 3.0};  // Weaving widths for circular motion
    float fwT[2]     = {0.3, 0.3};  // Corresponding weaving cycle times

    Drfl.app_weld_weave_cond_circular(fOffsetY, fOffsetZ, fGradient, fwWdt, fwT);

This example defines a circular weave pattern with 3 mm radius oscillations and  
0.3-second cycles, generating smooth circular motion ideal for corner welding or  
rotational symmetry joints where uniform heat distribution is required.
