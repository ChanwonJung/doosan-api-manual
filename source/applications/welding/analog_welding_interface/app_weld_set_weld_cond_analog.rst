.. _app_weld_set_weld_cond_analog:

app_weld_set_weld_cond_analog
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1012)

.. code-block:: cpp

    bool app_weld_set_weld_cond_analog(CONFIG_ANALOG_WELDING_SETTING pConfigAnalogWeldingSetting)
    {
        return _app_weld_set_weld_cond_analog(_rbtCtrl, pConfigAnalogWeldingSetting);
    };

**Features**

This function sets the **analog welding conditions**.  
These conditions are only valid within the welding section defined from activation  
(:ref:`app_weld_enable_analog <app_weld_enable_analog>`).

The welding process parameters (``weld_proc_param``) define detailed conditions such as gas preflow/postflow time, welding start current, and voltage profiles during the welding process.

Only one welding condition is allowed within a single welding section.  
During welding, these conditions can be dynamically adjusted using  
:ref:`app_weld_adj_welding_cond_analog <app_weld_adj_welding_cond_analog>` command,  
or by tuning voltage, feeding speed, and weave offset from the teaching pendant’s condition panel.

However, condition adjustment from the pendant is possible only when  
the welding condition adjustment state is **RESET**,  
that is, when the welding parameters were last configured via  
``app_weld_set_weld_cond_analog()``.

The welding current output varies depending on wire feed speed, base material, and welding voltage.  
These must be monitored through the welder or a connected current sensor for stability.

**Arguments**

.. list-table::
   :widths: 25 25 20 30
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - pConfigAnalogWeldingSetting
     - :ref:`CONFIG_ANALOG_WELDING_SETTING <struct_CONFIG_ANALOG_WELDING_SETTING>`
     - -
     - Analog welding setting structure

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

    // CONFIG_ANALOG_WELDING_SETTING Structure Initialization
    CONFIG_ANALOG_WELDING_SETTING config;

    config._iVirtualWelding  = 0;       // 0 = real welding mode
    config._fTargetVoltage   = 200.0;   // Target voltage (V)
    config._fTargetCurrent   = 150.0;   // Target current (A)
    config._fTargetVel       = 10.0;    // Target feeding speed (mm/s)
    config._fMinVel          = 10.0;    // Minimum feeding speed (mm/s)
    config._fMaxVel          = 100.0;   // Maximum feeding speed (mm/s)

    // Detailed timing & condition settings
    config._fDetail._fMs     = 0.5;     // Ratio start
    config._fDetail._fTss    = 0.3;     // Shielding gas release time
    config._fDetail._fIas    = 2.0;     // Start current time
    config._fDetail._fMc     = 1.6;     // Welding condition changed time
    config._fDetail._fRt     = 0.7;     // Ratio finish
    config._fDetail._fMc2    = 0.4;     // Current time
    config._fDetail._fTsf    = 0.7;     // Terminated shielding gas release time
    config._fDetail._fStartVoltage = 0.6;   // Start voltage condition
    config._fDetail._fEndVoltage   = 1.5;   // Terminated voltage condition
    config._fTargetFeedingSpeed    = 0.0;   // Target feeding speed

    // Apply analog welding settings
    bool result = Drfl.app_weld_set_weld_cond_analog(config);

This example initializes an analog welding condition configuration that defines  
target voltage/current, wire feeding speed, and timing parameters for a full welding cycle.  
It ensures stable arc ignition and shutdown control suitable for automated MIG/TIG welding operations.
