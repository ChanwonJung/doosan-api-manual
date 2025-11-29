.. _app_weld_adj_welding_cond_analog:

app_weld_adj_welding_cond_analog
------------------------------------------

**Definition** |br|
``DRFLEx.h`` within class `CDRFLEx`, public section (line 1014)

.. code-block:: cpp

    bool app_weld_adj_welding_cond_analog(unsigned char bRealTime, unsigned char bResetFlag, float fTargetVol, float fFeedingVel, float fTargetVel, float fOffsetY, float fOffsetZ, float fWidthRate)
    {
        return _app_weld_adj_welding_cond_analog(_rbtCtrl, bRealTime, bResetFlag, fTargetVol, fFeedingVel, fTargetVel, fOffsetY, fOffsetZ, fWidthRate);
    };

**Features**

This function adjusts **welding and weaving conditions** during analog welding.  
It is typically used immediately before executing motion commands such as  
``movej()``, ``movel()``, ``movec()``, ``movesx()``, when you need to update  
the welding conditions dynamically for each motion segment.

When adjustment parameters are sent using this command,  
the system updates the corresponding **welding and weave parameters** in real time.  
While this command is active, you cannot manually adjust the same parameters  
through the Teaching Pendant (TP) welding monitor interface.

To revert to the original conditions (e.g., those set by  
:ref:`app_weld_set_weld_cond_analog <app_weld_set_weld_cond_analog>`  
or :ref:`app_weld_weave_cond_trapezoidal <app_weld_weave_cond_trapezoidal>`),  
execute the command with ``bResetFlag = 1``.  

When ``bResetFlag`` is set to 1,  
the system restores the most recent condition defined in the TP (Teaching Pendant),  
and the **real-time weaving ratio (fWidthRate)** is reset to its original value (1.0).  
This allows further manual condition adjustment from the TP interface.

**Arguments**

.. list-table::
   :widths: 20 15 15 50
   :header-rows: 1

   * - **Argument Name**
     - **Data Type**
     - **Default Value**
     - **Description**
   * - bRealTime
     - unsigned char
     - 0
     - **Mode selection** |br|
       0: Present (apply immediately) |br|
       1: Real-time update
   * - bResetFlag
     - unsigned char
     - -
     - **Reset flag**
       0: Apply new adjusted values |br|
       1: Restore values from :ref:`app_weld_set_weld_cond_analog <app_weld_set_weld_cond_analog>`
   * - fTargetVol
     - float
     - -
     - Target welding voltage (V)
   * - fFeedingVel
     - float
     - -
     - Target wire feeding speed (m/min)
   * - fTargetVel
     - float
     - -
     - Target welding speed (mm/s). |br| 
       *Note:* The TP uses cm/min units, ensure conversion when necessary.
   * - fOffsetY
     - float
     - -
     - Y-direction offset in weave coordinate system (mm)
   * - fOffsetZ
     - float
     - -
     - Z-direction offset in weave coordinate system (mm)
   * - fWidthRate
     - float
     - -
     - Ratio of modified weaving width (0.0 – 2.0)

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

    // app_weld_adj_welding_cond_analog usage example
    unsigned char bRealTime  = 0;   // Apply adjustment immediately
    unsigned char bResetFlag = 0;   // Do not reset, apply new settings

    float fTargetVol   = 200.0;     // Target voltage (V)
    float fFeedingVel  = 8.0;       // Wire feeding speed (m/min)
    float fTargetVel   = 10.0;      // Welding speed (mm/s)
    float fOffsetY     = 0.5;       // Weave offset in Y (mm)
    float fOffsetZ     = 0.3;       // Weave offset in Z (mm)
    float fWidthRate   = 1.2;       // Increase weave width by 20%

    bool result = Drfl.app_weld_adj_welding_cond_analog(
        bRealTime, bResetFlag, fTargetVol, fFeedingVel,
        fTargetVel, fOffsetY, fOffsetZ, fWidthRate
    );

This example demonstrates real-time adjustment of welding voltage, wire feed speed,  
and weave offset during analog welding.  
Setting ``fWidthRate = 1.2`` widens the weave by 20%, useful for filling wider joints  
or compensating for positional errors during robotic weld execution.
