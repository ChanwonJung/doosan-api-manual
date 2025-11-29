.. _app_weld_weave_cond_trapezoidal:

app_weld_weave_cond_trapezoidal
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1002)

.. code-block:: cpp

    bool app_weld_weave_cond_trapezoidal(CONFIG_TRAPEZOID_WEAVING_SETTING pConfigtrapezoidweavingsetting) 
    { 
        return _app_weld_weave_cond_trapezoidal(_rbtCtrl, pConfigtrapezoidweavingsetting); 
    };

**Features**

This function sets the trapezoidal weaving conditions.  
These conditions are only valid within the welding section defined from weld activation  
(:ref:`app_weld_enable_analog <app_weld_enable_analog>` / :ref:`app_weld_enable_digital <app_weld_enable_digital>`)  
to deactivation (:ref:`app_weld_disable_digital <app_weld_disable_digital>`),  
and an error will occur if executed outside of this section.

Weaving conditions are defined in the weave coordinate system, where the direction of the weld path is the weave x-axis, and the direction of the vector product (cross-product) of the weave x-axis and the TCP-z direction is the weave y-axis. 

Refer to the figure below for the coordinate system and weave setting parameters.

.. figure:: /tutorials/images/welding/app_weld_weave_cond_trapezoidal.png
   :alt: app_weld_weave_cond_trapezoidal
   :width: 100%
   :align: center

   *Source by* `ResearchGate — "Weaving parameters of weaving welding" <https://www.researchgate.net/figure/Weaving-parameters-of-weaving-welding_fig1_360913664>`_
   
**Weaving Coordinate System and Parameters**

Only one weaving condition is allowed within a single welding section.  
During welding, you can adjust the **offset or weaving width** using  
:ref:`app_weld_adj_welding_cond_analog <app_weld_adj_welding_cond_analog>` /
:ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>` command,  
or adjust the **voltage/current/speed** and offset using the welding condition popup on the teaching pendant.  

However, adjusting weaving conditions from the pendant is only possible when the condition adjustment state is **RESET**,  
i.e., the condition was last set by :ref:`app_weld_set_weld_cond_digital <app_weld_set_weld_cond_digital>`.

**Arguments**

.. list-table::
   :widths: 20 20 15 45
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - wv_offset
     - float[2]
     - [0, 0]
     - [0] Weave coordinate y-axis offset (mm) |br| [1] Weave coordinate z-axis offset (mm)
   * - wv_angle
     - float
     - 0
     - Rotation angle of the weaving plane with respect to the weave x-axis (deg)
   * - wv_param
     - list(float[10])
     - [0, 1.5, 0, -1.5, 0.3, 0.1, 0.3, 0.3, 0.1, 0.3]
     - 
       [0] Weaving point 1 - X (mm) |br|
       [1] Weaving point 1 - Y (mm) |br|
       [2] Weaving point 2 - X (mm) |br|
       [3] Weaving point 2 - Y (mm) |br|
       [4] Weaving point 1 → 2 time (sec) |br|
       [5] Acceleration/deceleration time (sec) |br|
       [6] Weaving point 1 dwell time (sec) |br|
       [7] Weaving point 2 → 1 time (sec) |br|
       [8] Acceleration/deceleration time (sec) |br|
       [9] Weaving point 2 dwell time (sec)

**Return**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Value**
     - **Description**
   * - ``0``
     - Error
   * - ``1``
     - Success

**Example**

.. code-block:: cpp

    CONFIG_TRAPEZOID_WEAVING_SETTING weaving_trap;

    weaving_trap.fOffsetY = 0.0;
    weaving_trap.fOffsetZ = 0.0;
    weaving_trap.fAngle = 0.0;

    weaving_trap.fParam[0] = 0.0;   // Weaving point 1 - X
    weaving_trap.fParam[1] = 1.5;   // Weaving point 1 - Y
    weaving_trap.fParam[2] = 0.0;   // Weaving point 2 - X
    weaving_trap.fParam[3] = -1.5;  // Weaving point 2 - Y
    weaving_trap.fParam[4] = 0.3;   // 1→2 transition time
    weaving_trap.fParam[5] = 0.1;   // Accel/decel time
    weaving_trap.fParam[6] = 0.3;   // Point 1 dwell time
    weaving_trap.fParam[7] = 0.3;   // 2→1 transition time
    weaving_trap.fParam[8] = 0.1;   // Accel/decel time
    weaving_trap.fParam[9] = 0.3;   // Point 2 dwell time

    Drfl.app_weld_weave_cond_trapezoidal(weaving_trap);

This example defines a trapezoidal weave path that oscillates between ±1.5 mm  
in the y-direction with a 0.3 s dwell and smooth acceleration, suitable for thin sheet welding.
