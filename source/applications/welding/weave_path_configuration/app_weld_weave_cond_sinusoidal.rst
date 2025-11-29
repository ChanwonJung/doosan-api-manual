.. _app_weld_weave_cond_sinusoidal:

app_weld_weave_cond_sinusoidal
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1008)

.. code-block:: cpp

    bool app_weld_weave_cond_sinusoidal(float fOffsetY, float fOffsetZ, float fGradient, float fWeavingWidth, float fWeavingCycle)
    {
        return _app_weld_weave_cond_sinusoidal(_rbtCtrl, fOffsetY, fOffsetZ, fGradient, fWeavingWidth, fWeavingCycle);
    };

**Features**

This function sets the sine (sinusoidal) weaving conditions.  
The weaving conditions are only valid within the welding section defined from weld activation  
(:ref:`app_weld_enable_analog <app_weld_enable_analog>` / :ref:`app_weld_enable_digital <app_weld_enable_digital>`)  
to deactivation (:ref:`app_weld_disable_digital <app_weld_disable_digital>`),  
and an error will occur if executed outside of this section.

Weaving conditions are defined in the weave coordinate system,  
where the direction of the welding path is the **weave x-axis**,  
and the direction obtained by the cross-product of the weave x-axis and the TCP z-direction  
is the **weave y-axis**.  

Only one weaving condition is allowed within a single welding section.  
During welding, you can adjust the offset or weaving width using  
:ref:`app_weld_adj_welding_cond_analog <app_weld_adj_welding_cond_analog>` /
:ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>` commands,  
or adjust voltage/current/speed and offset using the welding condition adjustment popup  
on the teaching pendant.  

However, adjusting weaving conditions from the pendant is only possible when  
the welding condition adjustment state is **RESET**, i.e.,  
the condition was last set by  
:ref:`app_weld_set_weld_cond_analog <app_weld_set_weld_cond_analog>` /
:ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>`.

**Arguments**

.. list-table::
   :widths: 22 18 15 45
   :header-rows: 1

   * - **Field Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - fOffsetY
     - float
     - 0.0
     - Offset in Y direction of the weave coordinate system (mm)
   * - fOffsetZ
     - float
     - 0.0
     - Offset in Z direction of the weave coordinate system (mm)
   * - fGradient
     - float
     - 0.0
     - Rotation angle of the weaving plane based on the X-axis of the weave coordinate system (deg)
   * - fWeavingWidth
     - float
     - 3.0
     - Weaving width (mm)
   * - fWeavingCycle
     - float
     - 0.6
     - Weaving period (sec)

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
    float fWeavingWidth = 3.0;
    float fWeavingCycle = 0.6;

    Drfl.app_weld_weave_cond_sinusoidal(fOffsetY, fOffsetZ, fGradient, fWeavingWidth, fWeavingCycle);

This example sets up a **sinusoidal weaving pattern** with a 3 mm amplitude and a 0.6 s period.  
The smooth, continuous motion of a sine wave ensures consistent heat input,  
making it ideal for thin plates or aesthetic bead applications where ripple uniformity is desired.
