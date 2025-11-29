.. _struct_SAFETY_ZONE_PROPERTY_LOCAL_ZONE:

SAFETY_ZONE_PROPERTY_LOCAL_ZONE
===============================

This structure defines **comprehensive local safety zone properties**,  
allowing the configuration of **individual behavior overrides** and **safety reactions**  
within a specific local zone of the robot workspace.  
Each field provides an option to locally override the global safety configuration.

This structure integrates joint, TCP, and collision parameters,  
as well as control flags for LED indication, nudge function, and collaborative workspace modes.

.. list-table::
   :widths: 10 28 20 8 34
   :header-rows: 1

   * - **BYTE#**
     - **Field Name**
     - **Data Type**
     - **Value**
     - **Remarks**
   * - 0
     - ``_tJointRangeOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_JOINT_RANGE <struct_LOCAL_ZONE_PROPERTY_JOINT_RANGE>`
     - -
     - Override for joint range limits (min/max).
   * - 76
     - ``_tJointSpeedOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_JOINT_SPEED <struct_LOCAL_ZONE_PROPERTY_JOINT_SPEED>`
     - -
     - Override for joint speed limits.
   * - 108
     - ``_tTcpForceOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_TCP_FORCE <struct_LOCAL_ZONE_PROPERTY_TCP_FORCE>`
     - -
     - Override for TCP force.
   * - 113
     - ``_tTcpPowerOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_TCP_POWER <struct_LOCAL_ZONE_PROPERTY_TCP_POWER>`
     - -
     - Override for TCP power.
   * - 118
     - ``_tTcpSpeedOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_TCP_SPEED <struct_LOCAL_ZONE_PROPERTY_TCP_SPEED>`
     - -
     - Override for TCP speed.
   * - 123
     - ``_tTcpMomentumOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_TCP_MOMENTUM <struct_LOCAL_ZONE_PROPERTY_TCP_MOMENTUM>`
     - -
     - Override for TCP momentum.
   * - 128
     - ``_tCollisionOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_COLLISION <struct_LOCAL_ZONE_PROPERTY_COLLISION>`
     - -
     - Override for collision detection sensitivity.
   * - 133
     - ``_tSpeedRate``
     - :ref:`LOCAL_ZONE_PROPERTY_SPEED_RATE <struct_LOCAL_ZONE_PROPERTY_SPEED_RATE>`
     - -
     - Override for robot motion speed rate.
   * - 138
     - ``_tCollisionViolationStopmodeOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE <struct_LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE>`
     - -
     - Override for stop behavior when a collision occurs.
   * - 140
     - ``_tForceViolationStopmodeOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE <struct_LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE>`
     - -
     - Override for stop behavior during TCP or self-limit events.
   * - 142
     - ``_tToolOrientationLimitOverride``
     - :ref:`LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION <struct_LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION>`
     - -
     - Override for tool orientation limit (direction and maximum deviation angle).
   * - 159
     - ``_iDynamicZoneEnable``
     - ``unsigned char``
     - 0~8
     - Dynamic zone enable option. |br|
       0: Disable, 1~8: Mapped to safety input channel. |br|
   * - 160
     - ``_iLedOverride``
     - ``unsigned char``
     - 0~2
     - LED indicator control. |br|  
       0: Not used, 1: Green, 2: Yellow
   * - 161
     - ``_iNundgeEanble``
     - ``unsigned char``
     - 0 or 1
     - Enables or disables nudge functionality.
   * - 162
     - ``_iAllowLessSafeWork``
     - ``unsigned char``
     - 0 or 1
     - Allows less safe operations (e.g., relaxed limits) when active.
   * - 163
     - ``_iOverrideReduce``
     - ``unsigned char``
     - 0 or 1
     - Ignore or apply global reduce mode.
   * - 164
     - ``_iInsideZoneDectection``
     - ``unsigned char``
     - 0~8
     - Inside zone detection option. |br| 
       0: Not used, 1~8: Safety input channel index. |br|
   * - 165
     - ``_bCollaborativeZone``
     - ``unsigned char``
     - 0 or 1
     - Collaborative workspace flag.
   * - 166
     - ``_tReservedBuffer[58]``
     - ``unsigned char[58]``
     - -
     - Reserved for internal use and future expansion. |br|  
       Includes flags for: |br|  
       - Collaborative workspace |br| 
       - Collision mute zone |br| 
       - Tool orientation limit zone |br| 
       - Clamping prevention zone |br|

Total size: 224 bytes

**Defined in:** ``DRFS.h``

.. code-block:: cpp

   typedef struct _SAFETY_ZONE_PROPERTY_LOCAL_ZONE
   {
       LOCAL_ZONE_PROPERTY_JOINT_RANGE        _tJointRangeOverride;
       LOCAL_ZONE_PROPERTY_JOINT_SPEED        _tJointSpeedOverride;
       LOCAL_ZONE_PROPERTY_TCP_FORCE          _tTcpForceOverride;
       LOCAL_ZONE_PROPERTY_TCP_POWER          _tTcpPowerOverride;
       LOCAL_ZONE_PROPERTY_TCP_SPEED          _tTcpSpeedOverride;
       LOCAL_ZONE_PROPERTY_TCP_MOMENTUM       _tTcpMomentumOverride;
       LOCAL_ZONE_PROPERTY_COLLISION          _tCollisionOverride;
       LOCAL_ZONE_PROPERTY_SPEED_RATE         _tSpeedRate;
       LOCAL_ZONE_PROPERTY_COLLISION_STOPMODE _tCollisionViolationStopmodeOverride;
       LOCAL_ZONE_PROPERTY_TCPSLF_STOPMODE    _tForceViolationStopmodeOverride;
       LOCAL_ZONE_PROPERTY_TOOL_ORIENTATION   _tToolOrientationLimitOverride;

       unsigned char _iDynamicZoneEnable;
       unsigned char _iLedOverride;
       unsigned char _iNundgeEanble;
       unsigned char _iAllowLessSafeWork;
       unsigned char _iOverrideReduce;
       unsigned char _iInsideZoneDectection;
       unsigned char _bCollaborativeZone;

       unsigned char _tReservedBuffer[58];
   } SAFETY_ZONE_PROPERTY_LOCAL_ZONE, *LPSAFETY_ZONE_PROPERTY_LOCAL_ZONE;

.. note::
   - This structure allows **fine-grained local overrides** for all major safety parameters.  
   - Useful for defining **collaborative work areas**, **restricted zones**,  
     or **sensitive environments** with unique safety responses.  
   - The reserved buffer provides compatibility with future versions,  
     ensuring forward extensibility of the local zone property schema.
