.. _app_weld_weave_cond_zigzag:

app_weld_weave_cond_zigzag
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1004)

.. code-block:: cpp

    bool app_weld_weave_cond_zigzag(float fOffsetY, float fOffsetZ, float fGradient, float fWeavingWidth, float fWeavingCycle)
    {
        return _app_weld_weave_cond_zigzag(_rbtCtrl, fOffsetY, fOffsetZ, fGradient, fWeavingWidth, fWeavingCycle);
    };

**Features**

This function sets the zigzag weaving conditions.  
These conditions are only valid within the welding section defined from weld activation  
(:ref:`app_weld_enable_analog <app_weld_enable_analog>` / :ref:`app_weld_enable_digital <app_weld_enable_digital>`)  
to deactivation (:ref:`app_weld_disable_digital <app_weld_disable_digital>`),  
and an error will occur if executed outside of this section.

Weaving conditions are defined in the weave coordinate system, where the direction of the weld path is the weave x-axis, and the direction of the vector product (cross-product) of the weave x-axis and the TCP-Z direction is the weave y-axis. Refer to the figure below for the coordinate system and weave setting parameters.

Only one weaving condition is allowed within a single welding section. During welding, you can adjust the offset or weaving width using the :ref:`app_weld_adj_welding_cond_analog <app_weld_adj_welding_cond_analog>` / :ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>` command, or adjust the (voltage/current/speed and) offset from the welding condition adjustment popup on the teaching pendant. However, adjusting the welding conditions from the teaching pendant is only possible when the welding condition adjustment state is RESET (i.e., the welding condition setting specified by :ref:`app_weld_set_weld_cond_analog <app_weld_set_weld_cond_analog>` / :ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>`).

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
   * - fWeavingWidth
     - float
     - 5.0
     - Weaving width (mm)
   * - fWeavingCycle
     - float
     - 0.7
     - Weaving cycle (sec)

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

    float fOffsetY      = 0.0;
    float fOffsetZ      = 0.0;
    float fGradient     = 0.0;
    float fWeavingWidth = 5.0;
    float fWeavingCycle = 0.7;

    Drfl.app_weld_weave_cond_zigzag(fOffsetY, fOffsetZ, fGradient, fWeavingWidth, fWeavingCycle);

This example configures a symmetric zigzag weave (5 mm width, 0.7 s cycle) with no plane tilt and zero Y/Z offsets.  
Use this as a baseline and tune width/cycle to control bead width and heat input for your material and travel speed.
