.. _struct_MONITORING_FORCECONTROL:

MONITORING_FORCECONTROL
=======================

This structure provides **real-time monitoring data for force control mode**,  
including button state, external task force/torque, temperature, and control status.  
It is mainly used to observe **compliance / force control behavior** and the current robot dynamics.

.. list-table::
   :widths: 10 28 15 10 37
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_iActualBS``
     - ``unsigned char[NUMBER_OF_BUTTON]``
     - -
     - Digital button states |br|
       (0: off, 1: on)
   * - 6
     - ``_fActualCS``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Current sensor values per joint
   * - 30
     - ``_fSingularity``
     - ``float``
     - -
     - Singularity index (minimum singular value)
   * - 34
     - ``_fToolActualETT``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Tool coordinate external force/torque (Fx, Fy, Fz, Tx, Ty, Tz)
   * - 58
     - ``_iForceControlMode``
     - ``unsigned char[NUMBER_OF_JOINT]``
     - 0-2
     - Force control mode per joint |br|
       (0: Compliance, 1: Force, 2: None)
   * - 64
     - ``_iReferenceCoord``
     - ``unsigned char``
     - 0-120
     - Reference coordinate |br|
       (0: Base, 1: Tool, 2: World, 101-120: User)
   * - 65
     - ``_iAutoAccMode``
     - ``unsigned char``
     - 0/1
     - Auto acceleration mode flag
   * - 66
     - ``_fActualHDT``
     - ``float[NUMBER_OF_JOINT]``
     - -
     - Reducer (harmonic drive) temperature (°C)
   * - 90
     - ``_iSingularHandlingMode``
     - ``unsigned char``
     - -
     - Singular handling mode flag
   * - 91
     - ``_isMoving``
     - ``unsigned char``
     - -
     - Robot moving status |br|
       (0: stopped, 1: moving)
   * - 92
     - ``_iOperationSpeed``
     - ``unsigned char``
     - 0-100
     - Current operation speed percentage
   * - 93
     - ``reserved``
     - ``unsigned char``
     - -
     - Reserved for future use

Total size: 94 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _MONITORING_FORCECONTROL
   {
       unsigned char _iActualBS[NUMBER_OF_BUTTON];     /* Digital button state */
       float          _fActualCS[NUMBER_OF_JOINT];     /* Current sensor */
       float          _fSingularity;                   /* Singularity index */
       float          _fToolActualETT[NUMBER_OF_JOINT];/* Tool Coord External Task Force/Torque */
       unsigned char  _iForceControlMode[NUMBER_OF_JOINT]; /* 0:Compliance, 1:Force, 2:None */
       unsigned char  _iReferenceCoord;                /* 0:Base, 1:Tool, 2:World, 101~120:User */
       unsigned char  _iAutoAccMode;                   /* Auto acceleration mode flag */
       float          _fActualHDT[NUMBER_OF_JOINT];    /* Reducer temperature */
       unsigned char  _iSingularHandlingMode;          /* Singular Handling Mode */
       unsigned char  _isMoving;                       /* Moving status (0:stop, 1:move) */
       unsigned char  _iOperationSpeed;                /* Operation speed (0–100%) */
       unsigned char  reserved;                        /* Reserved */
   } MONITORING_FORCECONTROL, *LPMONITORING_FORCECONTROL;

.. note::
   - ``_iForceControlMode``: per-joint control type (0 = compliance, 1 = force, 2 = none)  
   - ``_fToolActualETT``: task-space external wrench (Fx, Fy, Fz, Tx, Ty, Tz)  
   - ``_fActualHDT``: reducer temperature values, useful for thermal monitoring  
   - ``_fSingularity``: helps detect near-singular kinematic configurations  
   - This structure is typically used in **force control / compliance** operations.
